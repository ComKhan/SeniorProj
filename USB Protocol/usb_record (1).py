import pyaudio
import matplotlib.pyplot as plt
import numpy as np
import wave

# set all base requirements for class creation
form_1 = pyaudio.paInt16
chans = 1
samp_rate = 48000
chunk =4096
record_secs = 5
dev_index = 1   #this is the device index (usb device specific port) connection in hardware VARIES
wav_output_filename = 'test6.wav'
audio = pyaudio.PyAudio()

stream = audio.open(format = form_1, rate = samp_rate, channels = chans, \
                    input_device_index = dev_index, input = True, \
                    frames_per_buffer = chunk)

print("recording")

#create arrays for store
frames = []
array = []

#create condition for exiting streaming(like a switch) NOT NEEDED
compare = 1

#create condition for stopping randomly in code(not needed)
f = 0

#start stream
stream.start_stream()

#create a for loop to get chunks of data and store them
for i in range (0,int((samp_rate/chunk)*record_secs)):
        while compare == 1:
            if f ==  int((samp_rate/chunk)*5):
                compare = input()
                
            data = stream.read(chunk, exception_on_overflow = False)
            
            #add data to frames for .wav processing
            frames.append(data)
            
            #add data to array and convert from bytes to integer values
            array.append(np.frombuffer(data,dtype = np.int16))
            f = f+1
    
print("finished recording")

#get length of array for fft processing
length = len(array)

#get length of each tuple in list
tuple_len = chunk/16

#creat a list of values of 0-tuple len for accessing tuples in array
tuple_ar = []
for i in range(0,int(tuple_len - 1)):
    tuple_ar.append(i)
    
    
#use list comprehension to create a list of only single values (no tuples)    
final = [x[y] for x in array for y in tuple_ar]


#run fft on final list and store
fin_fft = np.fft.fft(final)

#get length of final fft
fin_len = len(fin_fft)

#create digital frequencies to match length of fft
fin_Fd = np.arange(0,1,(1/fin_len))

#create analog frequences use fs = 48000
fin_Fd = fin_Fd * 48000

#find the index analog frequencies greateer than or equal to 2000 Hz
fin_fft_cutoff = np.where(fin_Fd >= 2000)

#use list comprehension to get the first position where this occurs
fin_fft_cutoff = [x[0] for x in fin_fft_cutoff]

#turn this value from  a list to an int
fin_fft_cutoff = fin_fft_cutoff[0]

#make all analog frequency vals in fft greater than 2000 equal to zero LPF @ 2000 Hz cutoff
for i in range (0,int(fin_len)):
    if i >= fin_fft_cutoff :
        fin_fft[i] = 0
        


#find max value of fft with its index
fin_max = max(fin_fft)
fin_max_index = np.where(fin_fft == fin_max)

#find analog frequency at the fin max index
fin_freq = fin_Fd[fin_max_index]

#plot fft vs analog frequency
plt.plot(fin_Fd,abs(fin_fft))
plt.show()

print(fin_freq)
print(final)

stream.stop_stream()
stream.close()
audio.terminate()



wavefile = wave.open(wav_output_filename, 'wb')
wavefile.setnchannels(chans)
wavefile.setsampwidth(audio.get_sample_size(form_1))
wavefile.setframerate(samp_rate)
wavefile.writeframes(b''.join(frames))
wavefile.close()