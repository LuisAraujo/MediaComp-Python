import pyaudio
import wave

class Sound:
    filename =""
    audio = None
    stream = None

    def __init__(self, filename, audio):
        self.filename = filename
        self.audio = audio
        self.pa = pyaudio.PyAudio()
        self.stream = self.pa.open(format=self.pa.get_format_from_width(self.audio.getsampwidth()),
                                   channels=self.audio.getnchannels(), rate=self.audio.getframerate(), output=True)

    def __str__(self):
        return "Sound file: {} samples: {} ".format(self.filename, 0)

