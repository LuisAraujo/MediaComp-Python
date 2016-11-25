Media Computation with native Python
=========================

> This libary in Python is a remake of Media Computation with Jython. 
Media Computation is a contextualized approach to introducing computing using a ubiquitous theme of manipulating media, created by Contextualized Support for Learning Lab (CSL). You can see more MediaComp [here](http://coweb.cc.gatech.edu/mediaComp-teach/ "Home page of MediaComp") 

* Developed with native Python
* Use the libary in any Python IDE

### Version
alfa

## 1 - Images
### Functions available*
- *makePicture* 
	-  Takes a filename as input, reads the file, and creates a picture from it. Returns the picture.
- *show* 
	- Shows a picture provided as input. No return value.
- *pickAFile* 
	- Lets the user pick a file and returns the complete
path name as a string. No input.
- *getWidth* 
	- Takes a picture as input and returns its width in the number of pixels across the picture.
- *getHeight* 
	-  Takes a picture as input and returns its length in the number of pixels top-to-bottom in the picture.
- *getPixel* 
	- Takes a picture, an x position and a y position (two numbers), and returns the Pixel object at that point in the picture.
- getPixels 
	-  Takes a picture as input and returns the sequence of Pixel objects in the picture.
- *getX, getY* 
	-  Takes a Pixel object and returns the x or y (respectively) position of where that Pixel is at in the picture.
- *getRed, getGreen, getBlue* 
	- Each of these functions takes a Pixel object and returns the value (between 0 and 255) of the amount of redness, greenness, and blueness (respectively) in that pixel.
- *setRed, setGreen, setBlue
	- Each of these functions takes a Pixel object and a value (between 0 and 255) and sets the redness, greenness, or blueness (respectively) of that pixel to the given value.
- *getColor* 
	- Takes a Pixel and returns the Color object at that pixel.
- *setColor* 
	- Takes a Pixel object and a Color object and sets the color for that pixel.
- *makeColor*
	- Takes three inputs: For the red, green, and blue components (in order), then returns a color object.
- *distance* 
	- Takes two Color objects and returns a single number representing the distance between the colors. The red, green, and blue values of the colors are taken as a point in (x, y, z) space, and the cartesian distance is computed.
- *makeDarker, makeLighter* 
	- Each take a color and return a slightly darker or lighter (respectively) version of the color.
- *writePictureTo*
	- Takes a picture and a file name (string) as input, then writes the picture to the file as a JPEG. (Be sure to end the filename in “.jpg” for the operating system to understand it well.)
- *addText*
	- Takes a picture, an x position and a y position (two numbers), and some text as a string, which will get drawn into the picture.
- *addLine*
	- Takes a picture, a starting (x, y) position (two numbers), and an ending (x, y) position (two more numbers, four total) and draws a black line from the starting point to the ending point in the picture.
- *addRect*
	- Takes a picture, a starting (x, y) position (two numbers), and a width and height (two more numbers, four total) then draws a black rectangle in outline of the given width and height with the position (x, y) as the upper left corner.
- *addRectFilled*
	- Exactly like addRect, but fills the rectangle with black.

### Functions not available*
- *pickAColor* 
	- Takes no input, but puts up a color picker. Find the color you want, and the function will return the Color object of what you picked.
- *repaint* 
	- Shows again a picture provided as input. No return value.


## 2 - Sounds
### Functions available*
### Functions not available*


## 3 - Movies
### Functions available*
### Functions not available*

\* Description of functions by *Introduction to Media Computation:
A Multimedia Cookbook in Python* book. This book is available [here](http://coweb.cc.gatech.edu/mediaComp-plan/uploads/26/book-Sp2003.pdf "Introduction to Media Computation book")

## Dependence

* You need install the Pillow libary. Look more [Here](http://pillow.readthedocs.io/en/3.0.x/installation.html "Installation of Pillow")
* You need Tkinter, but it is the standard Python interface. Look mode (https://docs.python.org/2/library/tkinter.html)

### How use

1. Install Pillow libary
2. Copy the folder mediacomp for your python folder lib
3. Import MediaComp in your file (look examples)


### Examples

1 -Greyscale

```python
from mediacomp.image import  *

picture=makePicture(pickAFile())

for px in getPixels(picture): 
	newRed = getRed(px) * 0.299
	newGreen = getGreen(px) * 0.587
	newBlue = getBlue(px) * 0.114
	luminance = newRed+newGreen+newBlue
	setColor(px,makeColor(luminance,luminance,luminance))

show(picture)
```

![Tela Principal](https://github.com/LuisAraujo/MediaCompPython/blob/master/images/papertGS.png "Original picture [left] and converted to greyscale[right]")

2 - Mirrored

```python
from mediacomp.image import  *

picture=makePicture(pickAFile())
mirrorpoint = int(getWidth(picture)/2)

for y in range(1,getHeight(picture)):
	for x in range(1,mirrorpoint):
		p = getPixel(picture, x+mirrorpoint,y)
		p2 = getPixel(picture, mirrorpoint-x,y)
		setColor(p,makeColor(getRed(p2), getGreen(p2), getBlue(p2)))

show(picture)
```

![Tela Principal](https://github.com/LuisAraujo/MediaCompPython/blob/master/images/papertMir.png "Original picture [left] and mirrored along the vertical axis [right]")

3 - Line, Rect and Text

```python
from mediacomp.image import  *

picture=makePicture(pickAFile())

color = makeColor(255,255,255)
addRectFilled(picture,  color, 10, 300, 30, 310)
addText(picture, color, 70, 300, "Seymour Papert")
addRectFilled(picture, color , 200, 300, 220, 310)
addLine(picture, color, 30, 300, 200, 300)
addLine(picture, color, 30, 310, 200, 310)

show(picture)

```
![Tela Principal](https://github.com/LuisAraujo/MediaCompPython/blob/master/images/papertTxt.png "Original picture [left] and converted to greyscale[right]")

### Validation (JES vs. This Libary)

Original picture [left] and mirrored along the vertical axis [right]

### Validation (JES vs. This Libary) *

![Tela Principal](https://github.com/LuisAraujo/MediaCompPython/blob/master/images/barbaraLineYellow.png "Add small yellow line on the left")

Add small yellow line on the left (JES vs. This Libary)

![Tela Principal](https://github.com/LuisAraujo/MediaCompPython/blob/master/images/barbaraReduceBlue.png "Blue erased")

Blue erased (JES vs. This Libary)

![Tela Principal](https://github.com/LuisAraujo/MediaCompPython/blob/master/images/barbaraNegative.png "Negative of the image")

Negative of the image (JES vs. This Libary)

![Tela Principal](https://github.com/LuisAraujo/MediaCompPython/blob/master/images/Santa.png "Mirrored along the vertical axis")

Mirrored along the vertical axis (JES vs. This Libary)


![Tela Principal](https://github.com/LuisAraujo/MediaCompPython/blob/master/images/chromakey.png "Mirrored along the vertical axis")

Chromakey (JES vs. This Libary)

\* Examples by *Introduction to Media Computation: A Multimedia Cookbook in Python* book.