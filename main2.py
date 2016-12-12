from mediacomp.audio import *


def echoes(delay, echoes, f):
    # fazendo o novo som
    s2 = makeSound(f)
    print("s2", getLength(s2))
    # pegando o valor final do novo original
    endCurrentSound = getLength(s2)
    # calculando o valor final do novo som
    newLength = (echoes * delay) + endCurrentSound
    #print(newLength)
    # fazendo um novo som vazio do tamnho calculado
    s1 = makeEmptySound(newLength)

    # copiando o sample para o novo som
    for i in range(1, getLength(s2)):
        setSampleValueAt(s1, i, getSampleValueAt(s2, i))

    # limpando os samples restantes
    for i in range(endCurrentSound, newLength):
        setSampleValueAt(s1, i, 0)

    echoAmplitude = 1
    for echoCount in range(1, echoes + 1):
        echoAmplitude = echoAmplitude * 0.6

        for e in range(1, getLength(s2)):
            position = e + delay * echoCount
            #print(e)
            setSampleValueAt(s1, position, getSampleValueAt(s1, position) + echoAmplitude * getSampleValueAt(s2, e))
    play(s1)

path ="C:/Users/fl43/Dropbox/MESTRADO LUIS_Concepção_Blocos/Som/recursos/preamble10.wav"

s1 = makeSound(path)
#s = makeEmptySound(getLength(s1))

samples = getSamples(s1)
explore(s1)


'''
play(s1)

for i in range(0, len(samples)):
    s = getSample(samples[i])
    setSample(samples[i] , s*0.2)

play(s1)'''

#for p in samples1:
#setSample(p, getSample(p)*0.5)
#s.dataString = s1.dataString
#print(len(s.dataString), len(s1.dataString))
