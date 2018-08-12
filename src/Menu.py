from Button import *
from Graphics import *
from math import *
from Pixel import *

class Menu:
    def __init__(self,size,win):
        self.colors =[  '#E6E6E6',
                        '#503D8A','#9D41B6',
                        '#EC4141','#DB7730',
                        '#EBC529','#6BBA46',
                        '#30D5C7','#72C1E8',
                        '#5681C9','#5151B6',
                        '#3c3c3c','#ffffff',]
        self.win = win
        self.width = self.win.getWidth()
        self.height = size
        self.backgroundColor = '#E0E0E0'

        p1 = Point(0,self.win.getHeight()-self.height)
        p2 = Point(self.width,self.win.getHeight())
        self.frame = Rectangle(p1,p2)
        self.frame.setWidth(0)
        self.frame.setFill(self.backgroundColor)
        self.frame.draw(self.win)

        self.buttons = []
        self.addButtons()

        self.buttonSelected = False
        self.selectedColorButton = self.buttons[-1]
        self.selectedColorButton.highlight()

        self.selectedColor = '#ffffff'

    def addButton(self,center,w,h,fill,text=''):
        self.buttons.append(Button(self.win,center,w,h,text,fill,'#3c3c3c'))

    def addButtons(self):
        spacing = self.width/len(self.colors)
        for i in range(len(self.colors)):
            center = Point((i*spacing)+(spacing/2),self.win.getHeight()-(self.height/2))
            w,h = spacing*0.8,min((spacing/3,self.height*0.7))
            if i==0:
                self.addButton(center,w,h,self.colors[i],text='Clear',)
            else:
                self.addButton(center,w,h,self.colors[i])

    def clearButtonSelected(self,point):
        return self.buttons[0].clicked(point)

    def highlightClearButton(self):
        self.buttons[0].depress()

    def colorButtonSelected(self,point):
        for i in range(1,len(self.buttons)):
            if self.buttons[i].clicked(point):
                self.selectedColorButton.removeHighlight()
                self.selectedColorButton = self.buttons[i]
                self.selectedColorButton.highlight()
                return True
        return False

    def updateColorSelection(self):
        self.selectedColor = self.selectedColorButton.getColor()
