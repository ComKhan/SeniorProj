import multiprocessing
from wav_2_list import wav_2_list
from noteMatch import *
from wavFuncs import *


def get_data(sample_rate1, chunk1, q1, data1):
    v = 0
    data1.value = 0
    print("Recording")

    # start stream
#     obj.start_stream()

    # set value to count to
    while v != 5:
#         # ADD INTERRUPT HERE
# 
#         # read data from usb mic
#         val = (obj.read(chunk1, exception_on_overflow=False))
# 
#         # put data into queue
#         q1.put(val)

        #CONRADS CODE
        
        liverec = recording(1)
        q1.put(liverec)


        # incrementer to keep track of how many things were put in queue
        v = v + 1

        # data_value tells system its okay to start processing data
        data1.value = 1

        # ADD INTTERUPT HERE AS WELL MAYBE

    # setting data1.value to 0 for done processing
    data1.value = 0

#     obj.stop_stream()
#     obj.close()
#     aud.terminate()
    print("finished recording")


def get_freq(sample_rate2, chunk2, q2, data2, f_freq, f_vol, queue_count1,q3, q4, flag1):
    d = 0
    flag1.value = 0

    # array where data is getting stored for processing
    process_array = []

    # time domain values array
    time_vals = []

    # frequency,volume, and store variables
    freq = 0
    vol = 0
    store = 0

    # while data != 1 and the queue is empty stay here
    while (data2.value == 0) and (q2.empty()):
        d = d + 1

    d = 0

    # now that you have data in your queue start processing
    data2.value = 1
    while data2.value == 1:
        while not q2.empty():
            # pop value from queue and store in process array
            process_array.append(q2.get())

            # gueue count is used to determine how many values were popped
            store = queue_count1.value
            queue_count1.value = store + 1

            # if you've hit the desired number of seconds for processing then start run auto correlation
            if len(process_array) == 1:
                # write to a wav for processing
                time_vals, freq = wav_2_list(sample_rate2, process_array, aud2, chunk2)

                # store final frequency into shared array for processing
                f_freq[d] = freq
                # f_vol[d] = vol

                q3.put(freq)
                # q4.put(vol)
                # add adsr stuff
                process_array = []
                d = d + 1

                # tell next process it's okay to start going
                flag1.value = 1

    while not q2.empty():

        if len(process_array) == 1:
            # write to wav
            time_vals, freq = wav_2_list(sample_rate2, process_array, aud2, chunk2)

            # vol = get_adsr(time_domain)
            f_freq[d] = freq
            # f_vol[d] = vol

            q3.put(freq)
            # q4.put(vol)

            # clear array for next batch of processing
            process_array = []
            d = d + 1

        # add more data for processing
        process_array.append(q2.get())
        store = queue_count1.value
        queue_count1.value = store + 1

        # if there isn't any more data to process and data hasn't been processed yet
    if (len(process_array) != 0) and (data2.value == 0):
        time_vals, freq = wav_2_list(sample_rate2, process_array, aud2, chunk2)
        # vol = get_adsr(time_domain)
        f_freq[d] = freq
        # f_vol[d] = vol

        q3.put(freq)
        # q4.put(vol)

    # tell next queue to stop checking for more values
    flag1.value = 0


def play_freq(q5, q6, flag2):
    increment = 0
    freq_val = 0
    vol_val = 0

    while (flag2.value == 0) and (q5.empty()):
        increment = increment + 1

    increment = 0
    flag2.value = 1
    
    while flag2.value == 1:

        if not q5.empty():
            freq_val = q5.get()
            print(freq_val)
            Tune(freq_val, 1)


        # if not q6.empty():
        # vol_val = q6.get()

        # play frequency stuff

    while not q5.empty():
        if not q5.empty():
            freq_val = q5.get()
            print(freq_val)
            Tune(freq_val, 1)

        # if not q6.empty():
        # vol_val = q6.get()

        # play frequency stuff
