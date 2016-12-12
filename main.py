from mediacomp.image import  *

#imagem=makePicture(pickAFile())


def choromakwy(source, bg):
    # source should have something in front of blue, bg is the new background
    for x in range(1,getWidth(source)):
        for y in range(1,getHeight(source)):
            p = getPixel(source,x,y)
            # My definition of blue: If the redness + greenness < blueness
            if (getRed(p) +  getBlue(p) < getGreen(p)):
                #Then, grab the color at the same spot from the new background
                setColor(p,getColor(getPixel(bg,x,y)))


    return source

#fundo=makePicture(pickAFile())

'''for x in range(1, getWidth(imagem)):
    for y in range(1, getHeight(imagem)):
        p = getPixel(imagem, x, y)
        if (getRed(p) + getBlue(p) < getGreen(p)):
            setColor(p, getColor(getPixel(fundo, x, y)))

#show(imagem)
'''

def blackwhite(source):
    # source should have something in front of blue, bg is the new background
    for x in range(1,getWidth(source)):
        for y in range(1,getHeight(source)):
            p = getPixel(source,x,y)
            # My definition of blue: If the redness + greenness < blueness
            if (  (getRed(p) +  getBlue(p) + getGreen(p))/255 < 1) :
                setColor(p,makeColor(0,0,0))
            else:
                setColor(p, makeColor(255, 255, 255))


    return source


    # source should have something in front of blue, bg is the new background

def colage(source1, source2):
    # source should have something in front of blue, bg is the new background
    for x in range(1, int(getWidth(source1)/2)):
        for y in range(1,getHeight(source1)):
            p = getPixel(source1,x,y)
            p2 = getPixel(source2, x, y)
            setColor(p,getColor(p2))


    return source1

#source1=makePicture("C:/Users/fl43/Desktop/musc.jpg")
#source2=makePicture("C:/Users/fl43/Desktop/esq.jpg")

#show(source1)
#show(source2)

#show(colage(source2, source1))


picture=makePicture("C:/Users/fl43/Desktop/rosa.jpg")

def greyscale(picture):
    for px in getPixels(picture):
        newRed = getRed(px) * 0.299
        newGreen = getGreen(px) * 0.587
        newBlue = getBlue(px) * 0.114
        luminance = newRed+newGreen+newBlue
        setColor(px,makeColor(luminance,luminance,luminance))

#show(greyscale(picture))


def negative(picture):
    for px in getPixels(picture):
        red=getRed(px)
        green=getGreen(px)
        blue=getBlue(px)
        negColor=makeColor( 255-red, 255-green, 255-blue)
        setColor(px,negColor)

    return picture


def lessRed(picture):
    for px in getPixels(picture):
        red = getRed(px)
        green = getGreen(px)
        blue = getBlue(px)
        negColor=makeColor( red+50, green+50, green+50)
        setColor(px,negColor)

    return picture


#show(lessRed(picture))

explore(picture)
#from mediacomp.image import  *
