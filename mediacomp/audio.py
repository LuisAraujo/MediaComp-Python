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

    data = sound.audio.readframes(1024)
    while len(data) != 0:
        sound.stream.write(data)
        #1024 is a chunk
        data = sound.audio.readframes(1024)
    sound.stream.close()
    sound.pa.terminate()


def makeSound(path):
    sound = None
    try:
        wf = wave.open(path, 'rb')
        sound = Sound(path, wf)
    except:
        print("No file path!")
    return sound


#http://stackoverflow.com/questions/6951046/pyaudio-help-play-a-file
