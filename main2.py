from mediacomp.audio import *

path ="C:/Users/fl43/Dropbox/MESTRADO LUIS_Concepção_Blocos/Som/recursos/preamble10.wav"

s = makeSound(path)
#play(s)
vp = getSampleValueAt(s, 1)
ss = getSamples(s)
p = getSample(ss[0])
for ssi in ss:
    setSample(ssi, getSample(ssi)/10)
#play(s)
a = getLength(s)
print(a)
#print(vp)
#print(ss[0])
sec= getSamplingRate(s)
print(sec)

playAtRate(s, 0.5)

