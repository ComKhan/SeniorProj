import matplotlib.pyplot
from scipy.io.wavfile import read, write
import sounddevice as sd
import numpy as np
import wavFuncs

def matchnote(freq):
    notes = {
    32.70 :"Piano/C1.wav",
    36.71 :"Piano/D1.wav",
    41.2  :"Piano/E1.wav",
    43.65 :"Piano/F1.wav",
    49.00 :"Piano/G1.wav",
    55.00 :"Piano/A1.wav",
    61.74 :"Piano/B1.wav",
    65.41 :"Piano/C2.wav",
    73.42 :"Piano/D2.wav",
    82.41 :"Piano/E2.wav",
    87.31 :"Piano/F2.wav",
    98.00 :"Piano/G2.wav",
    110.0 :"Piano/A2.wav",
    123.47:"Piano/B2.wav",
    130.81:"Piano/C3.wav",
    146.83:"Piano/D3.wav",
    164.81:"Piano/E3.wav",
    174.61:"Piano/F3.wav",
    196.00:"Piano/G3.wav",
    220.00:"Piano/A3.wav",
    246.94:"Piano/B3.wav",
    261.63:"Piano/C4.wav",
    293.66:"Piano/D4.wav",
    329.63:"Piano/E4.wav",
    349.23:"Piano/F4.wav",
    392.00:"Piano/G4.wav",
    440.00:"Piano/A4.wav",
    493.88:"Piano/B4.wav",
    523.25:"Piano/C5.wav",
    587.33:"Piano/D5.wav",
    659.25:"Piano/E5.wav",
    698.46:"Piano/F5.wav",
    783.99:"Piano/G5.wav",
    880.00:"Piano/A5.wav",
    987.77:"Piano/B5.wav" 
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
