import tkinter as tk
from tkinter import filedialog
import os
import threading
import numpy as np

class CanvasExploreImage:
    def __init__(self,pic):
        raiz = tk.Tk()
        raiz.size = [pic.img.size[0] + 50, pic.img.size[1] + 50]

        #picture
        self.pic = pic
        raiz.title(pic.filename)
        filespath = os.path.dirname(os.path.abspath(__file__))

        #button zoom
        self.widget4 = tk.Frame(raiz)
        self.widget4["height"] = 15
        self.widget4.pack()
        self.labText_w01 = tk.Label(self.widget4, text="Explore Image")
        self.labText_w01["font"] = ("Arial", "12")
        self.labText_w01["width"] = 40
        self.labText_w01.pack(side=tk.LEFT)

        #button zoom (not implements yet)
        #self.btZoom = tk.Button(self.widget4)
        #self.btZoom["text"] = "Zoom"
        #self.btZoom["font"] = ("Arial", "10", "bold")
        #self.btZoom["width"] = 40
        #self.btZoom.pack()

        #lable X
        self.widget0 = tk.Frame(raiz)
        self.widget0.pack()
        self.labText_w01 = tk.Label(self.widget0, text="X:")
        self.labText_w01["font"] = ("Arial", "12")
        self.labText_w01.pack(side=tk.LEFT)

        #button less pixel X
        self.bt_menos1 = tk.Button(self.widget0)
        imgMenos1 = tk.PhotoImage(master=self.bt_menos1, file=filespath+"/source/leftArrow.gif")
        self.bt_menos1["image"] =  imgMenos1
        self.bt_menos1.photo = imgMenos1
        self.bt_menos1.pack(side=tk.LEFT)
        self.bt_menos1.bind('<Button-1>', self.changeValueXmenos)

        # text value pixel X
        self.v_x = tk.StringVar()
        self.v_x.set(0)
        self.posX = tk.Entry(self.widget0,textvariable=self.v_x)
        self.posX["width"] = 7
        self.posX.pack(side=tk.LEFT)

        # button more pixel X
        self.bt_mais1 = tk.Button(self.widget0)
        imgMais1 = tk.PhotoImage(master=self.bt_mais1, file=filespath+"/source/rightArrow.gif")
        self.bt_mais1["image"] = imgMais1
        self.bt_mais1.photo = imgMais1
        self.bt_mais1.pack(side=tk.LEFT)
        self.bt_mais1.bind('<Button-1>', self.changeValueXmais)

        #lable Y
        self.labText_w02 = tk.Label(self.widget0, text="Y:")
        self.labText_w02["font"] = ("Arial", "12")
        self.labText_w02.pack(side=tk.LEFT)

        # button less pixel Y
        self.bt_menos2 = tk.Button(self.widget0)
        imgMenos2 = tk.PhotoImage(master=self.bt_menos2,file=filespath+"/source/leftArrow.gif")
        self.bt_menos2["image"] = imgMenos2
        self.bt_menos2.photo = imgMenos2
        self.bt_menos2.pack(side=tk.LEFT)
        self.bt_menos2.bind('<Button-1>', self.changeValueYmenos)

        self.v_y = tk.StringVar()
        self.v_y.set(0)
        self.posY = tk.Entry(self.widget0, textvariable=self.v_y)
        self.posY["width"] = 7
        self.posY.pack(side=tk.LEFT)

        # button more pixel Y
        self.bt_mais2 = tk.Button(self.widget0)
        imgMais2 = tk.PhotoImage(master=self.bt_mais2, file=filespath+"/source/rightArrow.gif")
        self.bt_mais2["image"] = imgMais2
        self.bt_mais2.photo = imgMais2
        self.bt_mais2.pack(side=tk.LEFT)
        self.bt_mais2.bind('<Button-1>', self.changeValueYmais)

        #info rgb
        self.widget1 = tk.Frame(raiz)
        self.widget1["pady"] = 10
        self.widget1["padx"] = 10
        self.v = tk.StringVar()
        self.v.set("R: {} G: {} B: {} Color at location:".format(10,10,10))
        self.labText_w11 = tk.Label(self.widget1, textvariable=self.v)
        self.labText_w11["font"] = ("Arial", "12" )
        self.labText_w11.pack(side=tk.LEFT)
        self.widget1.pack()

        #little canvas for show color of selected pixel
        self.cavCor = tk.Canvas(self.widget1, bg="black", height=25, width=25)
        self.cavCor.pack(side=tk.LEFT)

        self.widget2 = tk.Frame(raiz)
        self.widget2.pack()

        #creating path gif file
        path = ""
        #same path jpg file
        pathS = self.pic.filename.split("/");
        for i in range(0, len(pathS)-1):
            path+=pathS[i]+"/"

        #add name git file
        path += "imagetemp.gif"
        #save
        self.pic.img.save(path)

        self.image = tk.PhotoImage(master = self.widget2, file=path)
        self.canvas = tk.Canvas(self.widget2, width=self.pic.img.size[0], height=self.pic.img.size[1])
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)
        self.canvas.photo = self.image
        self.canvas.pack(side=tk.LEFT)
        self.canvas.bind('<Button-1>', self.clickCanvas)

        raiz.mainloop()

    def clickCanvas(self, event):

        rgb = self.pic.img.getpixel( (event.x, event.y) )
        self.v.set("R: {} G: {} B: {} Color at location:".format(rgb[0], rgb[1], rgb[2]))
        self.v_x.set(event.x)
        self.v_y.set(event.y)
        self.cavCor.create_rectangle(0, 0, 30, 30, fill='#%02x%02x%02x' % (rgb[0], rgb[1], rgb[2]))
        self.creatTarget(int(self.v_x.get()), int(self.v_y.get()))


    def changeValueXmais(self, event):
        if(int(self.v_x.get()) < self.pic.img.size[0]-1):
            self.v_x.set(int(self.v_x.get())+1)
            rgb = self.pic.img.getpixel(( int(self.v_x.get()) , int(self.v_y.get())))
            self.v.set("R: {} G: {} B: {} Color at location:".format(rgb[0], rgb[1], rgb[2]))
            self.cavCor.create_rectangle(0, 0, 30, 30, fill='#%02x%02x%02x' % (rgb[0], rgb[1], rgb[2]))
            self.creatTarget(int(self.v_x.get()), int(self.v_y.get()))

    def changeValueXmenos(self, event):
        if (int(self.v_x.get()) > 0):
            self.v_x.set(int(self.v_x.get()) - 1)
            rgb = self.pic.img.getpixel((int(self.v_x.get()), int(self.v_y.get())))
            self.v.set("R: {} G: {} B: {} Color at location:".format(rgb[0], rgb[1], rgb[2]))
            self.cavCor.create_rectangle(0, 0, 30, 30, fill='#%02x%02x%02x' % (rgb[0], rgb[1], rgb[2]))
            self.creatTarget(int(self.v_x.get()), int(self.v_y.get()))

    def changeValueYmais(self, event):
        if (int(self.v_y.get()) < self.pic.img.size[1] - 1):
            self.v_y.set(int(self.v_y.get()) + 1)
            rgb = self.pic.img.getpixel((int(self.v_x.get()), int(self.v_y.get())))
            self.v.set("R: {} G: {} B: {} Color at location:".format(rgb[0], rgb[1], rgb[2]))
            self.cavCor.create_rectangle(0, 0, 30, 30, fill='#%02x%02x%02x' % (rgb[0], rgb[1], rgb[2]))
            self.creatTarget(int(self.v_x.get()), int(self.v_y.get()))

    def changeValueYmenos(self, event):
        if (int(self.v_y.get()) > 0):
            self.v_y.set(int(self.v_y.get()) - 1)
            rgb = self.pic.img.getpixel((int(self.v_x.get()), int(self.v_y.get())))
            self.v.set("R: {} G: {} B: {} Color at location:".format(rgb[0], rgb[1], rgb[2]))
            self.cavCor.create_rectangle(0, 0, 30, 30, fill='#%02x%02x%02x' % (rgb[0], rgb[1], rgb[2]))
            self.creatTarget(int(self.v_x.get()), int(self.v_y.get()))

    def creatTarget(self, x, y):
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)
        self.canvas.create_line(x, y+2, x, y+6, fill="yellow")
        self.canvas.create_line(x+2, y, x+6, y, fill="yellow")
        self.canvas.create_line(x, y-2, x, y-6, fill="yellow")
        self.canvas.create_line(x-2, y, x-6, y, fill="yellow")



