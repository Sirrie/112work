#invasion_backup.py
 #invasion.py
  
from Tkinter import *
import math



    
def invaTimerFired(canvas):



    invaRedrawAll(canvas)
    delay = 250 # milliseconds
    def f():
        invaTimerFired(canvas)
    canvas.after(delay, f) # pause, then call timerFired again

def invaRedrawAll(canvas):
    canvas.delete(ALL)
    drawBottomShapes(canvas)
    #drawFallingShapes(canvas)




def drawBottomShapes(canvas):
    # draw the botton shapes at the bottom
    shapeLocations=canvas.data.bottomShapes
    #shapeColors=canvas.data.shapeColors
    #number=3
    #len(shapeLocations)
    print shapeLocations

    for i in xrange(len(shapeLocations)):
        #color = shapeColors[i]
        (cx,cy,color)= shapeLocations[i]
        print(cx,cy,color)
        drawShape(canvas,cx,cy,i+3,color)


# directly draw the shapes
def drawShape(canvas,cx,cy,n,fillColor):
    pts=[]
    for step in xrange(n):
        theta = math.radians(90 + step*360/(n))
        r = canvas.data.r
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
    canvas.data.shapeColors=["red","yellow","green","blue","purple","brown"]
    shapes=[]
    for e in xrange(canvas.data.cellNumber-2):
        print e
        shapes.append(((cellWidth/2)+e*cellWidth,cellHeight*(cellNumber-1),canvas.data.shapeColors[e+1]))
    canvas.data.bottomShapes=shapes
    print canvas.data.bottomShapes
    
    canvas.data.r=cellWidth/2/2


    canvas.data.starNumber=0
    canvas.data.mouseCounter=0
    canvas.data.winStarNumber=5
    


    #newFallingShapes(canvas)
    invaRedrawAll(canvas)

########### copy-paste below here ###########

def run(width,height):
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
  
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run(1000,800)