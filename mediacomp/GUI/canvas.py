import tkinter as tk
from tkinter import filedialog
import os

class CanvasExplore:
    def __init__(self,raiz, pic):
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
        self.v = tk.StringVar()
        self.v.set("R: {} G: {} B: {} Color at location:".format(10,10,10))
        self.labText_w11 = tk.Label(self.widget1, textvariable=self.v)
        self.labText_w11["font"] = ("Arial", "12" )
        self.widget1["pady"] = 10
        self.widget1["padx"] = 10
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






class CanvasShowImage:
    def __init__(self,raiz, pic):
        #picture
        self.pic = pic
        raiz.title(pic.filename)
        filespath = os.path.dirname(os.path.abspath(__file__))

        self.widget = tk.Frame(raiz)
        self.widget.pack()

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

        self.image = tk.PhotoImage(master = self.widget, file=path)
        self.canvas = tk.Canvas(self.widget, width=self.pic.img.size[0], height=self.pic.img.size[1])
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)
        self.canvas.photo = self.image
        self.canvas.pack(side=tk.LEFT)


