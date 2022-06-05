# For date and time used:
# https://www.programiz.com/python-programming/datetime/current-datetime
from scipy.io import wavfile
from datetime import datetime

Fs = 4800

def storeUSB():
    Fs, y = wavfile.read('/home/pi/Documents/SeniorProj-main/Final_Files/recording.wav')
    dt = datetime.now()
    dt_string = dt.strftime("%d_%m_%Y_%H_%M")
    fileName = "/media/pi/GRMCPRXFRER/" + dt_string
    fileStore = open(fileName, "w")
    wavfile.write(fileName, Fs, y)
    fileStore.close()
