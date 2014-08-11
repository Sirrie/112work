#invasion.py
  
from Tkinter import *
import math

def invaMousePressed(event,canvas):
    # when you press the mouse once you find the index of the shape 
    # that you click on you can first change the color and then the 
    # second time swap it
    selectedShape=clickSelectedShape(event,canvas)
    mouseClickCounter=canvas.data.mouseClickCounter
    if selectedShape!=None:
        mouseClickCounter+=1
        if mouseClickCounter==1:
            #changeShapeColor(canvas,selectedShape)
            canvas.data.selectedShape=selectedShape
            canvas.data.previous=selectedShape
            canvas.data.mouseClickCounter=mouseClickCounter
        elif mouseClickCounter==2:
            swapShape(canvas,selectedShape)
            # every time after I check I should update the starNumber and check
            # is gameover and if game is not over we should generate new 
            # falling shapes
            if checkMatch(canvas):
                print "mimimi"
                canvas.data.starNumber+=1
                if canvas.data.starNumber <0 or canvas.data.starNumber==5:
                    canvas.data.isGameOver=True
                else:
                    newFallingShapes(canvas)
            mouseClickCounter=0
            canvas.data.mouseClickCounter=mouseClickCounter
            canvas.data.selectedShape=None
    # check whether the falling shapes and the bottom shapes match        
    



    invaRedrawAll(canvas)
# return the selected index of the shape
def clickSelectedShape(event,canvas):
    bottomShapes=canvas.data.bottomShapes
    (x,y)=(event.x,event.y)
    print (x,y)
    counter=0
    r=canvas.data.r
    for (bx,by) in bottomShapes:
        (top,bottom,left,right)=(by-r,by+r,bx-r,bx+r)
       # we should check that y should be smaller than the bottom but 
       #larger than the top
        if (( x>left and x<right) and (y<bottom and y>top)):
            return counter
        counter+=1

    return None
# given the index of the shape change it's color
#def changeShapeColor(canvas,selectedShape):
 #   pass


# change the shape collor if it is chosen
def changeShapeColor(canvas,selectShape):
    # updatae the color that has been chosen
    bottomShapes=canvas.data.bottomShapes
    (cx,cy)=bottomShapes[selectShape]
    color=canvas.data.shapeColors[0]
    canvas.data.bottomShapes[selectShape]=(cx,cy)

def invaKeyPressed(event,canvas):
    if(event.char=="r"):
        invaInit(canvas)

    invaRedrawAll(canvas)

# we need to swap the target chosen  place
def swapShape(canvas,selectShape):

    presentShapes=canvas.data.bottomShapes
    previous=canvas.data.previous
    # swap those things
    (presentShapes[previous],presentShapes[selectShape])=(presentShapes[selectShape],presentShapes[previous])
    
    canvas.data.bottomShapes=presentShapes






def moveFallingShapes(canvas):
    # move falling Shapes step by step
    fallingShapes=canvas.data.newFallingShapes
    cellHeight=canvas.data.cellHeight
    #if fallingShapeIsLegal(canvas):

    for index in xrange(len(fallingShapes)):
        (cx,cy)=fallingShapes[index]
        fallingShapes[index]=(cx,cy+cellHeight/10)
    canvas.data.newFallingShapes=fallingShapes


    

def checkMatch(canvas):
    bottomShapes=canvas.data.bottomShapes
    fallingShapes=canvas.data.newFallingShapes
    # when falling shapes get to the bottom check wether they are the same as
    # the bottom ones
    xFalling=[]
    xBottom=[]
    for i in xrange(len(bottomShapes)):
        (xf,yf)=fallingShapes[i]
        (xb,yb)=bottomShapes[i]
        xFalling.append(xf)
        xBottom.append(xb)
    return xFalling==xBottom





import random
import copy
def newFallingShapes(canvas):
    # geneerate new falling 
    # we should use copy.copy
    bottomShapes=copy.copy(canvas.data.bottomShapes)
    random.shuffle(bottomShapes)
    newShapes=bottomShapes
    for index in xrange(len(newShapes)):
        (cx,cy)=newShapes[index]
        newShapes[index]=(cx,canvas.data.r)
    canvas.data.newFallingShapes=newShapes


    
def invaTimerFired(canvas):

    #newFallingShapes(canvas)
    if(canvas.data.isGameOver==False):
        moveFallingShapes(canvas)
        # check if it has already get to the bottom
        fallingShapes=canvas.data.newFallingShapes
        bottomShapes=canvas.data.bottomShapes
        (cx,cy)  =fallingShapes[0]
        (cx0,cy0)=bottomShapes[0]
        # when go to the bottom, starNumber should -1
        if cy==cy0:
            if not checkMatch(canvas):
                canvas.data.starNumber-=1
            # check whether the game ends
            if (canvas.data.starNumber <0 or 
                canvas.data.starNumber==canvas.data.winStarNumber):
                canvas.data.isGameOver=True
            else:
                print " hello "
                newFallingShapes(canvas)

        invaRedrawAll(canvas)
    #whether or not game is over, call next timerFired
    delay = 100+150/(2+canvas.data.starNumber) # milliseconds
    def f():
        invaTimerFired(canvas)
    canvas.after(delay, f) # pause, then call timerFired again

