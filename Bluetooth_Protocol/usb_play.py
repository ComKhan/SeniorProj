import pyaudio
import wave

wav_file = 'test5.wav' #file from usb_record to play

chunk = 2096
audio = pyaudio.PyAudio()

stream = audio.open(format = audio.get_format_from_width(wav_file.getsampwidth()), channels = wav_file.getnchannels(), \
                    rate = wav_file.getframerate(), \
                    output = True)

data = wav_file.readframes(chunk)

while data != '':
    stream.write(data)
    data = wav_file.readframes(chunk)

print("playing")

stream.stop_stream()
stream.close()
audio.terminate()

print("end playback of file")