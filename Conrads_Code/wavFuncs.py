from math import pi
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write
from scipy.fft import fft, fftfreq
import numpy as np
import time as ti


def liverec(myarray, time=3, Fs=8000, freq=150):
    while True:
        myrecording = sd.rec(int(time*Fs),Fs,2)
        sd.wait()
        freqtemp = maxfft(myrecording[:,0], time)
        print(freqtemp)
        if abs(freqtemp - freq) > 20:
            break
    return myrecording, freqtemp


def maxfft(sound, time=3, Fs=8000):
    xf, yf = noplotfft(sound, time, Fs)
    N = int(time * Fs)
    ind = np.where(yf[:N // 2] == np.max(yf[:N // 2]))
    return int(xf[ind[0]])


# records a clip using the default microphone of the device
def recording(time=3, Fs=8000):
    print('Now Recording')
    myrecording = sd.rec(int(time * Fs), Fs, 2)
    sd.wait()
    print('done recording')
    write('recording.wav', Fs, myrecording)
    return myrecording[:, 0]


# Generates an Envelope for a set frequency signal

def freqADSR(freq,  # Frequency of the wave
             time=3,  # Sound duration
             ADSR1=(35, 10, 25, 30),  # Tuple of Percentages length for each section
             ADSR2=(0, 0.9, 0.7, 0.7, 0),  # Tuple of Intensity values before and after each section
             Fs=8000):  # sampling Frequency
    N = time * Fs
    T = 1 / Fs
    x = np.linspace(0.0, N * T, N, endpoint=False)
    y = np.int16(2000 * np.sin(2 * pi * freq * x))
    A = np.linspace(ADSR2[0], ADSR2[1], int(len(y) * ADSR1[0] / 100))
    D = np.linspace(ADSR2[1], ADSR2[2], int(len(y) * ADSR1[1] / 100))
    S = np.linspace(ADSR2[2], ADSR2[3], int(len(y) * ADSR1[2] / 100))
    R = np.linspace(ADSR2[3], ADSR2[4], int(len(y) * ADSR1[3] / 100))
    ADSR = np.concatenate([A, D, S, R])
    for i in range(len(y) - 1):
        y[i] = (y[i] * ADSR[i])
    write('ADSR.wav', Fs, y)
    sd.play(y, Fs)
    sd.wait()
    plt.show()


def noplotfft(sound, time=3, Fs=8000):
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

    yf = fft(y)
    xf = fftfreq(N, T)[:N // 2]
    write('FFT.wav', Fs, y)
    return xf, yf


def plotfft(sound, time=3, Fs=8000):
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

    yf = fft(y)
    xf = fftfreq(N, T)[:N // 2]
    fig, axs = plt.subplots(2, constrained_layout=True)
    axs[0].plot(xf, 2.0 / N * np.abs(yf[0:N // 2]))
    axs[0].set_xlim([0, 2000])
    axs[0].set_title('FFT')
    axs[0].set_xlabel('Frequency(Hz)')
    axs[1].plot(x, y)
    axs[1].set_title('Sound over Time')
    axs[1].set_ylabel('Amplitude')
    axs[1].set_xlabel('time(s)')
    write('FFT.wav', Fs, y)
    plt.show()


# plotfft('recording.wav')
freq = maxfft(recording(3))
print(freq)
# noplotfft('recording.wav')\
# freqADSR(freq)
# Fs, y = read('recording.wav')
# liverec(y)
