import tkinter as tk
from math import sqrt
from tkinter import filedialog

from PIL import Image, ImageDraw
from mediacomp.picture import *
from mediacomp.pixel import *

from mediacomp.color import *

def makePicture(path):
    im = Image.open(path)
    pic = Picture(path, im)
    return pic

def show(pic):
    pic.img.show()

def pickAFile():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename()

def getWidth(pic):
    return pic.img.size[0];

def getHeight(pic):
    return pic.img.size[1];

def getPixel(pic,x,y):
    if ( x >= 0 and x<getWidth(pic)) and (y >= 0 and y <getHeight(pic))  :
         rgb = pic.img.getpixel((x, y))
         col = makeColor(rgb[0],rgb[1],rgb[2])
         px = Pixel(col, [x, y], pic)
         return px;



def setPixel(pic,x,y,color):
    if ( x >= 0 and x<getWidth(pic)) and (y >= 0 and y <getHeight(pic))  :
         rgb2 = pic.img.putpixel((x, y), (color.rgb[0] ,color.rgb[1],color.rgb[2]))


def getPixels(pic):
    list = []
    for x in range(0, getWidth(pic)):
        for y in range(0, getHeight(pic)):
            px = getPixel(pic, x, y)
            list.append(px)
    return list

def getX(pixel):
    return pixel.xy[0]

def getY(pixel):
    return pixel.xy[1]

def getRed(pixel):
    return pixel.color.rgb[0]

def getGreen(pixel):
    return pixel.color.rgb[1]

def getBlue(pixel):
    return pixel.color.rgb[2]

def setRed(pixel, col):
    pixel.color.rgb[0] = int(col)
    pixel.pic.img.putpixel((pixel.xy[0], pixel.xy[1]), (pixel.color.rgb[0], pixel.color.rgb[1], pixel.color.rgb[2]) )

def setGreen(pixel, col):
    return pixel.color.rgb[1]

def setBlue(pixel,col):
    return pixel.color.rgb[2]

def getColor(pixel):
    return pixel.color

def setColor(pixel, color):
    if(type(color) == Color):
        setPixel(pixel.pic, pixel.xy[0], pixel.xy[1], color)
    else:
        print("color not is a type Color")

def makeColor(r, g, b):
    col = Color([int(r),int(g),int(b)])
    return col

def distance(color1, color2):
    return sqrt( (color1.rgb[0] - color2.rgb[0])**2 +  (color1.rgb[1] - color2.rgb[1])**2 + (color1.rgb[2] - color2.rgb[2])**2)

def makeDarker(color):
    colorReturn = Color([color.rgb[0], color.rgb[1], color.rgb[2]])
    color.rgb[0] = int(color.rgb[0] - color.rgb[0]*.3)
    color.rgb[1] = int(color.rgb[1] - color.rgb[1] * .3)
    color.rgb[2] = int(color.rgb[2] - color.rgb[2] * .3)
    return colorReturn

def makeLighter(color):
    colorReturn = Color([color.rgb[0],color.rgb[1], color.rgb[2]])
    color.rgb[0] = int(color.rgb[0] + color.rgb[0]*.42)
    color.rgb[1] = int(color.rgb[1] + color.rgb[1] * .42)
    color.rgb[2] = int(color.rgb[2] + color.rgb[2] * .275)
    return colorReturn

def pickAColor():
    print("Nao implementado")

def repaint(pic):
    print("Nao implementado")

def addText(pic, color, x, y, text):
    draw = ImageDraw.Draw(pic.img)
    draw.text((x, y), text, fill=(color.rgb[0],color.rgb[1],color.rgb[2]))

def addLine(pic, color, x1, y1, x2, y2):
    draw = ImageDraw.Draw(pic.img)
    draw.line((x1, y1, x2, y2), fill=(color.rgb[0],color.rgb[1],color.rgb[2]))

def addRect(pic, color, x, y, w, h):
    draw = ImageDraw.Draw(pic.img)
    draw.rectangle(((x,y),(w,h)), fill=None, outline = (color.rgb[0],color.rgb[1],color.rgb[2]))

def addRectFilled(pic, color, x, y, w, h):
    draw = ImageDraw.Draw(pic.img)
    draw.rectangle(((x, y), (w, h)), fill=(color.rgb[0], color.rgb[1], color.rgb[2]), outline=(color.rgb[0], color.rgb[1], color.rgb[2]))


def writePictureTo(pic,path):
    filename = str.split(path, ".")
    if( (filename[len(filename)-1] != "jpeg") or (filename[len(filename)-1] != "JPEG")):
        pic.img.save(path+".jpeg", 'JPEG')

