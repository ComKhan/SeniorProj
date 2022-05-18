# This is Alberto's get_new_1 file but renamed when I was doing tests
import multiprocessing
import pyaudio
import numpy as np
from scipy.fft import fft,ifft
from scipy.signal import hilbert
import wave
import np2
import time
from fir_filter import fir_filt
import wave
#import soundfile as sf
#import data_sound

def process_data(process_val,chunk_process,fs):
       
    #use list comprehension to create a list of only single values (no tuples)    
    #time_domain_vals_process = [x[y] for x in process_val for y in range(0,int(chunk_process))]
    #print('data size')
    
    
 #   ff = data_sound.process_data1(time_domain_vals_process,fs)
    
    output = fir_filt(process_val)
    #get length of array for fft processing
    time_len_process = len(process_val)
    #print(time_len_process + time_len_process - 1)
#get fft and its conjugate
    fft_vals = fft(process_val,int(time_len_process+time_len_process-1))
    fft_conj_vals = np.conjugate(fft_vals)
    
#get auto correlation for frequency detection
    
    #multiply fft by fft conjugate
    auto_corr_RXX = fft_vals*fft_conj_vals
    
    #turn array into list
    auto_corr_RXX = auto_corr_RXX.tolist()
    
    #shorten zero padded spectrum to actual length of its spectrum
    auto_corr_RXX = auto_corr_RXX[0:int(time_len_process+time_len_process-1)]
     
    #take ifft of RXX to find rxx(time domain) 
    auto_corr_rxx = np.fft.ifft(auto_corr_RXX)
    
    #take real values of ifft and turn them into list
    auto_corr_rxx = auto_corr_rxx.real
    auto_corr_rxx = auto_corr_rxx.tolist()
    
    #get rxx(0)
    energy_rxx = auto_corr_rxx[0]
    
    if energy_rxx == 0:
        energy_rxx = 1
            
    #divide by root to normalize
    auto_corr_rxx = np.divide(auto_corr_rxx,np.sqrt(energy_rxx * energy_rxx))
    
    print(len(auto_corr_rxx))
    #find correlation values that are greater than 0.9
    corr_vals = np.where(auto_corr_rxx >= 0.80)
    corr_len = len(corr_vals[0])
    
    corr_vals = [x[y] for x in corr_vals for y in range(0,int(corr_len))]    
    corr_len = len(corr_vals)
    print(corr_vals)
    
    freq_found = 0
    final_freq_process = 0
    f = 0
    
    while freq_found == 0:
       # compare = int(corr_vals[i])
        if (corr_vals[f] >= 40) and (corr_vals[f] < 4800):
            print(corr_vals[f])
            final_freq_process = corr_vals[f]
            freq_found = 1
        f = f+1
        
        if f == corr_len:
            freq_found = 1
            final_freq_process = 48000
        
    return process_val, float(fs/final_freq_process)

    #return time_domain_vals_process, ff 




def get_data(obj,sample_rate1,chunk1,q1,data1,aud):
    v = 0
    data1.value =1
    print("Recording")
    while v != 74:
        obj.start_stream()
        val = (obj.read(chunk1, exception_on_overflow = False))
        q1.put(val)
        v = v+1
        data1.value =1
    data1.value = 0
    
    obj.stop_stream()
    obj.close()
    aud.terminate()
    print("finished recording")        
def get_freq(sample_rate2,chunk2,q2,data2,f_freq,f_vol,queue_count1):

    d = 0
    process_array = []
    freq = 0
    time_vals = []
    vol = 0
    store = 0
    
#     while(data2.value == 0) and (q2.empty()):
#         d = d+1
#     d =0
#     while data2.value == 1:
#         while not q2.empty():
#             print(q2.get())
#             d= d+1
#     while(data2.value == 0) and (not q2.empty):
#         print(q2.get())
#         d= d+1
#     print(d)
#             
    
    while(data2.value == 0) and (q2.empty()):
        d = d+1
    d = 0
    while data2.value == 1:
        while not q2.empty():
            process_array.append(q2.get())
            store =queue_count1.value
            queue_count1.value = store+1
            if len(process_array) == 36:
                #print([x[y] for x in process_array for y in range(0,int(chunk2))])
                wavefile = wave.open('test5.wav', 'wb')
                wavefile.setnchannels(1)
                wavefile.setsampwidth(audio.get_sample_size(8))
                wavefile.setframerate(sample_rate2)
                wavefile.writeframes(b''.join(process_array))
                wavefile.close()
                p_array,samplerate = sf.read('test5.wav')
                p_array.tolist()
                print('p_array')
                print(p_array)
                time_vals,freq = process_data(p_array,chunk2,sample_rate2)
                f_freq[d] = freq 
                #add adsr stuff
                process_array = []
                d = d+1
               
    while not q2.empty():
        process_array.append(q2.get())
        store =queue_count1.value
        queue_count1.value = store+1
        if len(process_array) == 36:
           # print(process_array)
            wavefile = wave.open('test5.wav', 'wb')
            wavefile.setnchannels(1)
            wavefile.setsampwidth(audio.get_sample_size(8))
            wavefile.setframerate(sample_rate2)
            wavefile.writeframes(b''.join(process_array))
            wavefile.close()
            p_array,samplerate = sf.read('test5.wav')
            p_array.tolist()
            print('parray')
            print(p_array)
            time_vals,freq = process_data(p_array,chunk2,sample_rate2)
            #vol = get_adsr(time_domain)
            final_freq[d] = freq
            #volume[i] = vol
   
            process_array = []
            d = d+1

        if (len(process_array) != 0) and (data2.value == 0):

            time_vals,freq = process_data(process_array,chunk2,sample_rate2)
            #vol = get_adsr(time_domain)
            final_freq[d] = freq
            #volume[d] = vol
          
          
# set all base requirements for class creation
form_1 = pyaudio.paInt16
chans = 1
samp_rate = 48000
chunk =4096
record_secs = 5
dev_index = 1   #this is the device index (usb device specific port) connection in hardware VARIES
#wav_output_filename = 'test6.wav'
audio = pyaudio.PyAudio()

stream = audio.open(format = form_1, rate = samp_rate, channels = chans, \
                    input_device_index = dev_index, input = True, \
                    frames_per_buffer = chunk)
data= multiprocessing.Value('i')
data.value= 0

queue_count = multiprocessing.Value('i')
queue_count.value = 0

final_freq = multiprocessing.Array('f',4096)
final_vol= multiprocessing.Array('i',4096)

# print(data.value)
# v = data.value
# print(type(v))
#print(type(variable))

if __name__ == "__main__":
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target = get_data,args = (stream,samp_rate,chunk,q,data,audio))
    p1 =multiprocessing.Process(target = get_freq, args = (samp_rate,chunk,q,data,final_freq,final_vol,queue_count))
   
    tic = time.time()
    p.start()
    p1.start()
    p.join()
    p1.join()
    
    toc = time.time()
    print(list(final_freq[:]))
    print(queue_count.value)
    print(toc-tic)
    i = 0
# while not q.empty():
#     print(q.get())
#     i = i +1
#     
# print(i)
# values = []
# values = get_new(stream,chunk)
# print(values)

