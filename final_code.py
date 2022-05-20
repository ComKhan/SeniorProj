import multiprocessing
import pyaudio
import wave
from get_functions1 import get_data, get_freq, play_freq



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

flag = multiprocessing.Value('i')
flag.value = 0

button_press = multiprocessing.Value('i')
button_press.value = 0

queue_count = multiprocessing.Value('i')
queue_count.value = 0

final_freq = multiprocessing.Array('f', 4096)
final_vol = multiprocessing.Array('i', 4096)

if __name__ == "__main__":
    q_get = multiprocessing.Queue()
    q_freq = multiprocessing.Queue()
    q_vol =  multiprocessing.Queue()
    p = multiprocessing.Process(target=get_data, args=(stream, samp_rate, chunk, q_get, data, audio))
    p1 = multiprocessing.Process(target=get_freq, args=(samp_rate, chunk, q_get, data, final_freq, final_vol, \
                                                        queue_count, audio, q_freq, q_vol,flag))
    p2 = multiprocessing.Process(target=play_freq, args=(q_freq, q_vol,flag))


    p.start()
    p1.start()
    p2.start()
    p.join()
    p1.join()
    p2.join()


   # print(list(final_freq[:]))