from Button import Button
from Graphics import *
from math import *
from Menu import Menu
from Pixel import Pixel
from time import sleep

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