class CanvasExploreSound:
    sound = None
    last = -1
    def __init__(self, sound):
        self.sound = sound
        raiz = tk.Tk()
        raiz.size = [200, 500]
        filespath = os.path.dirname(os.path.abspath(__file__))

        self.widget = tk.Frame(raiz)
        self.widget["height"] = 100
        self.widget["pady"] = 2
        self.widget.pack()

        self.btZoom = tk.Button(self.widget)
        self.btZoom["text"] = "Play Entire Sound"
        self.btZoom["font"] = ("Arial", "10")
        self.btZoom.pack(side = tk.LEFT, fill = tk.BOTH, padx=8)

        self.btZoom2 = tk.Button(self.widget)
        self.btZoom2["text"] = "Play Before"
        self.btZoom2["font"] = ("Arial", "10")
        self.btZoom2.pack(side = tk.LEFT, fill = tk.BOTH, padx=8)

        self.btZoom3 = tk.Button(self.widget)
        self.btZoom3["text"] = "Play After"
        self.btZoom3["font"] = ("Arial", "10")
        self.btZoom3.pack(side=tk.LEFT, fill=tk.BOTH, padx=8)

        self.btZoom4 = tk.Button(self.widget)
        self.btZoom4["text"] = "Stop"
        self.btZoom4["font"] = ("Arial", "10")
        self.btZoom4.pack(side=tk.LEFT, fill=tk.BOTH, padx=8)

        #widget 2
        self.widget2 = tk.Frame(raiz)
        self.widget2["height"] = 100
        self.widget2["pady"] = 2
        self.widget2.pack()

        self.btPlaySelec = tk.Button(self.widget2)
        self.btPlaySelec["text"] = "Play Selection"
        self.btPlaySelec["font"] = ("Arial", "10")
        self.btPlaySelec.pack(side=tk.LEFT, fill=tk.BOTH, padx=8)

        self.btClearSelec = tk.Button(self.widget2)
        self.btClearSelec["text"] = "Clear Selection"
        self.btClearSelec["font"] = ("Arial", "10")
        self.btClearSelec.pack(side=tk.LEFT, fill=tk.BOTH, padx=8)

        #lable
        self.labStartIdx = tk.Label(self.widget2, text="Start Index:")
        self.labStartIdx["font"] = ("Arial", "10", "bold")
        self.labStartIdx.pack(side=tk.LEFT)

        # text value pixel X
        self.startIndex = tk.StringVar()
        self.startIndex.set(0)
        self.labText_w02 = tk.Label(self.widget2,textvariable=self.startIndex)
        self.labText_w02["font"] = ("Arial", "10", "bold")
        self.labText_w02.pack(side=tk.LEFT)

        self.labText_w03 = tk.Label(self.widget2, text="Stop Index:")
        self.labText_w03["font"] = ("Arial", "10", "bold")
        self.labText_w03.pack(side=tk.LEFT)

        # text value pixel X
        self.stopIndex = tk.StringVar()
        self.stopIndex.set(0)
        self.labText_w04 = tk.Label(self.widget2, textvariable=self.stopIndex)
        self.labText_w04["font"] = ("Arial", "10", "bold")
        self.labText_w04.pack(side=tk.LEFT)

        self.widget3 = tk.Frame(raiz)
        self.widget3["height"] = 100
        self.widget3["pady"] = 2
        self.widget3.pack()

        # little canvas for show color of selected pixel
        self.canvas = tk.Canvas(self.widget3, bg="black", height=200, width=700)
        self.canvas.bind("<Button-1>", self.printLine)
        self.canvas.pack(side=tk.LEFT)


        self.widget4 = tk.Frame(raiz)
        self.widget4["height"] = 100
        self.widget4.pack()

        self.bt_mais1 = tk.Button(self.widget4)
        imgMais1 = tk.PhotoImage(master=self.bt_mais1, file=filespath + "/source/leftArrow.gif")
        self.bt_mais1["image"] = imgMais1
        self.bt_mais1.photo = imgMais1
        self.bt_mais1.pack(side=tk.LEFT)

        self.bt_mais2 = tk.Button(self.widget4)
        imgMais2 = tk.PhotoImage(master=self.bt_mais2, file=filespath + "/source/endLeft.gif")
        self.bt_mais2["image"] = imgMais2
        self.bt_mais2.photo = imgMais2
        self.bt_mais2.pack(side=tk.LEFT)

        self.labText_w03 = tk.Label(self.widget4, text="Current Index:")
        self.labText_w03["font"] = ("Arial", "10", "bold")
        self.labText_w03.pack(side=tk.LEFT)

        self.currentIndex = tk.StringVar()
        self.currentIndex .set(0)
        self.posX = tk.Entry(self.widget4, textvariable=self.currentIndex )
        self.posX["width"] = 7
        self.posX.pack(side=tk.LEFT)

        self.labText_w03 = tk.Label(self.widget4, text="Sample Value:")
        self.labText_w03["font"] = ("Arial", "10", "bold")
        self.labText_w03.pack(side=tk.LEFT)

        self.sampleValue = tk.StringVar()
        self.sampleValue.set(0)
        self.sampleValueGUI = tk.Entry(self.widget4, textvariable=self.sampleValue)
        self.sampleValueGUI["width"] = 7
        self.sampleValueGUI.pack(side=tk.LEFT)

        self.bt_mais1 = tk.Button(self.widget4)
        imgMais1 = tk.PhotoImage(master=self.bt_mais1, file=filespath + "/source/rightArrow.gif")
        self.bt_mais1["image"] = imgMais1
        self.bt_mais1.photo = imgMais1
        self.bt_mais1.pack(side=tk.LEFT)

        self.bt_mais2 = tk.Button(self.widget4)
        imgMais2 = tk.PhotoImage(master=self.bt_mais2, file=filespath + "/source/endRight.gif")
        self.bt_mais2["image"] = imgMais2
        self.bt_mais2.photo = imgMais2
        self.bt_mais2.pack(side=tk.LEFT)

        self.widget5 = tk.Frame(raiz)
        self.widget5["height"] = 100
        self.widget5.pack()

        self.numSampleLabel = tk.Label(self.widget5, text="The number of samples between pixels:")
        self.numSampleLabel["font"] = ("Arial", "10", "bold")
        self.numSampleLabel.pack(side=tk.LEFT, pady=12)

        self.numSampleValue = tk.StringVar()
        self.numSampleValue.set(0)
        self.numSampleValueGUI = tk.Entry(self.widget5, textvariable=self.numSampleValue)
        self.numSampleValueGUI["width"] = 7
        self.numSampleValueGUI.pack(side=tk.LEFT)

        self.widget6 = tk.Frame(raiz)
        self.widget6["height"] = 100
        self.widget6.pack()
        self.btZoom = tk.Button(self.widget)

        self.btZoomIn = tk.Button(self.widget6)
        self.btZoomIn["text"] = "Zoom In"
        self.btZoomIn["font"] = ("Arial", "10")
        self.btZoomIn.pack(fill=tk.BOTH, pady=8)

        self.printGraph()
        raiz.mainloop()

    def printLine(self, event):
        self.canvas.create_line(self.last, 0, self.last, 200, fill="#000000")
        self.canvas.create_line(event.x, 0, event.x, 200, fill="#00ffff")
        self.last = event.x

        self.currentIndex.set(event.x*700)
        self.sampleValue.set(0)


    def printGraph(self):
        samples = self.sound.dataString
        print(type(self.sound.dataString))
        normSamples = []

        for a in self.sound.dataString:
            #multiplicando pelo fator de aplitude
            normSamples.append(int(a)*0.004)

        #tamanho do array pelo numero de pixel
        num = int(len(normSamples)/700)
        i =0
        j =0
        while( i <  len(normSamples)):
                self.canvas.create_line(j, int(normSamples[i-num])+100, j+1, int(normSamples[i])+100, fill="#ffffff")
                i+= num #sampleByPixel
                j+=1

        print(num)

        self.canvas.create_line(0, 100, 700, 100, fill="#00ffff")














