from Graphics import *
from time import sleep

class Button:

    def __init__(self,win,center,width,height,label,color,textColor,borderWidth=0,borderColor='black'):
        self.center = center
        self.p1 = Point(self.center.getX() - width/2, self.center.getY() - height/2)
        self.p2 = Point(self.center.getX() + width/2, self.center.getY() + height/2)
        self.rect = Rectangle(self.p1,self.p2)
        self.color = color
        self.rect.setFill(self.color)
        self.rect.setOutline(borderColor)
        self.rect.setWidth(borderWidth)
        self.rect.draw(win)
        self.label = Text(self.center, label)
        self.label.setFill(textColor)
        self.textColor = textColor
        self.label.draw(win)
        self.highlighted = False

    def getColor(self):
        return self.color

    def setLabel(self,label):
        self.label.setText(label)

    def setFill(self,color):
        self.rect.setFill(color)

    def undraw(self):
        self.rect.undraw()
        self.label.undraw()

    def move(self,dx,dy):
        self.rect.move(dx,dy)
        self.label.move(dx,dy)

    def clicked(self, p):
        if p == None: return False
        elif (self.p1.getX() <= p.getX() <= self.p2.getX() and self.p1.getY() <= p.getY() <= self.p2.getY()):
            return True

    def depress(self):
        self.rect.setFill('#c2c2c2')
        sleep(0.2)
        self.rect.setFill(self.color)

    def highlight(self):
        self.highlighted = True
        self.rect.setWidth(1.5)

    def removeHighlight(self):
        self.highlighted = False
        self.rect.setWidth(0)
