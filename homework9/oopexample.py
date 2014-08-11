from Tkinter import *
import random
import copy
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



class WizardGame(Animation):
    def init(self):
        self.wizard=Wizard(self.widh/2,self.height/2)
    def keyPressed(self,event):
        c = event.char
        if(c=="w"):self.wizard.move(0,-1)
        elif(c=="a"):self.wizard.move(-1,0)
        elif(c=="s"):self.wizard.move(0,1)
        elif(c=="d"):self.wizard.move(1,0)

def redrawAll(self):
    canvas=self.canvas
    self.wizard.draw(canvas)
    numEnemies =5
    for i in xrange(numEnemies):
        enemies.append(Enemy(random.randint(0,self.width),random.randint(0,self.height)))

def timerFired(self):
    self.enemies =[e for e in self.enemies if not self.wizard.overlaps(e)]


class wizard(object):
    def __init__(self,x,y):
        self.x,self.y =x,y
        self.r =15
        self.color="purple"
    def overlaps(self,other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx**2 + dy**2)**0.5 < self.r+other.redrawAll

    def draw(self,canvas):
        cx,cy,r= self.x,self.y,self.r
        canvas.create_oval()
