from Tkinter import *
import math


def drawGrid(canvas, x0, y0, x1, y1):
    if x1-x0>200:size=1
    else:size=0
    width=x1-x0
    height=y1-y0
    initialNumbera=4
    initialNumberb=8
    if size==1:
        rowNumber=initialNumbera
        colNumber=initialNumberb
    else:
        rowNumber=initialNumberb
        colNumber=initialNumbera
    cellwidth=width/colNumber
    cellheight=height/rowNumber
    drawGridHelper(canvas,size,colNumber,rowNumber,cellwidth,cellheight)

def drawGridHelper(canvas,size,colNumber,rowNumber,cellwidth,cellheight):
    number=1
    if size==1:
        for row in xrange(rowNumber):
            for col in xrange(colNumber):
                drawRectangle(canvas,row,col,cellwidth,cellheight,number,size)
                number+=1
    else:
        for col in xrange(colNumber):
            for row in xrange(rowNumber,-1,-1):
                drawRectangle(canvas,row,col,cellwidth,cellheight,number,size)
                number+=1


# helper function for drawing rectangle
def drawRectangle(canvas,row,col,cellwidth,cellheight,number,size):
    x0=col*cellwidth
    y0=row*cellheight
    x1=x0+cellwidth
    y1=y0+cellheight
    if size==1:
        if (row+col)%2==0:
            color = 'pink'
        else:
            color = 'purple'
    else:
        if (row+col)%2==0:
            color = 'black'
        else:
            color = 'white'
    canvas.create_rectangle(x0,y0,x1,y1,fil=color)
    canvas.create_text(x0+cellwidth/2,y0+cellheight/2,text=str(number),fill='red')

root=Tk()
canvas = Canvas(root, width=750, height=500)
canvas.pack()
drawGrid(canvas,0,0,150,150)
root.mainloop()

