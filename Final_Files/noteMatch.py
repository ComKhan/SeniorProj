from enum import auto
#import matplotlib.pyplot
from scipy.io.wavfile import read, write
import sounddevice as sd
import pyaudio
import wave
import numpy as np
import wavFuncs
# from demo_file import *
#from fir_filter import *
from process_data import *
from playsound import playsound
import soundfile as sf
# from btns_V1 import *

# btn1 = Button(16) #Filter, Yes
# btn2 = Button(6) # Inst
# btn3 = Button(5) # No
# btn4 = Button(0) # Output
# btn5 = Button(4) # Record
# btn6 = Button(3) # Vol Dwn
# btn7 = Button(2) # Vol Up



def matchnote(freq):

    notefreqs = [
    32.70 ,
    36.71 ,
    41.2  ,
    43.65 ,
    49.00 ,
    55.00 ,
    61.74 ,
    65.41 ,
    73.42 ,
    82.41 ,
    87.31 ,
    98.00 ,
    110.0 ,
    123.47,
    130.81,
    146.83,
    164.81,
    174.61,
    196.00,
    220.00,
    246.94,
    261.63,
    293.66,
    329.63,
    349.23,
    392.00,
    440.00,
    493.88,
    523.25,
    587.33,
    659.25,
    698.46,
    783.99,
    880.00,
    987.77 
    ]
    
    val =(np.abs(np.array(notefreqs)-freq)).argmin()
    return notefreqs[val]

def interpolate(first, second, dist):
    return first + (dist*(second-first))

def setPer(Amplitude, tfreq, instrument_file, time):
    Fs, y = read(instrument_file)
    i = 0
    output = []
    length = len(y)
    while i < Fs*time:
        output.append(Amplitude*interpolate(y[int((i*tfreq/523.25) % (length-1))],
                                            y[int(((i*tfreq/523.25) % (length-1))+1)],
                                            (i*tfreq/523.25) % 1))
        i += 1

    output = np.int16(output)

    write('setPer.wav', Fs, output)
    Fs, y = read('setPer.wav')
    
    wavFuncs.playwav('setPer.wav')
    
    return Fs, y

def autoTune(instr, match):
    chunk = 4096

    wavFuncs.recording(1)
    p_array, samplerate = sf.read("recording.wav")
    p_array = list(p_array)
    filt_out, freq = process_data(p_array, chunk, samplerate)
    if match == "AUTOTUNEMD":
        setPer(1, matchnote(freq), "periodfiles/"+instr+".wav", 1)
    else:
        setPer(1, freq, "periodfiles/"+instr+".wav", 1)
    
# while True:
#     btn1.when_pressed = clickA.clicked
#     btn2.when_pressed = clickB.clicked
#     btn3.when_pressed = clickC.clicked
#     btn4.when_pressed = clickD.clicked
#     btn5.when_pressed = clickE.clicked
#     btn6.when_pressed = clickF.clicked
#     btn7.when_pressed = clickG.clicked
#     if clickC.implement == False:
#         wavFuncs.recording(1)
#         audio = autoTune('recording.wav', 0.1)
#         clickC.implement = True
#     if clickE.implement == False:
#         break
#curl -sS https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/i2samp.sh | bash