import wave
import soundfile as sf
from process_data import process_data



def wav_2_list(sample_rate3,process_array1,aud3,chunk3):

    data_array = []


    # write to a wav for processing
    wavefile = wave.open('test5.wav', 'wb')
    wavefile.setnchannels(1)
    wavefile.setsampwidth(aud3.get_sample_size(8))
    wavefile.setframerate(sample_rate3)
    wavefile.writeframes(b''.join(process_array1))
    wavefile.close()

    # decode from .wav and turn into data list with sample rate
    data_array, samplerate = sf.read('test5.wav')
    data_array.tolist()

    # run auto_correlation on the data
    time_vals1, freq1 = process_data(data_array, chunk3, sample_rate3)

    return time_vals1,freq1