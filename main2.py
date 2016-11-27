from mediacomp.audio import *
from mediacomp.image import *

path ="C:/Users/fl43/Dropbox/MESTRADO LUIS_Concepção_Blocos/Som/recursos/Elliot-hello.wav"

c = makeSound(path)
print(c)

play(c)