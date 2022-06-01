from math import pi
import wave
import pyaudio
import matplotlib.pyplot
import numpy
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write
from scipy.fft import fft, fftfreq
import numpy as np
import time as ti
import soundfile as sf


def liverec(myarray, time=0.1, Fs=48000, freq=150):
    while True:
        myrecording = sd.rec(int(time*Fs),Fs,2)
        sd.wait()
        freqtemp = maxffthps(myrecording[:,0], time)
        print(freqtemp)
        if abs(freqtemp - freq) > 10:
            break
    return myrecording, freqtemp


def maxfft(sound, time=3, Fs=48000):
    xf, yf = noplotfft(sound, time, Fs)
    N = int(time * Fs)
    ind = np.where(yf[:N // 2] == np.max(yf[:N // 2]))
    return int(xf[ind[0]])


def maxffthps(sound, time=3, Fs=48000):
    xf, yf = hps(sound, time, Fs)
    N = int(time * Fs)
    ind = np.where(yf[:N] == np.max(yf[:N]))
    return int(xf[ind[0]])


# records a clip using the default microphone of the device
def recording(time=3, Fs=48000):
    print('Now Recording')
    myrecording = sd.rec(int(time * Fs), Fs, 1)
    sd.wait()
    print('done recording')
    write('recording.wav', Fs, myrecording)
    data_array, samplerate = sf.read('recording.wav')
    #sd.play(myrecording,Fs)
    return data_array


# Generates an Envelope for a set frequency signal

def freqADSR(freq,  # Frequency of the wave
             time=3,  # Sound duration
             ADSR1=(35, 10, 25, 30),  # Tuple of Percentages length for each section
             ADSR2=(0, 0.9, 0.7, 0.7, 0),  # Tuple of Intensity values before and after each section
             Fs=48000):  # sampling Frequency
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


def noplotfft(sound, time=3, Fs=48000):
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


def hps(sound, time=0.02, Fs=48000):
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
    N = int(N)
    x = np.linspace(0.0, N * T, N, endpoint=False)

    if type(sound) == int:
        freq = sound
        y = np.int16(2000 * np.sin(2 * pi * freq * x))
#     fig, axs = plt.subplots(5, constrained_layout=True)
    yf1 = np.abs(fft(numpy.append(y,np.linspace(0, 0, 9*N))))
    xf = fftfreq(10*N, T)[:N//6]
#     axs[0].plot(xf, yf1[:N//6])
    yf2 = np.abs(yf1[0:yf1.size:2])
    yf2[N // 2] = 0
    yf2[N // 4:] = 0
#     axs[1].plot(xf, yf2[:N//6])
    yf3 = np.abs(yf1[0:yf1.size:3])
    yf3[N // 2] = 0
    yf3[N // 6:] = 0
#     axs[2].plot(xf, yf3[:N//6])
    yff = numpy.multiply(yf1[:N//6], yf2[:N//6])
    yff = numpy.multiply(yff[:N//6], yf3[:N//6])
#     axs[3].plot(xf, yff)
#     axs[4].plot(x, y)
#     matplotlib.pyplot.show()
    write('hps.wav', Fs, y)
    return xf[yff.argmax()]


def plotfft(sound, time=3, Fs=48000):
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

def playwav(fileName):
    chunk = 4096
    wf = wave.open(fileName,'rb')
    p1 = pyaudio.PyAudio()
    stream1 = p1.open(format=p1.get_format_from_width(wf.getsampwidth()),
        channels= wf.getnchannels(),
        rate=wf.getframerate(),
        output=True)
    data = wf.readframes(chunk)
    while len(data) > 0:
        stream1.write(data)
        data = wf.readframes(chunk)
    stream1.stop_stream()
    stream1.close()
    wf.close()
    p1.terminate()


#plotfft('hps.wav')
#tim = .05
#freq1 = maxfft(recording(tim), tim)
#freq2 = maxffthps('FFT.wav', tim)
#print('fft:',freq1,'\nhps:', freq2)
# noplotfft('recording.wav')\
# freqADSR(freq)
# Fs, y = read('recording.wav')
# liverec(y)
