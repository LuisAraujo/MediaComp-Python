from mediacomp.image import  *

picture=makePicture(pickAFile())

for p in getPixels(picture):
    setRed(p, 500)

explore(picture)