def invaRedrawAll(canvas):
    canvas.delete(ALL)
    drawBottonShapes(canvas)
    drawFallingShapes(canvas)
    drawStars(canvas)
    cx=canvas.data.canvasWidth/2
    cy=canvas.data.canvasHeight/2
    if canvas.data.isGameOver==True:
        if canvas.data.starNumber==5:
            canvas.create_text(cx,cy,text="YOU WIN",font=("Helvetica",32,"bold"))
        if canvas.data.starNumber==-1:
            canvas.create_text(cx,cy,text="YOU LOSE",font=("Helvetica",32,"bold"))





def drawBottonShapes(canvas):
    # draw the botton shapes at the bottom
    shapeLocations=canvas.data.bottomShapes
    shapeColors=canvas.data.shapeColors
    
    selectedShape=canvas.data.selectedShape
    #len(shapeLocations)
    for i in xrange(len(shapeLocations)):
        if i == selectedShape:
            color="red"
        else:
            color = shapeColors[i+1]
        (cx,cy)= shapeLocations[i]

        drawShape(canvas,cx,cy,i,color)


# directly draw the shapes
def drawShape(canvas,cx,cy,n,fillColor):
    r=canvas.data.r
    (x0,y0,x1,y1)=(cx-r,cy-r,cx+r,cy+r)
    if n==0:
        #to do drawTriangle(x0,y0,x1,y1)  accroding to the input
        canvas.create_polygon([((x0+x1)/2,y0),(x0,y1),(x1,y1)],fill=fillColor)
    elif n==1:
        #to do drawSquare(x0,y0,x1,y1) according to the input
        canvas.create_polygon([(x0,y0),(x0,y1),(x1,y1),(x1,y0)],fill=fillColor)
    elif n==2:
        #to do drawPentagram(x0,y0,x1,y1)according to the input
        parameterx=0.5
        #parametery=0.82
        canvas.create_polygon([(cx-r,cy),(cx,cy-r),(cx+r,cy),(cx+parameterx*r,y1),(cx-parameterx*r,y1)],fill=fillColor)
    elif n==3:
        #to do drawHexagon(x0,y0,x1,y1) according to the input
        parameterx=0.5
        canvas.create_polygon([(x0+parameterx*r,y0),(x1-parameterx*r,y0),(x1,cy),(x1-parameterx*r,y1),(x0+parameterx*r,y1),(x0,cy)],fill=fillColor)
    else:
        canvas.create_oval(x0,y0,x1,y1,fill=fillColor)

def drawFallingShapes(canvas):
    fallingShapes=canvas.data.newFallingShapes
    shapeColors=canvas.data.shapeColors
    for i in xrange(len(fallingShapes)):
        color = shapeColors[i+1]
        (cx,cy)= fallingShapes[i]

        drawShape(canvas,cx,cy,i,color)


def drawStars(canvas):
    # draw the star on the left
    cellNumber=5
    (x0,y0,x1,y1)=(0,0,canvas.data.cellWidth*2,canvas.data.cellHeight)
    starCellSize=(x1-y1)/cellNumber
    starCenter=[]
    for i in xrange(5):
        starCenter.append((starCellSize/2+i*starCellSize,starCellSize))
    r=canvas.data.r
    counter=canvas.data.starNumber
    for (cx,cy)in starCenter:
        drawStar(canvas,cx,cy,None,r/2,cellNumber,"black")
        if counter >0:
            drawStar(canvas,cx,cy,None,r/2-2,cellNumber,"yellow")
            counter-=1
        else:
            drawStar(canvas,cx,cy,None,r/2-2,cellNumber,"white")

def drawStar(canvas, cx, cy, rInner, rOuter, n, fillColor):
    if (rInner == None):
        thetaInner = math.radians(90 + 360/(2*n))
        thetaOuter = math.radians(90 + 2*360/(2*n))
        rInner = rOuter*math.sin(thetaOuter)/math.sin(thetaInner)
    pts = []
    for step in xrange(2*n):
        theta = math.radians(90 + step*360/(2*n))
        r = rOuter if (step % 2 == 0) else rInner
        x = cx + r*math.cos(theta)
        y = cy - r*math.sin(theta)
        pts += [(x,y)]
    canvas.create_polygon(pts, fill=fillColor)




def invaInit(canvas):
    canvas.data.cellNumber=7
    cellNumber=canvas.data.cellNumber
    canvas.data.cellWidth=canvas.data.canvasWidth/canvas.data.cellNumber
    cellWidth=canvas.data.cellWidth
    cellHeight=canvas.data.canvasHeight/canvas.data.cellNumber
    canvas.data.cellHeight=cellHeight
    canvas.data.shapeColors=["red","yellow","green","blue","purple","brown"]
    shapes=[]
    for e in xrange(canvas.data.cellNumber-2):
        print e
        shapes.append(((cellWidth/2)+(e+2)*cellWidth,cellHeight*(cellNumber-1)))
    canvas.data.bottomShapes=shapes
    
    canvas.data.r=cellWidth/2/2
    # use this to denote the selected shape
    canvas.data.previous=None
    canvas.data.selectedShape=None
    canvas.data.starNumber=0
    canvas.data.mouseClickCounter=0
    canvas.data.winStarNumber=5
    canvas.data.isGameOver=False
    

    newFallingShapes(canvas)
    invaRedrawAll(canvas)

########### copy-paste below here ###########

def runInvasion(width,height):
    # create the root and the canvas
    global canvas
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    canvas.data.canvasWidth=width
    canvas.data.canvasHeight=height
    invaInit(canvas)
    # set up events
    root.bind("<Button-1>", lambda event:invaMousePressed
        (event,canvas))
    root.bind("<Key>",lambda event: invaKeyPressed(event,canvas))
    invaTimerFired(canvas)
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

runInvasion(1000,800)