from mediacomp.sound import *
import tkinter as tk
from tkinter import filedialog
import math
import  array
from mediacomp.GUI.canvas import *

def pickAFile():
    root = tk.Tk()
    root.withdraw()
    r = filedialog.askopenfilename()
    root.destroy()
    return r

def play(sound):
    sound.play(1,-1)

def makeSound(path):
    sound = None
    try:
        sound = Sound(path)
    except:
        print("No file path!")
    return sound

def getSampleValueAt(sound, index):
    return sound.samples.values[index].value

def getSamples(sound):
    return sound.samples

def getSample(sample):
    return sample.value

def setSample(sample, value):
    sample.changeValue(int(value))

def writeSoundTo(sound,path):
    sound.save(path)

def setSampleValueAt(sound, index, value):
    sound.samples.values[index].changeValue(int(value))

def getLength(sound):
    return len(sound.samples.values)

def getSound(sample):
    return sample.samples.sound

def getSamplingRate(sound):
    return sound.sampleRate

def playAtRate(sound, rate):
    sound.play(rate, -1)

def playAtRateDur(sound, rate, duration):
    print("Not implemented yet")
    sound.play(rate, -1)

def blockingPlay(sound, rate, duration):
    print("Not implemented yet")

def getDuration(sound):
    return sound.duration;

def makeEmptySound(newLength):

    freq = 440  # of cycles per second (Hz) (frequency of the sine waves)
    volume = 100  # percent
    data = array.array('h')  # signed short integer (-32768 to 32767) data
    sampleRate = 22050  # of samples per second (standard)
    numChan = 1  # of channels (1: mono, 2: stereo)
    dataSize = 2  # 2 bytes because of using signed short integers => bit depth = 16
    numSamplesPerCyc = int(sampleRate / freq)
    numSamples = newLength

    for i in range(numSamples):
        data.append(0)

    path = 'tempo.wav'
    f = wave.open(path, 'w')
    f.setparams((numChan, dataSize, sampleRate, numSamples, "NONE", "Uncompressed"))
    f.writeframes(data.tostring())
    f.close()
    sound = Sound(path)
    return sound

#http://stackoverflow.com/questions/6951046/pyaudio-help-play-a-file


def explore(sound):
        cav = CanvasExploreSound(sound)
