#hw10.py
'''
siyuchen homework10

andrewID  siyuchen


'''


'''
##---------------------------------------------------------------------------##
OOP game:
#oop game

#oop game

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


class Game(Animation):
   
    def keyPressed(self,event):
        # if it is Up move car up
        # if it is Down move car down
        # if it is h make the draw helper True
        # if it is r
        if (event.char=="h"):
            self.printHelp = not self.printHelp
        elif(event.char == "r"):
        # create a new game
            self.__init__()
            self.init()
        # in the game we have differnet 
        if(self.isGameOver==False):
            if(event.keysym == "Up"):
                self.car.moveItem(self.car.moveVertical,-1,self.moveDy)
            elif(event.keysym == "Down"):
                self.car.moveItem(self.car.moveVertical,1,self.moveDy)
            elif(event.char=="s"):
                self.Bullets.append(Bullet(self.car.xPosition,self.car.yPosition))
                self.isThereBullet = True
        self.redrawAll()

    def drawHelpPage(self):
        # print helper texts
        cellHeight=self.height/10
        cellShift = 10
        self.canvas.create_text(self.width/2,cellHeight*0+cellShift,text="this is the help page ")
        self.canvas.create_text(self.width/2,cellHeight*1+cellShift,text="press up and down to move the blue car")
        self.canvas.create_text(self.width/2,cellHeight*2+cellShift,text="avoid red barriers and eat yellow new life")
        self.canvas.create_text(self.width/2,cellHeight*3+cellShift,text="press 's' to shoot bullets target at barriers ")
        self.canvas.create_text(self.width/2,cellHeight*4+cellShift,text="press 'r' to restart the game ")

        self.canvas.create_text(self.width/2,cellHeight*5+cellShift,text="press 'h' to go to the help page and 'h' to goback ")
        

    def redrawAll(self):
        # if it is started or when we press h 
        if self.printHelp:
            self.drawHelpPage()
        elif self.isGameOver:
             self.drawGameOver()
        else:
        # draw the car
            self.car.drawItem(self.canvas)
        # draw all the enemies
            for enemy in self.Enemies:
                enemy.drawItem(self.canvas)
            for b in self.Bullets:
                b.drawItem(self.canvas)
            self.drawScore()
    def drawGameOver(self):
        self.canvas.create_text(self.width/2,self.height/2,text="GAME OVER PRESS R TO RESTART ")

    def drawScore(self):
        self.canvas.create_text(0,0,anchor=NW, text="Present Life"+str(self.life))

    def timerFired(self):
        # when in 
        if(self.isGameOver==False and self.printHelp==False):
            # every time when lifeCounter== inputRound
            self.moveEnemies()
            self.moveBullets()
            # I need to add some thing we need to add the barrier,
            # every 10 times we add a newlife 
            if len(self.Enemies)!=0:
                for e in self.Enemies:
                    # if we go out of the window delete them
                    if e.xPosition<=self.startShift:
                        self.Enemies.remove(e)
                # every time we add a new barrier
                self.Enemies.append(Barrier(self.width,self.randomY()))
                if self.lifeCounter % self.lifeInputRound==0:   
                    self.Enemies.append(NewLife(self.width,self.randomY()))
                self.lifeCounter+=1
            else:
                self.Enemies.append(Barrier(self.width,self.randomY()))
            # call meetBarrier 
            self.meetBarrier()
            if self.isThereBullet:
                self.eliminateBarrier()
            self.redrawAll()
     
    # helper funciton randomly generate y position to place the bullet
    def randomY(self):
        return random.randrange(0,self.height-1,2*self.car.radius)

    def moveBullets(self):
        for b in self.Bullets:
            b.moveItem(b.moveVertical,0,-self.moveDx)

    def moveEnemies(self):
        # every time move the Enemies according to the 
        for e in self.Enemies:
            e.moveItem(e.moveVertical,0,self.moveDx)
    
    def eliminateBarrier(self):
        # for every bullet we need to ellimate an enemy
        listBullets=copy.copy(self.Bullets)
        listEnemies=copy.copy(self.Enemies)
        # for every bulltes
        for b in listBullets:
            x = b.xPosition
            y = b.yPosition
            if b.xPosition>=self.width:
                continue
                # check whether we can meet the enemy
            for e in listEnemies:
                if ((abs(e.xPosition-x)<2*b.radius and abs(e.yPosition-y)<2*b.radius)):
                    self.Bullets.remove(b)
                    self.Enemies.remove(e)
                    listEnemies=copy.copy(self.Enemies)
                    break                 
        if len(self.Bullets)==0:
            self.isThereBullet = False

    def meetBarrier(self):
        # meet the barrier then game over
        if len(self.Enemies)!=0:
            for e in self.Enemies:
                if (abs(self.car.xPosition-e.xPosition )<self.car.radius*2 and
                    abs(self.car.yPosition-e.yPosition)<self.car.radius*2):
                    if type(e)==Barrier:
                        self.life -=1
                    else:
                        #or meet the newlife and increase the life
                        self.life +=1
        if self.life <0:
            self.isGameOver = True
    

    def init(self):
        # init the viralbes
        startShift = self.startShift = 30
        width =self.width 
        height=self.height
        self.car = Car(startShift,width/2)
        self.Enemies = []
        self.Bullets = []
        self.life = 1
        self.moveDx = -20
        self.moveDy = 10
        self.yCell = []
        self.printHelp = True
        self.lifeCounter=0
        self.lifeInputRound = 10
        self.isGameOver = False
        self.isThereBullet = False

class Item(object):
    def __init__(self,x,y):
        self.yPosition= y
        self.xPosition= x
        self.radius   = 10
        


    def moveItem(self,v,dir,speed):
        # move Item according to their direction its horizontal or vertical
        if v :
            self.yPosition +=dir * speed
        else:
            self.xPosition +=speed


    def drawItem(self,canvas):
        # draw the Item according to their postion
        r=self.radius
        cx=self.xPosition
        cy=self.yPosition
        (x0,y0,x1,y1)=(cx-r,cy-r,cx+r,cy+r)
        canvas.create_rectangle(x0,y0,x1,y1,fill=self.color)



# create class s       
class Car(Item):
    def __init__(self,x,y):
        super(Car,self).__init__(x,y)
        self.color = "blue"
        self.moveVertical = True
    def shoot():
        Bullet(slef.xPosition,self.yPosition)

    
# when meet with barriers we will lose one point 
class Barrier(Item):
    def __init__(self,x,y):
        super(Barrier,self).__init__(x,y)
        self.color = "red"
        self.moveVertical = False
        
# when we eat NewLife we will increase life record
class NewLife(Item):
    def __init__(self,x,y):
        super(NewLife,self).__init__(x,y)
        self.color = "yellow"
        self.moveVertical = False

# Bullet will deliminate the barriers
class Bullet(Item):
    def __init__(self,x,y):   
        super(Bullet,self).__init__(x,y)
        self.color = "green"
        self.moveVertical = False
    
    def drawItem(self,canvas):
        r = self.radius
        cx= self.xPosition
        cy= self.yPosition
        (x0,y0,x1,y1)=(cx-r,cy-r/2,cx+r,cy+r/2)
        canvas.create_oval(x0,y0,x1,y1,fill=self.color)




game = Game()
game.run(600,600)







##---------------------------------------------------------------------------##
15-112 Midterm #2 - Fall 2013
1:
a:True  because we already implemented wordsearch we can do that to ease life

b:False the advantage is the file is properly closed after its suite finishes evenif an exception is raised

c:False  isinstance will take the inheritance into consideration, type will only care about the certain class type not the superclass 

d:True  outside def we just use this to unpack a list, but in def("") we need to pack it

2:
c: we use class to put the virables into the instance of the class, store them in the "self" and we just use the method of the class to avoid using closures.  and we put the class in the wrapper function to avoid using closures.
d: because in wordsearch we use randomly build a board to do wordsearch it has nothing to do with previous ones

e: to implement hash of string, we compute the number of ASCII of every character and then we sum them up.

g:Yes the set won't work, because mutable values will be hased to different places when they are changed so in the set we cannot gurantee that every element should be exactly different.


h: the first is the event, the second is the function handler that we should bind with the event


5,
def myReduce(function,iterable,initializer=None):
    it = iter(iterable)
    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:
            raise TypeError('reduce non itereable')
    accum_value=initializer
    for x in it:
        accum_value=function(accum_value,x)
    return accum_value

6,
class Q(object):
    def __init__(self):
        self.queue=[]
        self.name="Q"
    def add(self,element):
        self.queue.append(element)

    def remove(self):
        temp=self.queue.pop(0)
        return temp
    def __str__(self):
        return "<%s of size %d>" %(self.name,len(self.queue))
    
    def __eq__(self,other):
        return self.queue==other.queue

class PQ(Q):
    def __init__(self):
        super(PQ,self).__init__()
        self.name="PQ"

    def remove(self):
        self.queue.sort()
        temp=self.queue.pop(0)
        return temp

7: the solution of KingTourEditor:
from Tkinter import *

def mousePressed(canvas, event):
    #get the location the press position 
    (row,col)=getPressPosition(canvas,event)
    if canvas.data.board[row][col]==0:
        canvas.data.board[row][col]=canvas.data.step
        canvas.data.tour[canvas.data.step]=(row,col)
        canvas.data.step+=1
        canvas.data.isLeaglTour=isLeagleTour(canvas)
        if canvas.data.step==0:
            canvas.data.isLeagleTour=True

    # do nothing
   
    redrawAll(canvas)

def getPressPosition(canvas,event):
    x,y=event.x,event.y
    cellSize=canvas.data.cellSize
    row,col=event.y/cellSize,event.x/cellSize
    return(row,col)
  

def keyPressed(canvas, event):
    if(event.keysym=='u'):
        removeLast(canvas)
    redrawAll(canvas)

def removeLast(canvas):
    (rows,cols)=(canvas.data.rows,canvas.data.cols)
    if canvas.data.step>0:
        canvas.data.step-=1
        for row in xrange(rows):
            for col in xrange(cols):
                if canvas.data.board[row][col]==canvas.data.step:
                    canvas.data.board[row][col]=0
                    

def isLeagleTour(canvas):
    tour=dict()
    (rows,cols)=(canvas.data.rows,canvas.data.cols)
    
    for row in xrange(rows):
        for col in xrange(cols):
            step=canvas.data.board[row][col]
            if step!=0:
                tour[step]=(row,col)
    print len(tour),"time hewe"
    
    if len(tour)==1:
        return True
    for x in xrange(1,len(tour)):
        (rowStart,colStart)=tour[x]
        if(x+1 in tour):
            (nextRow,nextCol)=tour[x+1]
            if abs(rowStart-nextRow)>1 or abs(colStart-nextCol)>1:
                return False
    return True

def timerFired(canvas):
   
    redrawAll(canvas)
    delay = 250 # milliseconds
    def f():
        timerFired(canvas) # DK: define local fn in closure
    canvas.after(delay, f) # pause, then call timerFired again

def redrawAll(canvas): # DK: redrawAll() --> redrawAll(canvas)
    canvas.delete(ALL)
    # draw the text
    drawBoard(canvas)

def drawBoard(canvas):
    for row in xrange(canvas.data.rows):
        for col in xrange(canvas.data.cols):
            number=canvas.data.board[row][col]
            color="white"
            if number!=0:
                if canvas.data.isLeaglTour:
                    color="green"
                else:
                    color="red"
            drawCell(canvas,row,col,color,number)

def drawCell(canvas,row,col,color,number):
    x0=col*canvas.data.cellSize
    y0=row*canvas.data.cellSize
    x1=x0+canvas.data.cellSize
    y1=y0+canvas.data.cellSize
    canvas.create_rectangle(x0,y0,x1,y1,fill=color)
    if number!=0:
        canvas.create_text((x0+x1)/2,(y0+y1)/2,text=number)

def init(canvas):
    canvas.data.rows=8
    canvas.data.cols=8
    canvas.data.tour=dict()
    canvas.data.step=1
    canvas.data.cellSize=50
    canvas.data.timerCounter = 0
    canvas.data.isLeaglTour=True

    a=[]
    for row in xrange(canvas.data.rows):a+=[[0]*canvas.data.cols]
    canvas.data.board=a

def run():
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=600, height=800)
    canvas.pack()
    # Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    init(canvas) # DK: init() --> init(canvas)
    # set up events
    # DK: You can use a local function with a closure
    # to store the canvas binding, like this:
    def f(event): mousePressed(canvas, event)    
    root.bind("<Button-1>", f)
    # DK: Or you can just use an anonymous lamdba function,
    # like this:
    root.bind("<Key>", lambda event: keyPressed(canvas, event))
    timerFired(canvas) # DK: timerFired() --> timerFired(canvas)
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()
##-----------------------------------------------------------------------####

15112 S13 midterm2
1:
a   True: yes we always can use iterative way to solve that 
d   True: because the elements in set should be different, only immutable elements can be added to the set. Dictionaries are mutable

2:
a   Because  when we don't use global virable Tkinter cannot handle the bind function if we bind the canvas vitable with it, Tkinter only accept binding with a function with one argumnet

e   we need to overwrite the built in constructor __init__ function in the subclass, __init__ initialize all the aurguments you 

f   root.bind("<Button-1>",foo)   this one should tell the time to 

4:  
g
    def g(d):
    assert(type(d) == dict)
    s = set([d[key] for key in d])
    return (len(d) == len(s)**2

    d={'1':1,'2':2,'3':1,'4':2} first d should be a dictionary, and with length 4, the set should have 2 elemnts, that means, there are 2 values in dictionary d
g2  
   def f(x):return x-2    x=100
    the type of f should be function the same as g2, it is a function, and then, the L should be [100,98...2] so the f(x) should be f(x)=x-2 x =100

6:
class A(object):
    counter=0
    @classmethod
    def getCount(cls):
        return A.counter

    def __init__(self,x,y=42):
        self.x=x
        self.y=y
        A.counter+=1

    def __str__(self):
        x=self.x
        y=self.y
        counter=A.getCount()
        return "A#%d<x is %d, y is %d>"%(counter,x,y)

    def getSwappedA(self):
        x,y=(self.y,self.x)
        return A(x,y)



    

def test():

    assert(str(A(5)) == "A#1<x is 5, y is 42>")
    assert(str(A(5)) == "A#2<x is 5, y is 42>") # counter increases!
    assert(str(A(5, 99)) == "A#3<x is 5, y is 99>")
    b = A(2, 3).getSwappedA() # returns a new A with x and y swapped
    assert(type(b) == A)
    assert(str(b) == "A#5<x is 3, y is 2>")
    print "finished"
test()


7:

in the keypressed:
def keyPressed(event):
    canvas.data.ignoreNextTimerEvent = True # for better timing
    # first process keys that work even if the game is over
    if (event.char == "q"):
        gameOver()
    elif (event.char == "r"):
        init()
    elif (event.char == "d"):
        canvas.data.inDebugMode = not canvas.data.inDebugMode
    elif(event.char=="h"):
        halfSnake()
    # now process keys that only work if the game is not over
    if (canvas.data.isGameOver == False):
        if (event.keysym == "Up"):
            moveSnake(-1, 0)
        elif (event.keysym == "Down"):
            moveSnake(+1, 0)
        elif (event.keysym == "Left"):
            moveSnake(0,-1)
        elif (event.keysym == "Right"):
            moveSnake(0,+1)
    redrawAll()


def halfSnake():
    findSnakeHead()
    row,col=canvas.data.headRow,canvas.data.headCol
    max=canvas.data.snakeBoard[row][col]
    max=max/2
    for i in xrange(max):
        removeTail()


###---------------------------------------------------------------------####

from Tkinter import *
# Animation.py

import random
import math


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
###--------------------------------------------------------------####
###########################################
# Utility functions
###########################################
# if u get stuck at the place when adding line u should go to see the comment
def make2dList(rows, cols):
    a=[]
    for row in xrange(rows): a += [[0]*cols]
    return a


class DotAndBox(Animation):
    def __init__(self,rows,cols,maxSecondsPerTurn=0):
        self.rows=rows
        self.cols=cols
        self.maxSecondsPerTurn=maxSecondsPerTurn
        
    # init all the virables
    def init(self):
        self.makeDotAndBoxBoard()
        self.legalMove=[]
        self.linesBug=set()
        self.presentPlayer=1
        # see this kind of the 
        self.selectedDots=None
        self.isGameOver=False
    # create the  total DotAndBoxBoard and help to draw the dots   
    def makeDotAndBoxBoard(self):
        self.cellSize=500/(self.rows)
        self.boardMargin=100
        self.dotRadius=10
        self.titleMargin=10
        self.firstClickRow=None
        self.firstClickCol=None
        self.leagleMoves=[]
        self.clickcounter=0
        self.isDotSelcted=False
        self.selectedLine=[]
        self.scorePlayers=[0,0]
        self.timeCounter=0
        self.flashCount=0
        rows,cols=self.rows,self.cols
        # create a box to store the things in the box
        a=[]
        for row in xrange(rows-1):a+=[[0]*(cols-1)]
        self.wholeBoxes=a
        # create a board that will store all the 
        a=[]
        for row in xrange(rows):a+=[[0,0]*cols]
        board=a
        for row in xrange(rows):
            for col in xrange(cols):
                cx= self.boardMargin+self.cellSize*col
                cy= self.boardMargin+self.titleMargin+self.cellSize*row
                board[row][col]=(cx,cy)
        self.board=board
   
    def mousePressed(self,event):
        if(self.isOnBoard(event.x,event.y)):
            x,y=event.x,event.y
            # find the dot that is clicked
            for row in xrange(self.rows):
                for col in xrange(self.cols):
                    dotX,dotY=self.board[row][col]
                    distance = math.sqrt(abs(dotX-x)**2+abs(dotY-y)**2)
                    if distance<=self.dotRadius*2:
                        # get the row and col of the dot that is clicked
                       self.firstClickRow,self.firstClickCol=row,col
           # if we find the dot that is clicked call dotPressFunction
            if (self.firstClickCol!=None and self.firstClickRow!=None):
                self.dotPress(self.firstClickRow,self.firstClickCol)

    # first time you press the dot and you will  show the possible legal 
    #  move of the next dot
    def dotPress(self,row,col):
        # record the dot that is used before and then go to link the
        # check there isn't a dot clicked so we store the row and col in
        # the self.selectedDots
        if self.isDotSelcted==False:
            self.selectedDots=(row,col)
            self.isDotSelcted=True
            # get all the is the leagle move of the chosen dot
            self.flagLeagleMove(row,col)
        else:
            # if there already has a selected dot 
            (startRow,startCol)=self.selectedDots
            # everytime you should check the validation of the second circled
            # dot, if it is in the leagleMoves you add the line in the linebug
            #but if it is not in the leaglMoves you should clean the selected 
            #dot and then start a new select dot
            if list((row,col))in self.leagleMoves:
                self.linesBug.add((startRow,startCol,row,col))
                self.linesBug.add((row,col,startRow,startCol))
                # everytime after you add a line you should check whether it has formed a box
                self.checkBoxes()
                self.checkGameOver()
                # every time you add a line you change a player
                self.changePlayer()
            # every time after click the second time, just start a nother turn
            self.selectedDots=[]
            self.isDotSelcted=False
    # when all boxes are closed that is game over
    def checkGameOver(self):
        (rows,cols)=(self.rows-1,self.cols-1)
        for row in xrange(rows):
            for col in xrange(cols):
                if self.wholeBoxes[row][col]==0:
                    self.isGameOver=False
                    return
        self.isGameOver=True
    # check whether the box belongs to one player
    def checkBoxes(self):
        box=self.wholeBoxes
        (rows,cols)=(self.rows-1,self.cols-1)
        hasBoxesClosed=False
        for row in xrange(rows):
            for col in xrange(cols):
                # get the 4 points of the box
                leftUpPoint=(row,col)
                rightUpPoint=(row,col+1)
                leftBottomPoint=(row+1,col)
                rightBottomPoint=(row+1,col+1)
                if self.wholeBoxes[row][col]==0:
                    if self.closedBox(leftUpPoint,rightUpPoint,leftBottomPoint,rightBottomPoint):
                        self.wholeBoxes[row][col]=self.presentPlayer
                        self.scorePlayers[self.presentPlayer-1]+=1
                        hasBoxesClosed=True
        if hasBoxesClosed:
            #change the player for one more time so we go back to the present player
            self.changePlayer()
            #self.timeCounter=0



    def closedBox(self,leftUpPoint,rightUpPoint,leftBottomPoint,rightBottomPoint):
        # check the four lines according to their 4 points
        lines=[]
        lines.append(list((leftUpPoint,rightUpPoint)))
        lines.append(list((rightUpPoint,rightBottomPoint)))
        lines.append(list((rightBottomPoint,leftBottomPoint)))
        lines.append(list((leftBottomPoint,leftUpPoint)))
        for e in lines:
            if sum(tuple(e),()) not in self.linesBug:
                return False
        return True

    def changePlayer(self):
        self.presentPlayer+=1
        if self.presentPlayer>2:
            self.presentPlayer=1
        #everytime you change a player u should reset the timeCounter
        self.timeCounter=0
        

    # helper function to get all possible leagleMove according to the input 
    # row and col
    def flagLeagleMove(self,row,col):
        self.leagleMoves=[]
        dirs = [  (-1, 0),( 0, -1), ( 0, +1), (+1, 0) ]
        for (drow,dcol) in dirs:
            tryRow,tryCol=drow+row,dcol+col
            if(tryRow >=0 and tryCol>=0 and tryRow<self.rows and tryCol<self.cols):
                if (row,col,tryRow,tryCol)not in self.linesBug:
                    self.leagleMoves.append([tryRow,tryCol])

   #helper function to check if it is on the board

    def isOnBoard(self,x,y):
        (boardX0, boardY0, boardX1, boardY1) = self.getBoardBounds()
        return ((x >= boardX0) and (x <= boardX1) and
                (y >= boardY0) and (y <= boardY1))

    # helper function to get the board bounds and check   
    def getBoardBounds(self):
        boardX0 = self.boardMargin
        boardX1 = self.width - self.boardMargin
        boardY0 = self.titleMargin + self.boardMargin
        boardY1 = self.height - self.boardMargin
        return (boardX0, boardY0, boardX1, boardY1)

    def keyPressed(self,event):
        if (event.char=="r"):
            self.init()
    
    def timerFired(self):
        if not self.isGameOver:
            self.timeCounter+=1
            millisecondsTrans=1000
            if self.timeCounter*self.timerFiredDelay>self.maxSecondsPerTurn*1000:
                self.flashCount+=1
                # every time flash 
                if self.flashCount>10:
                    self.flashCount=0
                    self.changePlayer()
    
    def redrawAll(self):
        if not self.isGameOver:
            self.drawBoard()
            self.drawLeagleMove()
            self.drawLine()
            self.drawPlayer()
            self.drawBoxes()
            self.drawScore()
            self.drawWarning()
        else:
            score1,score2=(self.scorePlayers)
            if score1!=score2:
                if score1>score2:
                    winner=1
                elif score1<score2:
                    winner=2
                error="GAME OVER press R to restart the winner is "+str(winner)
            else:
                error="GAME OVER press R to restart the game Tie"
            self.canvas.create_text(self.cellSize*self.rows/2,self.cellSize*self.cols/2,text=error,fill="red")
        pass

    def drawWarning(self):
        if self.flashCount%2>0:
            error="PLEASE QUICK"
            self.canvas.create_rectangle(0,0,self.width,self.height,fill="white")
            self.canvas.create_text(self.cellSize*self.rows/2,self.cellSize*self.cols/2,text=error,fill="red")

    def drawBoxes(self):
        (rows,cols)=(self.rows-1,self.cols-1)
        for row in xrange(rows):
            for col in xrange(cols):
                # get the 4 points of the box
                positionx,positiony=self.board[row][col]
                cellSize=self.cellSize
                self.canvas.create_text(positionx+cellSize/2,positiony+cellSize/2,text=self.wholeBoxes[row][col])

    
    # draw the score according to the playsers
    def drawScore(self):
        showMessage="the socre of Player1 and Player2 is "+str(self.scorePlayers)
        self.canvas.create_text(self.boardMargin*2,self.boardMargin/2,anchor=SW,text=showMessage)


    #print the player information    
    def drawPlayer(self):
        present="present Player"+str(self.presentPlayer)
        self.canvas.create_text(self.boardMargin/2,self.boardMargin/2,text=present)


    def drawLine(self):
        if self.isDotSelcted:
            self.canvas.create_text(self.boardMargin*5,self.boardMargin,text="select another dot to add a line")
        for (sr,sc,er,ec) in self.linesBug:
            (sx,sy)=self.board[sr][sc]
            (ex,ey)=self.board[er][ec]
            self.canvas.create_line(sx,sy,ex,ey)

    def drawLeagleMove(self):
        r=self.dotRadius
        leagleMoves=self.leagleMoves
        if len(leagleMoves)>0:
            for (row,col) in self.leagleMoves:
                (cx,cy)=self.board[row][col]
                self.canvas.create_oval(cx-r,cy-r,cx+r,cy+r,fill="yellow")
    def drawBoard(self):
        r=self.dotRadius
        for row in xrange(self.rows):
            for col in xrange(self.cols):
                (cx,cy)=self.board[row][col]
                self.canvas.create_oval(cx-r,cy-r,cx+r,cy+r,fill="black")


def runDotAndBOx(rows,cols,maxSecondsPerTurn=10):
    game=DotAndBox(rows,cols,maxSecondsPerTurn)
    game.run(600,600)

runDotAndBOx(3,3)


'''