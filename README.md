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

### Picture Tool (in development)

![Tela Principal](https://github.com/LuisAraujo/MediaCompPython/blob/master/images/interfaceExploreImg.png "Add small yellow line on the left")

Picture Tool (JES vs. This Libary)


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

### Validation (JES vs. This Libary)*

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


## 2 - Sounds
### Functions available*

- *pickAFile* 
	-  Lets the user pick a file and returns the complete path name as a string. No input
- *makeSound* 
    - Takes a filename as input, reads the file, and creates a sound from it. Returns the sound.
- *play*
    - Plays a sound provided as input. No return value.
- *getSamples* 
    - Takes a sound as input and returns the Samples in that sound.
- *writeSoundTo*
    - Takes a sound and a filename (a string) and writes the sound to that file as a WAV file. (Make sure that the filename ends in “.wav” if you want the operating system to treat it right.)
- *setSampleValueAt*
    - Takes a sound, an index, and a value (should be between -32000 and 32000), and sets the value of the sample at the given index in the given sound to the given value. getSampleObjectAt Takes a sound and an index (an integer value), and returns the Sample object at that index.
- *getSample*
    - Takes a Sample object and returns its value (between -32000 and 32000) 
- *setSample*
    - Takes a Sample object and a value, and sets the sample to that value.
- *getLength*
    - Takes a sound as input and returns the number of samples in that sound.
- *getSound*
    - Takes a Sample object and returns the Sound that it remembers as its own.
- *getSamplingRate*
    - Takes a sound as input and returns the number representing the number of samples in each second for the sound. getLength Returns the length of the sound as a number of samples getSampleValueAt Takes a sound and an index (an integer value), and returns the value of the sample (between -32000 and 32000) for that object.        
- *playAtRate*
    - Takes a sound and a rate (1.0 means normal speed, 2.0 is twice as fast, and 0.5 is half as fast), and plays the sound at that rate. The duration is always the same, e.g., if you play it twice as fast, the sound plays twice to fill the given time.

### Functions not available*
- *blockingPlay* 
    -Plays the sound provided as input, and makes sure that no other sound plays at the exact same time. (Try two play’s right after each other.)
- *playAtRateDur*
    - Takes a sound, a rate, and a duration as the number of samples to play.


### Examples
### Validation (JES vs. This Libary)*
### Sound Tool (in development)


## 3 - Movies
### Functions available*
### Functions not available*

### Examples
### Validation (JES vs. This Libary)*
### Movie Tool (in development)



\* Description of functions by *Introduction to Media Computation:
A Multimedia Cookbook in Python* book. This book is available [here](http://coweb.cc.gatech.edu/mediaComp-plan/uploads/26/book-Sp2003.pdf "Introduction to Media Computation book")

## Dependence

* You need install the *Pillow* libary. Look more [Here](http://pillow.readthedocs.io/en/3.0.x/installation.html "Installation of Pillow")
* You need install the *PyAudio* libary. Look more [Here](https://pypi.python.org/pypi/PyAudio "Installation pyAudio")
* Maybe you need install the *numpy* libary. Look more [Here](http://www.numpy.org/ "Installation numpy")

* MediaComp library use this standard libraries: [Tkinter](https://docs.python.org/2/library/tkinter.html), [Math](https://docs.python.org/2/library/math.html), [Struct](https://docs.python.org/2/library/struct.html), [wave](https://docs.python.org/2/library/wave.html)


### How use

1. Install all dependence libary (Pillow, PyAudio, Numpy ...) 
2. Copy the folder mediacomp for your python folder lib
3. Import MediaComp in your file (look examples)

Note: You can check whether you have the libary installed. Make this in console:

*\>\>\>python -c "import pillow*

*\>\>\>python -c "import pyaudio"*

*\>\>\>python -c "import numpy*


