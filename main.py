from mediacomp.image import  *

picture=makePicture(pickAFile())

color = makeColor(255,255,255)
addRectFilled(picture,  color, 10, 300, 30, 310)
addText(picture, color, 70, 300, "Seymour Papert")
addRectFilled(picture, color , 200, 300, 220, 310)
addLine(picture, color, 30, 300, 200, 300)
addLine(picture, color, 30, 310, 200, 310)

show(picture)