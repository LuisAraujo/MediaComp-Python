import pyaudio
import wave
import numpy as np
import struct

class Sound:
    filename =""
    sampleRate = 0
    channels = 0
    sampwidth = 0
    dataString = []
    samples = None

    def __init__(self, filename):
        self.filename = filename
        audio = wave.open(self.filename, 'rb')
        self.sampleRate = audio.getframerate()
        self.channels = audio.getnchannels()
        self.sampwidth = audio.getsampwidth()
        data = audio.readframes(audio.getnframes())
        self.dataString = np.fromstring(data, 'Int16')
        self.samples = Samples(self)
        audio.close()

    def __str__(self):
        return "Sound file: {} number of samples: {} ".format(self.filename, len(self.samples.values))

    def play(self, rateFactor, duration):
        audio = wave.open(self.filename, 'rb')
        pa = pyaudio.PyAudio()
        stream = pa.open(format=pa.get_format_from_width(audio.getsampwidth()), channels=audio.getnchannels(),
                         rate=int(audio.getframerate()*rateFactor), output=True)

        data = audio.readframes(audio.getnframes())
        n = bytes(self.dataString)
        stream.write(n)
        audio.close()
        stream.close()
        pa.terminate()

    def setSampleValue(self, index, value):
        self.dataString[index] = str(value)

    def save(self, path):
        wavef = wave.open(path, 'w')
        wavef.setnchannels(self.channels)  # mono
        wavef.setsampwidth(self.sampwidth)
        wavef.setframerate(self.sampleRate)
        a = self.samples.values
        for i in range(0, len(a)):
            data2 = struct.pack('<h', int(a[i].value) )
            wavef.writeframesraw(data2)


class Samples:
    values = []
    sound = None

    def __init__(self,sound):
        self.sound = sound
        for i in range(0, len(self.sound.dataString)):
            self.values.append(Sample(self, i, self.sound.dataString[i]))

    def __iter__(self):
        return iter(self.values)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, i):
        return self.values[i]


class Sample:
    samples = None
    value = 0
    index = 0

    def __init__(self,samples, index, value):
        self.samples = samples
        self.index = index
        self.value = int(value)

    def __str__(self):
        return "Sample at {} with {} ".format(self.index, self.value)


    def changeValue(self, value):
        self.value = value
        self.samples.sound.setSampleValue(self.index, value)
