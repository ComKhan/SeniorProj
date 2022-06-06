# For date and time used:
# https://www.programiz.com/python-programming/datetime/current-datetime
from scipy.io import wavfile
from datetime import datetime
import os

Fs = 4800

def storeUSB():
    if os.path.exists('/media/pi/GRMCPRXFRER/'):
        Fs, y = wavfile.read('playback.wav')
        dt = datetime.now()
        dt_string = dt.strftime("recording%d_%m_%Y_%H_%M")
        fileName = "/media/pi/GRMCPRXFRER/" + dt_string
        fileStore = open(fileName, "w")
        wavfile.write(fileName, Fs, y)
        fileStore.close()
