# AnimationWithClasses.py

import random
from Tkinter import *

###########################################
# Animation class
###########################################

class Animation(object):
    # Override these methods when creating your own animation
    def mousePressed(self, event): pass
    def keyPressed(self, event): pass
    def timerFired(self): pass
    def init(self): pass
    def redrawAll(self): pass
    
    # Call app.run(width,height) to get your app started
    def run(self, width=300, height=300):
        # create the root and the canvas
        root = Tk()
        self.width = width
        self.height = height
        self.canvas = Canvas(root, width=width, height=height)
        self.canvas.pack()
        # set up events
        def redrawAllWrapper():
            self.canvas.delete(ALL)
            self.redrawAll()
        def mousePressedWrapper(event):
            self.mousePressed(event)
            redrawAllWrapper()
        def keyPressedWrapper(event):
            self.keyPressed(event)
            redrawAllWrapper()
        root.bind("<Button-1>", mousePressedWrapper)
        root.bind("<Key>", keyPressedWrapper)
        # set up timerFired events
        self.timerFiredDelay = 250 # milliseconds
        def timerFiredWrapper():
            self.timerFired()
            redrawAllWrapper()
            # pause, then call timerFired again
            self.canvas.after(self.timerFiredDelay, timerFiredWrapper)
        # init and get timerFired running
        self.init()
        timerFiredWrapper()
        # and launch the app
        root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

###########################################
# EventsExample1 class
###########################################

class EventsExample1(Animation):
    def mousePressed(self, event):
        self.mouseText = "last mousePressed: " + str((event.x, event.y))
    
    def keyPressed(self, event):
        self.keyText = "last keyPressed: char=" + event.char + ", keysym=" + event.keysym
    
    def timerFired(self):
        self.timerCounter += 1
        self.timerText = "timerCounter = " + str(self.timerCounter)
    
    def redrawAll(self):
        self.canvas.create_text(150,20,text="events-example1 using Animation class!")
        self.canvas.create_text(150,40,text=self.mouseText)
        self.canvas.create_text(150,60,text=self.keyText)
        self.canvas.create_text(150,80,text=self.timerText)
    
    def init(self):
        self.mouseText = "No mousePresses yet"
        self.keyText = "No keyPresses yet"
        self.timerText = "No timerFired calls yet"
        self.timerCounter = 0

#app = EventsExample1()
#app.run(300,500)

#########################################################
# AnimationWithRetainedGraphics class
# with Color, Shape, Rectangle, Oval, and Circle classes
#########################################################

class Color(object):
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    @classmethod
    def randomColor(cls):
        r = random.randrange(256)
        g = random.randrange(256)
        b = random.randrange(256)
        return Color(r, g, b)

    def rgbString(self):
        return "#%02x%02x%02x" % (self.red, self.green, self.blue)

class Shape(object):
    def __init__(self, left, top, right, bottom):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.fill = None
        self.line = Color(0, 0, 0)
        self.lineWidth = 1
        print self.width
    
    def getFill(self):
        return None if (self.fill == None) else self.fill.rgbString()
        
    def getLine(self):
        return None if (self.line == None) else self.line.rgbString()

class Rectangle(Shape):
    def draw(self, canvas):
        canvas.create_rectangle(self.left, self.top, self.right, self.bottom,
                                fill=self.getFill(),
                                outline=self.getLine(), width=self.lineWidth)

class Oval(Shape):       
    def draw(self, canvas):
        canvas.create_oval(self.left, self.top, self.right, self.bottom,
                           fill=self.getFill(),
                           outline=self.getLine(), width=self.lineWidth)

class Circle(Oval):
    def __init__(self, cx, cy, r):
        (left, top, right, bottom) = (cx-r, cy-r, cx+r, cy+r)
        # Call superclass's __init__ method
        super(Circle, self).__init__(left, top, right, bottom)

class AnimationWithRetainedGraphics(Animation):
    def __init__(self):
        self.shapes = [ ]
    

    def addShape(self, shape):
        self.shapes.append(shape)
        return shape

    def createRectangle(self, left, top, right, bottom):
        return self.addShape(Rectangle(left, top, right, bottom))

    def createOval(self, left, top, right, bottom):
        return self.addShape(Oval(left, top, right, bottom))

    def createCircle(self, cx, cy, r):
        return self.addShape(Circle(cx, cy, r))

    def redrawAll(self):
        for shape in self.shapes:
            shape.draw(self.canvas)        

class RetainedGraphicsExample(AnimationWithRetainedGraphics):
    def mousePressed(self, event): self.randomizeColors()
    def keyPressed(self, event): self.randomizeColors()
    
    def randomizeColors(self):
        self.rect.line = Color.randomColor()
        self.oval.fill = Color.randomColor()
        self.circle.fill = Color.randomColor()

    def timerFired(self):
        self.rect.left += 10
        if (self.rect.left > self.width): self.rect.left = -150
        self.rect.right = self.rect.left + 150
        
    def init(self):
        print "Click to randomize colors"
        self.rect = self.createRectangle(50, 50, 200, 150)
        self.oval = self.createOval(75, 50, 225, 150)
        self.rect.lineWidth = 2
        self.rect.line = Color(255, 165, 0)   # orange
        self.oval.fill = Color(137, 207, 240) # baby blue
        self.circle = self.createCircle(150, 100, 40) # (cx, cy, radius)
        self.timerFiredDelay = 1 

app = RetainedGraphicsExample()
app.run()