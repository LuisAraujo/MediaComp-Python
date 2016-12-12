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
