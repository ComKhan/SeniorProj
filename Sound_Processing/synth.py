from scipy.io.wavfile import read, write
import matplotlib.pyplot as plt
import numpy as np
import time
import wavFuncs
import sys
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
        y = np.int16(2000 * np.sin(2 * pi * freq * x))

    plt.plot(x,y)
    plt.xlabel("Sample Number")
    plt.ylabel("Sample Amplitude")
    plt.show()
    plt.close()

plotWaveform('acousticPer.wav')
