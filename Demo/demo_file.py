import pyaudio
import wave
import numpy as np
from scipy.fft import fft, ifft
from scipy.signal import hilbert
import wave
import time
from fir_filter import fir_filt
import wave
import soundfile as sf


def process_data(process_val, chunk_process, fs):
    # use list comprehension to create a list of only single values (no tuples)
    # time_domain_vals_process = [x[y] for x in process_val for y in range(0,int(chunk_process))]
    # print('data size')


    filtered_output = fir_filt(process_val)

    # get length of array for fft processing
    time_len_process = len(filtered_output)

    # get fft and its conjugate
    fft_vals = fft(filtered_output, int(time_len_process + time_len_process - 1))
    fft_conj_vals = np.conjugate(fft_vals)

    # get auto correlation for frequency detection

    # multiply fft by fft conjugate
    auto_corr_RXX = fft_vals * fft_conj_vals

    # turn array into list
    auto_corr_RXX = auto_corr_RXX.tolist()

    # shorten zero padded spectrum to actual length of its spectrum
    auto_corr_RXX = auto_corr_RXX[0:int(time_len_process + time_len_process - 1)]

    # take ifft of RXX to find rxx(time domain)
    auto_corr_rxx = np.fft.ifft(auto_corr_RXX)

    # take real values of ifft and turn them into list
    auto_corr_rxx = auto_corr_rxx.real
    auto_corr_rxx = auto_corr_rxx.tolist()

    # get rxx(0)
    energy_rxx = auto_corr_rxx[0]

    if energy_rxx == 0:
        energy_rxx = 1

    # divide by root to normalize
    auto_corr_rxx = np.divide(auto_corr_rxx, np.sqrt(energy_rxx * energy_rxx))

    # find correlation values that are greater than 0.9
    corr_vals = np.where(auto_corr_rxx >= 0.80)
    corr_len = len(corr_vals[0])

    corr_vals = [x[y] for x in corr_vals for y in range(0, int(corr_len))]
    corr_len = len(corr_vals)

    freq_found = 0
    final_freq_process = 0
    f = 0

    while freq_found == 0:
        # compare = int(corr_vals[i])
        if (corr_vals[f] >= 40) and (corr_vals[f] < 4800):
            print(corr_vals[f])
            final_freq_process = corr_vals[f]
            freq_found = 1
        f = f + 1

        if f == corr_len:
            freq_found = 1
            final_freq_process = 48000

    return filtered_output, float(fs / final_freq_process)


# set all base requirements for class creation
# form_1 = pyaudio.paInt16
# chans = 1
# samp_rate = 48000
# chunk = 4096
# record_secs = 1
# dev_index = 1  # this is the device index (usb device specific port) connection in hardware VARIES
# wav_output_filename = 'test5.wav'
# audio = pyaudio.PyAudio()

# stream = audio.open(format=form_1, rate=samp_rate, channels=chans, \
#                     input_device_index=dev_index, input=True, \
#                     frames_per_buffer=chunk)

# print("recording")

# frames = []

# stream.start_stream()
# for i in range(0, int((samp_rate / chunk) * record_secs)):
#     data = stream.read(chunk, exception_on_overflow=False)
#     frames.append(data)

# print("finished recording")
# stream.stop_stream()
# stream.close()
# audio.terminate()

# wavefile = wave.open(wav_output_filename, 'wb')
# wavefile.setnchannels(chans)
# wavefile.setsampwidth(audio.get_sample_size(form_1))
# wavefile.setframerate(samp_rate)
# wavefile.writeframes(b''.join(frames))
# wavefile.close()





