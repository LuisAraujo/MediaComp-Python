from mediacomp import  *

source=makePicture(pickAFile())
mirrorpoint = int(getWidth(source)/2)
for y in range(1,getHeight(source)):
	for x in range(1,mirrorpoint):
		p = getPixel(source, x+mirrorpoint,y)
		p2 = getPixel(source, mirrorpoint-x,y)
		setColor(p,makeColor(getRed(p2), getGreen(p2), getBlue(p2)))

show(source)
#writePictureTo(pict,"teste")

'''source=makePicture(pickAFile())
mirrorpoint = int(getWidth(source)/2)
for y in range(1,getHeight(source)):
    for x in range(1,mirrorpoint):
        p = getPixel(source, x+mirrorpoint,y)
        p2 = getPixel(source, mirrorpoint-x,y)
        setColor(p,makeColor(getRed(p2), getGreen(p2), getBlue(p2)))

show(source)'''

'''picture=makePicture(pickAFile())
mirrorpoint = int(getWidth(picture)/2)
for y in range(1,getHeight(picture)):
	for x in range(1,mirrorpoint):
		p = getPixel(picture, x+mirrorpoint,y)
		p2 = getPixel(picture, mirrorpoint-x,y)
		setColor(p,makeColor(getRed(p2), getGreen(p2), getBlue(p2)))
show(picture)'''