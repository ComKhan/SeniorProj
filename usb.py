# Code used from : https://www.instructables.com/Raspberry-Pi-Data-Logging/
# https://betterprogramming.pub/how-to-run-a-python-script-on-insertion-of-a-usb-device-2e86d38dcdb

#import os
from scipy.io import wavfile

Fs = 4800
Fs, y = wavfile.read('/home/pi/Documents/SeniorProj-main/Piano/a0.wav')
file = open("/media/pi/GRMCPRXFRER/test.wav", "a")
i=0
#if os.stat("/home/pi/data_log.csv").st_size == 0:
wavfile.write("/media/pi/GRMCPRXFRER/test.wav", Fs, y)
#file.flush()
file.close()
