from math import sqrt
from PIL import Image, ImageDraw
from mediacomp.picture import *
from mediacomp.pixel import *
from mediacomp.color import *
from mediacomp.GUI.canvas import *

def makePicture(path):
    pic = None
    try:
        im = Image.open(path)
        pic = Picture(path, im)
    except:
        print("No file path!")
    return pic

def show(pic):
    if(pic != None):
        win = tk.Tk()
        win.size = [pic.img.size[0] + 50, pic.img.size[1] + 50]
        CanvasShowImage(win, pic)
        win.mainloop()


def pickAFile():
    root = tk.Tk()
    root.withdraw()
    r = filedialog.askopenfilename()
    root.destroy()
    return r


def getWidth(pic):
    if (pic != None):
        return pic.img.size[0];

def getHeight(pic):
    if (pic != None):
        return pic.img.size[1];

def getPixel(pic,x,y):
    if  ( (pic != None) and ( x >= 0 and x<getWidth(pic)) and (y >= 0 and y <getHeight(pic)) ) :
         rgb = pic.img.getpixel((x, y))
         col = makeColor(rgb[0],rgb[1],rgb[2])
         px = Pixel(col, [x, y], pic)
         return px;



def setPixel(pic,x,y,color):
    if  ( (pic != None) and  ( x >= 0 and x<getWidth(pic)) and (y >= 0 and y <getHeight(pic)) )  :
         rgb2 = pic.img.putpixel((x, y), (color.rgb[0] ,color.rgb[1],color.rgb[2]))


def getPixels(pic):
    list = None
    if(pic != None):
        list = []
        for x in range(0, getWidth(pic)):
            for y in range(0, getHeight(pic)):
                px = getPixel(pic, x, y)
                list.append(px)

    return list

def getX(pixel):
    if(pixel != None) and (type(pixel) == Pixel):
        return pixel.xy[0]

def getY(pixel):
    if (pixel != None) and (type(pixel) == Pixel):
        return pixel.xy[1]

def getRed(pixel):
    if (pixel != None) and (type(pixel) == Pixel):
        return pixel.color.rgb[0]

def getGreen(pixel):
    if (pixel != None) and (type(pixel) == Pixel):
        return pixel.color.rgb[1]

def getBlue(pixel):
    if (pixel != None) and (type(pixel) == Pixel):
        return pixel.color.rgb[2]

def setRed(pixel, color):
    if ((pixel != None) and (type(pixel) == Pixel)):
        pixel.color.rgb[0] = int(color%256)
        pixel.pic.img.putpixel((pixel.xy[0], pixel.xy[1]), (pixel.color.rgb[0], pixel.color.rgb[1], pixel.color.rgb[2]) )

def setGreen(pixel, color):
    if ((pixel != None) and (type(pixel) == Pixel)):
        pixel.color.rgb[1] =  int(color%256)
        pixel.pic.img.putpixel((pixel.xy[0], pixel.xy[1]), (pixel.color.rgb[0], pixel.color.rgb[1], pixel.color.rgb[2]))

def setBlue(pixel,color):
    if ((pixel != None) and (type(pixel) == Pixel)):
        pixel.color.rgb[2] =  int(color%256)
        pixel.pic.img.putpixel((pixel.xy[0], pixel.xy[1]), (pixel.color.rgb[0], pixel.color.rgb[1], pixel.color.rgb[2]))

def getColor(pixel):
    if (pixel != None) and (type(pixel) == Pixel):
        return pixel.color

def setColor(pixel, color):
    if((pixel != None) and (type(pixel) == Pixel) and (color != None) and (type(color) == Color)):
        setPixel(pixel.pic, pixel.xy[0], pixel.xy[1], color)
    else:
        print("Color not is a type Color, Color is None or Pixel is None")

def makeColor(r, g, b):
    col = Color([int(r),int(g),int(b)])
    return col

def distance(color1, color2):
    if((color1 != None) and (type(color1) == Color) and (color2 != None) and (type(color2) == Color)):
        return sqrt( (color1.rgb[0] - color2.rgb[0])**2 +  (color1.rgb[1] - color2.rgb[1])**2 + (color1.rgb[2] - color2.rgb[2])**2)

def makeDarker(color):
    if ((color != None) and (type(color) == Color)):
        colorReturn = Color([color.rgb[0], color.rgb[1], color.rgb[2]])
        color.rgb[0] = int(color.rgb[0] - color.rgb[0]*.3)
        color.rgb[1] = int(color.rgb[1] - color.rgb[1] * .3)
        color.rgb[2] = int(color.rgb[2] - color.rgb[2] * .3)
        return colorReturn

def makeLighter(color):
    if ((color != None) and (type(color) == Color)):
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
    if ((pic != None) and (type(pic) == Picture) and (color != None) and (type(color) == Color)):
        draw = ImageDraw.Draw(pic.img)
        draw.text((x, y), text, fill=(color.rgb[0],color.rgb[1],color.rgb[2]))

def addLine(pic, color, x1, y1, x2, y2):
    if ((pic != None) and (type(pic) == Picture) and (color != None) and (type(color) == Color)):
        draw = ImageDraw.Draw(pic.img)
        draw.line((x1, y1, x2, y2), fill=(color.rgb[0],color.rgb[1],color.rgb[2]))

def addRect(pic, color, x, y, w, h):
    if ((pic != None) and (type(pic) == Picture) and (color != None) and (type(color) == Color)):
        draw = ImageDraw.Draw(pic.img)
        draw.rectangle(((x,y),(w,h)), fill=None, outline = (color.rgb[0],color.rgb[1],color.rgb[2]))

def addRectFilled(pic, color, x, y, w, h):
    if ((pic != None) and (type(pic) == Picture) and (color != None) and (type(color) == Color)):
        draw = ImageDraw.Draw(pic.img)
        draw.rectangle(((x, y), (w, h)), fill=(color.rgb[0], color.rgb[1], color.rgb[2]), outline=(color.rgb[0], color.rgb[1], color.rgb[2]))


def writePictureTo(pic,path):
    filename = str.split(path, ".")
    if( (filename[len(filename)-1] != "jpeg") or (filename[len(filename)-1] != "JPEG")):
        pic.img.save(path+".jpeg", 'JPEG')

def explore(pic):

    if((pic != None) and (type(pic) == Picture)):
        instancia = tk.Tk()
        instancia.size = [pic.img.size[0]+50, pic.img.size[1]+50]
        CanvasExplore(instancia, pic)
        instancia.mainloop()