import mido
import time

import wavFuncs

msg = mido.Message('note_on', note=100, channel=0)
print(mido.get_output_names())
print(mido.get_input_names())
outport = mido.open_output('Microsoft GS Wavetable Synth 0')


def main():
    ti = .2
    myrec = wavFuncs.recording(ti)
    freq = wavFuncs.maxfft(myrec, ti)
    while True:
        myrec, freq = wavFuncs.liverec(myrec, ti, 8000, freq)
        outport.send(msg)


main()
