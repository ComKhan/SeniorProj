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


def interpolate(first, second, dist):
    return first + (dist*(second-first))

def setPer(Amplitude, tfreq, instrument_file, runtime, Fs):
    FS, y = read(instrument_file)
    i = 0
    output = []
    length = len(y)
    while i < Fs*runtime:
        output.append(y[(i*tfreq//110)%length])
        i += 1

    output = np.array(output)

    sd.play(output, FS)
    return FS, y


setPer(1, 200, "periodfiles/a2Piano.wav", 1, 48000)