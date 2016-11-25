class Pixel:
    xy = [0,0]
    pic = None
    color = None

    def __init__(self, color, xy, pic):
        self.color = color
        self.xy = xy
        self.pic = pic

    def __str__(self):
        return "Pixel, color = {} r={} g={} b={}".format(self.color.name, self.color.rgb[0], self.color.rgb[1], self.color.rgb[2])

