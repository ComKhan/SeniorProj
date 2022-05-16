from scipy.io.wavfile import read, write
import matplotlib.pyplot as plt
import sounddevice as sd
import numpy as np
import math
import time
import wavFuncs

def plotWaveform(sound, time = 0.05):
    if type(sound) == str:
        Fs, y = read(sound)
        try:
            if len(y[0]) > 1:
                y = y[:, 0]
        except:
            pass
        N = len(y)

    elif type(sound) == int:
        N = time * Fs

    else:
        N = time * Fs
        y = sound

    T = 1 / Fs
    N=int(N)
    x = np.linspace(0.0, N * T, N, endpoint=False)

    if type(sound) == int:
        freq = sound
        y = np.int16(2000 * np.sin(2 * math.pi * freq * x))

    plt.plot(x,y)
    plt.xlabel("Time")
    plt.ylabel("Sample Amplitude")
    plt.show()
    plt.close()


def setPer(Amplitude, tfreq, instrument_file, runtime):
    FS, y = read(instrument_file)
    print(len(y))
    afreq = FS/len(y)
    print(tfreq/afreq)
    y = y[0:int(afreq/tfreq):len(y)]
    print(len(y))
    y = [num*Amplitude for num in y]
    print(len(y))
    y = runtime/(len(y)/FS) * y
    sd.play(y, FS)
    return FS, y


setPer(1, 100, "periodfiles/pianoPer.wav", 1)