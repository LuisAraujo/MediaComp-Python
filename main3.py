import wave
import struct
import sys
'''
def wav_to_floats(wave_file):
    w = wave.open(wave_file)
    astr = w.readframes(w.getnframes())
    # convert binary chunks to short
    a = struct.unpack("%ih" % (w.getnframes()* w.getnchannels()), astr)
    return a

# read the wav file specified as first command line arg
signal = wav_to_floats('C:/Users/fl43/Dropbox/MESTRADO LUIS_Concepção_Blocos/Som/recursos/preamble10.wav')
print("read "+str(len(signal))+" frames")
print(signal[70620], type(signal[0]) == int)

print("in the range "+str(min(signal))+" to "+str(min(signal)))
'''
n = 36
a = bin(n & 0xffffffff)
print(a)
