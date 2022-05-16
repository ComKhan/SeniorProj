import matplotlib.pyplot
from scipy.io.wavfile import read, write
import sounddevice as sd
import numpy as np
import wavFuncs

def matchnote(freq):
    notes = {
    32.70 :"Piano/c1.wav",
    36.71 :"Piano/d1.wav",
    41.2  :"Piano/e1.wav",
    43.65 :"Piano/f1.wav",
    49.00 :"Piano/g1.wav",
    55.00 :"Piano/a1.wav",
    61.74 :"Piano/b1.wav",
    65.41 :"Piano/c2.wav",
    73.42 :"Piano/d2.wav",
    82.41 :"Piano/e2.wav",
    87.31 :"Piano/f2.wav",
    98.00 :"Piano/g2.wav",
    110.0 :"Piano/a2.wav",
    123.47:"Piano/b2.wav",
    130.81:"Piano/c3.wav",
    146.83:"Piano/d3.wav",
    164.81:"Piano/e3.wav",
    174.61:"Piano/f3.wav",
    196.00:"Piano/g3.wav",
    220.00:"Piano/a3.wav",
    246.94:"Piano/b3.wav",
    261.63:"Piano/c4.wav",
    293.66:"Piano/d4.wav",
    329.63:"Piano/e4.wav",
    349.23:"Piano/f4.wav",
    392.00:"Piano/g4.wav",
    440.00:"Piano/a4.wav",
    493.88:"Piano/b4.wav",
    523.25:"Piano/c5.wav",
    587.33:"Piano/d5.wav",
    659.25:"Piano/e5.wav",
    698.46:"Piano/f5.wav",
    783.99:"Piano/g5.wav",
    880.00:"Piano/a5.wav",
    987.77:"Piano/b5.wav" 
    }

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
    return notes[notefreqs[val]]

def autoTune(soundFile, time):
    freq = wavFuncs.hps(soundFile, time)
    Fs, y = read(matchnote(freq))
    sd.play(y[:Fs], Fs)
    sd.wait()


audio = autoTune(wavFuncs.recording(1), 1)
#curl -sS https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/i2samp.sh | bash