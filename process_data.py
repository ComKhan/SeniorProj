from fir_filter import fir_filt
import numpy as np
from scipy.fft import fft, ifft




def process_data(process_val, chunk_process, fs):
    #filter data
    filtered_output = fir_filt(process_val)
    # get length of array for fft processing
    time_len_process = len(filtered_output)

    # get fft and its conjugate
    fft_vals = fft(filtered_output, int(time_len_process + time_len_process - 1))
    fft_conj_vals = np.conjugate(fft_vals)

    # get auto correlation for frequency detection

    # multiply fft by fft conjugate
    auto_corr_RXX = fft_vals * fft_conj_vals

    # turn array into list
    auto_corr_RXX = auto_corr_RXX.tolist()

    # shorten zero padded spectrum to actual length of its spectrum
    auto_corr_RXX = auto_corr_RXX[0:int(time_len_process + time_len_process - 1)]

    # take ifft of RXX to find rxx(time domain)
    auto_corr_rxx = np.fft.ifft(auto_corr_RXX)

    # take real values of ifft and turn them into list
    auto_corr_rxx = auto_corr_rxx.real
    auto_corr_rxx = auto_corr_rxx.tolist()

    # get rxx(0)
    energy_rxx = auto_corr_rxx[0]

    if energy_rxx == 0:
        energy_rxx = 1

    # divide by root to normalize
    auto_corr_rxx = np.divide(auto_corr_rxx, np.sqrt(energy_rxx * energy_rxx))

    # find correlation values that are greater than 0.9
    corr_vals = np.where(auto_corr_rxx >= 0.80)
    corr_len = len(corr_vals[0])

    corr_vals = [x[y] for x in corr_vals for y in range(0, int(corr_len))]
    corr_len = len(corr_vals)

    freq_found = 0
    final_freq_process = 0
    f = 0

    while freq_found == 0:
        if (corr_vals[f] >= 40) and (corr_vals[f] < 4800):
            final_freq_process = corr_vals[f]
            freq_found = 1
        f = f + 1

        if f == corr_len:
            freq_found = 1
            final_freq_process = 48000

    return filtered_output, float(fs / final_freq_process)
