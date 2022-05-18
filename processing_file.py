import multiprocessing
import pyaudio
import wave
from get_functions import get_data, get_freq



# set all base requirements for class creation
form_1 = pyaudio.paInt16
chans = 1
samp_rate = 48000
chunk = 4096
record_secs = 5
dev_index = 1  # this is the device index (usb device specific port) connection in hardware VARIES
# wav_output_filename = 'test6.wav'
audio = pyaudio.PyAudio()

stream = audio.open(format=form_1, rate=samp_rate, channels=chans,  \
                    input_device_index=dev_index, input=True,  \
                    frames_per_buffer=chunk)
data = multiprocessing.Value('i')
data.value = 0

button_press = multiprocessing.Value('i')
button_press.value = 0

queue_count = multiprocessing.Value('i')
queue_count.value = 0

final_freq = multiprocessing.Array('f', 4096)
final_vol = multiprocessing.Array('i', 4096)

if __name__ == "__main__":
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=get_data, args=(stream, samp_rate, chunk, q, data, audio, button_press))
    p1 = multiprocessing.Process(target=get_freq, args=(samp_rate, chunk, q, data, final_freq, final_vol, queue_count, \
                                                        audio))
    p2 = multiprocessing.Process()


    p.start()
    p1.start()
    p.join()
    p1.join()


    print(list(final_freq[:]))