class CanvasShowImage():
    def __init__(self, pic):
        self.pic = pic
        self.raiz = tk.Tk()
        self.raiz.size = [self.pic.img.size[0] + 50, self.pic.img.size[1] + 50]
        self.raiz.protocol('WM_DELETE_WINDOW', self.closeWin)

        # picture
        self.raiz.title(self.pic.filename)
        filespath = os.path.dirname(os.path.abspath(__file__))

        self.widget = tk.Frame(self.raiz)
        self.widget.pack()

        # creating path gif file
        path = ""
        # same path jpg file
        pathS = self.pic.filename.split("/");
        for i in range(0, len(pathS) - 1):
            path += pathS[i] + "/"

        # add name git file
        path += "imagetemp.gif"
        # save
        self.pic.img.save(path)

        self.image = tk.PhotoImage(master=self.widget, file=path)
        self.canvas = tk.Canvas(self.widget, width=self.pic.img.size[0], height=self.pic.img.size[1])
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)
        self.canvas.photo = self.image
        self.canvas.pack(side=tk.LEFT)
        self.raiz.mainloop()


    def closeWin(self):
        print("ok")
        self.raiz.destroy()

    @classmethod
    def getInstance(cls, pic):
        if(cls.instance == None):
            c = CanvasShowImage()
            c.setPic(pic)
            return c
        else:
            return  cls.intance()

