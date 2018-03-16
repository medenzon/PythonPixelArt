from Graphics import *
from time import sleep
from math import *

width,height = 800,800
w,h = width,height
win = GraphWin('PixelArt',width,height)
size = height//20
menuSize = size-1
print(size)

rows,cols = h//size,w//size
borderWidth = 0.3
borderColor = '#E0E0E0'
print(rows,cols)

mat = []


###
###
### Pixel class
###
###
class Pixel:
    def __init__(self,p1,p2):
        self.frame = Rectangle(p1,p2)
        self.frame.setWidth(borderWidth+.2)
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


###
###
### Button class
###
###
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
              

###
###
### Menu class
###
###
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


##
##
## Main
##
##
def main():
    drawGrid()
    setupMatrix()
    menu = Menu(menuSize,win)
    while True:
        clickPoint = win.getMouse()
        offMat = clickPoint.getY() >= win.getHeight()-menuSize
        if offMat:
            if menu.clearButtonSelected(clickPoint):
                menu.highlightClearButton()
                undrawMatrix()
            elif menu.colorButtonSelected(clickPoint):
                menu.updateColorSelection()
        else:
            row,col = select(clickPoint)
            if mat[row][col].isDrawn:
                mat[row][col].setFill(menu.selectedColor)
            else:
                mat[row][col].setFill(menu.selectedColor)
                mat[row][col].draw(win)

def drawGrid():
    for i in range(h):
        line = Line(Point(0,i*size),Point(w,i*size))
        line.setWidth(borderWidth)
        line.setFill(borderColor)
        line.draw(win)
    for i in range(w):
        line = Line(Point(i*size,0),Point(i*size,h))
        line.setWidth(borderWidth)
        line.setFill(borderColor)
        line.draw(win)

def setupMatrix():
    for i in range(rows):
        row = []
        for j in range(cols):
            x,y,offset = (j)*size,(i)*size,size/2
            p1 = Point(x,y)
            p2 = Point(x+size,y+size)
            row.append(Pixel(p1,p2))
        mat.append(row)

def select(pt):
    x1,y1 = pt.getX(),pt.getY()
    x2,y2 = x1/(w/cols),y1/(h/rows)
    x,y = int(x2),int(y2)
    return y,x

def undrawMatrix():
    for row in mat:
        for col in row:
            col.undraw()

main()










