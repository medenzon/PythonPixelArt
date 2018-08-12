from Button import *
from Graphics import *

class Pixel:
    def __init__(self,p1,p2):
        self.frame = Rectangle(p1,p2)
        self.frame.setWidth(0.5)
        self.frame.setOutline('#969696')
        self.isDrawn = False

    def draw(self,win):
        self.frame.draw(win)
        self.isDrawn = True

    def undraw(self):
        self.frame.undraw()
        self.isDrawn = False

    def setFill(self,color):
        self.fillColor = color
        self.frame.setFill(self.fillColor)
