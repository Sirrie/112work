#homework7.py# hw2.py
# name + andrewId + section

"""
   ** Place your manually-graded (Reasoning Over Code) solutions here! **
"""

######################################################################
# Place your non-graphics solutions here!
######################################################################

def sumOfSquaresOfDigits(n):
    return 42

def isHappyNumber(n):
    return 42

def nthHappyNumber(n):
    return 42

def isPrime(n): # from course notes
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = int(round(n**0.5))
    for factor in xrange(2,maxFactor+1):
        if (n % factor == 0):
            return False
    return True

def isHappyPrime(n):
    return 42

def nthHappyPrime(n):
    return 42

##############################################
## Prime Counting
##############################################

def pi(n):
    return 42

def h(n):
    return 42

def estimatedPi(n):
    return 42

def estimatedPiError(n):
    return 42

######################################################################
##### ignore_rest: The autograder will ignore all code below here ####
######################################################################

######################################################################
# Place your (optional) additional tests here
######################################################################

def runMoreStudentTests():
    print "Running additional tests...",
    #### PUT YOUR ADDITIONAL TESTS HERE ####
    print "Passed!"

######################################################################
# Place your graphics solutions here!
######################################################################

from Tkinter import *
import math

def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

def drawCircle(canvas, x0, y0, x1, y1):
    width = x1 - x0
    if (width > 200):
        fill = "blue"
    else:
        fill = rgbString(147, 197, 114) # pistachio!
    canvas.create_oval(x0, y0, x1, y1, fill=fill, width=4)

def drawArrow(canvas, x0, y0, x1, y1):
    pass

def drawGradient(canvas, x0, y0, x1, y1):
    pass

def drawGrid(canvas, x0, y0, x1, y1):
    if x1-x0>200:
        size=1
    else:
        size=0
    width=x1-x0
    height=y1-y0
    initialNumbera=8
    initialNumberb=4
    if size==1:
        rowNumber=initialNumbera
        colNumber=initialNumberb
    else:
        rowNumber=initialNumbera
        colNumber=initialNumberb
    cellwidth=width/colNumber
    cellheight=height/rowNumber
    number=1
    if size ==1:
        for row in xrange(initialNumberb):
            for col in xrange(initialNumbera):
                drawRectangle(canvas,row,col,cellwidth,cellheight,number,size)
                number+=1
    else:
        for col in xrange(initialNumberb):
            for row in xrange(initialNumbera,-1,-1):
                drawRectangle(canvas,row,col,cellwidth,cellheight,number,size)
                number+=1



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

def drawSpiral(canvas, x0, y0, x1, y1):
    pass

######################################################################
# Drivers: do not modify this code
######################################################################

def onButton(canvas, drawFn):
    canvas.data.drawFn = drawFn
    redrawAll(canvas)
    
def redrawAll(canvas):
    canvas.delete(ALL)
    canvas.create_rectangle(0,0,canvas.data.width,canvas.data.height,fill="cyan")
    drawFn = canvas.data.drawFn
    if (drawFn):
        canvas.create_rectangle(50, 50, 450, 450, width=4)
        drawFn(canvas, 50, 50, 450, 450)
        canvas.create_rectangle(500, 150, 700, 350, width=4)
        drawFn(canvas, 500, 150, 700, 350)
        canvas.create_text(canvas.data.width/2,20, text=drawFn.__name__, fill="black", font="Arial 24 bold")

def graphicsMain():
    root = Tk()
    canvas = Canvas(root, width=750, height=500)
    class Struct: pass
    canvas.data = Struct()
    canvas.data.width = 750
    canvas.data.height = 500
    buttonFrame = Frame(root)
    canvas.data.drawFns = [drawCircle, drawArrow, drawGradient, drawGrid, drawSpiral]
    canvas.data.drawFn = canvas.data.drawFns[0]
    for i in xrange(len(canvas.data.drawFns)):
        drawFn = canvas.data.drawFns[i]
        b = Button(buttonFrame, text=drawFn.__name__, command=lambda drawFn=drawFn:onButton(canvas, drawFn))
        b.grid(row=0,column=i)
    canvas.pack()
    buttonFrame.pack()
    redrawAll(canvas)
    root.mainloop()

######################################################################
# Main: you may modify this to run just the parts you want to test
######################################################################

def main():
    # include following line to autograde when you run this file
    #execfile("hw2-public-grader.py", globals())
    runMoreStudentTests()
    graphicsMain()

if __name__ == "__main__":
    main()