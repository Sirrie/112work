#oop game

from Tkinter import *
import random
import copy
import ter as tp
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
            #self.__init__()
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
        foo = self.track.getImage(self.track.cap)
        self.car.xPosition=foo[0]
        self.car.yPosition=foo[1]
        
        print "foo = ", foo
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
        self.track=tp.TrackObject()
        self.track.init()
        #self.track.main()

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
    def drawItem(self,canvas):
        r=self.radius
        cx=self.xPosition
        cy=self.yPosition
    
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


