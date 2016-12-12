import pyaudio
import wave
import struct
from mediacomp.samples import *

class Sound:
    filename =""
    sampleRate = 0
    channels = 0
    sampwidth = 0
    dataString = []
    samples = None
    duration = 0

    def __init__(self, filename):
        self.filename = filename
        audio = wave.open(self.filename, 'rb')

        astr = audio.readframes(audio.getnframes())
        self.dataString = list(struct.unpack("%ih" % (audio.getnframes() * audio.getnchannels()), astr))
        self.sampleRate = audio.getframerate()
        print(len(self.dataString))

        self.channels = audio.getnchannels()
        self.sampwidth = audio.getsampwidth()
        audio.close()
        self.samples = Samples(self)
        self.duration =  len(self.samples.values)/ 22050.0
        #print(audio.getparams(), self.dataString[len(self.dataString)-1])


    def __str__(self):
        return "Sound file: {} number of samples: {} ".format(self.filename, len(self.samples.values))

    def play(self, rateFactor, duration):

        wavef = wave.open(self.filename+'-temp.wav', 'w')
        wavef.setnchannels(self.channels)  # mono
        wavef.setsampwidth(self.sampwidth)
        wavef.setframerate(self.sampleRate)
        a = self.dataString
        for i in range(0, len(a)):
            data2 = struct.pack('<h', int(a[i]))
            wavef.writeframesraw(data2)

        wavef.close()

        audio = wave.open(self.filename+'-temp.wav', 'rb')
        pa = pyaudio.PyAudio()
        stream = pa.open(format=pa.get_format_from_width(audio.getsampwidth()), channels=audio.getnchannels(),
                         rate=int(audio.getframerate()*rateFactor), output=True)

        n = audio.readframes(audio.getnframes())
        stream.write(n)
        audio.close()
        stream.close()
        pa.terminate()

    def setSampleValue(self, index, value):
        self.dataString[index] = value

    def save(self, path):
        wavef = wave.open(path, 'w')
        wavef.setnchannels(self.channels)  # mono
        wavef.setsampwidth(self.sampwidth)
        wavef.setframerate(self.sampleRate)
        a = self.samples.values
        for i in range(0, len(a)):
            data2 = struct.pack('<h', int(a[i].value) )
            wavef.writeframesraw(data2)


