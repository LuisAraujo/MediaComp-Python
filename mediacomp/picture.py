class Picture:
    filename = ""
    img = None
    def __init__(self, filename, img):
        self.filename = filename
        self.img = img

    def __str__(self):
        return "Picture, filename {} height {} width {}".format(self.filename, self.img.size[0], self.img.size[1])
