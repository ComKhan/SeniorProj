import mido
import time

import wavFuncs

msg = mido.Message('note_on', note=100, channel=0)
print(mido.get_output_names())
print(mido.get_input_names())
outport = mido.open_output('Microsoft GS Wavetable Synth 0')


def main():
    ti = 5
    myrec = wavFuncs.recording(ti)
    freq = wavFuncs.maxffthps(myrec, ti)
    while True:
        myrec, freq = wavFuncs.liverec(myrec, ti, 48000, freq)
        outport.send(mido.Message('note_on', note=int((freq-100)/700*(108-21)+21), channel=0))


main()
