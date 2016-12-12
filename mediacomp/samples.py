from mediacomp.sample import *

class Samples:
    values = []
    sound = None

    def __init__(self,sound):
        self.sound = sound
        self.values = []
        for i in range(0, len(self.sound.dataString)):
            self.values.append(Sample(self, i, self.sound.dataString[i]))


    def __iter__(self):
        return iter(self.values)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, i):
        return self.values[i]

