from mediacomp.sound import *
import tkinter as tk
from tkinter import filedialog

def pickAFile():
    root = tk.Tk()
    root.withdraw()
    r = filedialog.askopenfilename()
    root.destroy()
    return r

def play(sound):
    sound.play(1)

def makeSound(path):
    sound = None
    try:
        wf = wave.open(path, 'rb')
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
    sound.sample.values[index].changeValue(int(value))

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





#http://stackoverflow.com/questions/6951046/pyaudio-help-play-a-file
