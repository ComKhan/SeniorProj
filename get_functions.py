import multiprocessing
import rootFSM as fsm
import btns
from wav_2_list import wav_2_list

def get_data(obj, sample_rate1, chunk1, q1, data1, aud, button_press1):
    v = 0
    data1.value = 1
    print("Recording")

    # start stream
    obj.start_stream()

    # set value to count to
    while button_press1 != 0:
        # ADD INTERRUPT HERE
        fsm.btn5.when_pressed = btns.clickE.clicked

        # read data from usb mic
        val = (obj.read(chunk1, exception_on_overflow=False))

        # put data into queue
        q1.put(val)

        # incrementer to keep track of how many things were put in queue
        v = v + 1

        # data_value tells system its okay to start processing data
        data1.value = 1

        # ADD INTTERUPT HERE AS WELL
        # Uncomment if it's catching some but not all btn clicks
        # fsm.btn5.when_pressed = btns.clickE.clicked

    # setting data1.value to 0 for another condition
    data1.value = 0

    obj.stop_stream()
    obj.close()
    aud.terminate()
    print("finished recording")


def get_freq(sample_rate2, chunk2, q2, data2, f_freq, f_vol, queue_count1, aud2):
    d = 0

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
    while data2.value == 1:
        while not q2.empty():
            # pop value from queue and store in process array
            process_array.append(q2.get())

            # gueue count is used to determine how many values were popped
            store = queue_count1.value
            queue_count1.value = store + 1

            # if you've hit the desired number of seconds for processing then start run auto correlation
            if len(process_array) == 36:
                # write to a wav for processing
                time_vals,freq = wav_2_list(sample_rate2,process_array,aud2,chunk2)

                # store final frequency into shared array for processing
                f_freq[d] = freq
                # add adsr stuff
                process_array = []
                d = d + 1

    while not q2.empty():

        # add more data for processing
        process_array.append(q2.get())
        store = queue_count1.value
        queue_count1.value = store + 1
        if len(process_array) == 36:
            # write to wav
            time_vals,freq = wav_2_list(sample_rate2, process_array, aud2, chunk2)

            # vol = get_adsr(time_domain)
            final_freq[d] = freq
            # volume[i] = vol

            # clear array for next batch of processing
            process_array = []
            d = d + 1

        # if there isn't any more data to process and data hasn't been processed yet
        if (len(process_array) != 0) and (data2.value == 0):
            time_vals_freq = wav_2_list(sample_rate2, process_array, aud2, chunk2)
            # vol = get_adsr(time_domain)
            final_freq[d] = freq
            # volume[d] = vol

