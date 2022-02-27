import pyaudio
import wave

wav_file = 'test5.wav' #file from usb_record to play

chunk = 2096
file = wave.open(wav_file, 'rb')

audio = pyaudio.PyAudio()

stream = audio.open(format = audio.get_format_from_width(file.getsampwidth()), channels = file.getnchannels(), \
                    rate = file.getframerate(), \
                    output = True)

data = file.readframes(chunk)

while data != '':
    stream.write(data)
    data = file.readframes(chunk)

print("playing")

stream.stop_stream()
stream.close()
audio.terminate()

print("end playback of file")
