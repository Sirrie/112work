from Tkinter import *
import random
import copy
import math
#import track as track
import Item as item
import player as p
import enmies as e
import weapen as w
#import bounus as b
import pyaudio
import wave

class Animation(object):
    # Override these methods when creating your own animation
    def mousePressed(self, event): pass
    def keyPressed(self, event): pass
    def mouseMotion(self,event): pass
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
        def mouseMotionWrapper(event):
            self.mouseMotion(event)
            redrawAllWrapper()
        root.bind("<Button-1>", mousePressedWrapper)
        root.bind("<Key>", keyPressedWrapper)
        root.bind("<Motion>",mouseMotionWrapper)
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
    def init(self):
        width = self.width
        height = self.height
        self.player=p.Player(width/2,height/2,"images/hamster.gif")
    
        # decide when to 
        self.EnemyCycleRound=10
        self.EnemyBirdCyclceCoeff=1
        self.EnemySheepCycleCoeff=2

        self.levels= dict()

        self.EnemyPresentCounter=0
        # decide the diciculty of the game, to gurantee 5 enemies on the screen
        self.Dificulty       = 5
        #self.Dificulty      = 1

        self.topBoxes   = []

        self.Enemies=[]
        self.Bullets=[]
        self.otherWeapens=[]
        

        self.level =1 
        self.screen = "Menu"
        self.isGameOver=False


       # self.warningFlash=False

        self.endLevelCounter=4

        self.warningCounter=3
        #self.areThereEnemies = False
        #self.areThereBulltes = False



        self.initButtons()

    def initButtons(self):
        startButton = Button(self.canvas,text="start",command=self.buttonStartPressed)
        self.startButton=startButton


    def keyPressed(self,event):
        if self.isGameOver:return
        if (event.char=="s"):
            print "key pressed"
            self.Bullets.append(self.player.shoot())
        elif(event.char=="r"):
            self.init()
        self.redrawAll()

        
    def mouseMotion(self,event):
        x =event.x_root
        y =event.y_root
        # keep the hamster in the window
        if x>0 and x < self.width and y>0 and y<self.height:
            self.player.xPosition=event.x_root
            self.player.yPosition=event.y_root
        if x<0:
            self.player.xPosition=0
        if x>self.width:
            self.player.xPosition=self.width
        if y<0:
            self.player.yPosition=0
        if y>self.height:
            self.player.yPosition=self.height-self.player.radius*2
            
    def buttonStartPressed(self):
        self.screen="play"
        self.level =1
        #self.redrawAll(self.canvas)

    def redrawAll(self):
        self.canvas.delete(ALL)
       # if not self.isGameOver and self.screen=="play":
        if not self.isGameOver:
            if self.screen=="play":
                # draw the warning funciton of the 
                self.playerDrawFlash(self.canvas)
                self.player.drawPlayer(self.canvas)
                self.player.drawLife(self.canvas,self.width,self.height)
               # draw enemies
                for enemy in self.Enemies:
                    enemy.drawEnemy(self.canvas)
                # draw 
                for bullet in self.Bullets:
                    bullet.drawBullet(self.canvas)
            elif self.screen == "Menu":
                print "drawMenu", self.screen,self.player
                self.drawMenu(self.canvas)
            elif self.screen == "EndLevel":
                self.level+=1
                self.drawEndLevel(self.canvas)

    
       
    def drawMenu(self,canvas):
        imageFile=PhotoImage(file="images/hamster.gif")
        cellSize = self.width/7
        #canvas.create_image(cellSize,cellSize,image=imageFile)
        canvas.create_rectangle(0,0,self.width,self.height,fill="pink")
        msg = "start game"
        #canvas.create_text(cellSize*6,cellSize,text=msg)
        b1=self.startButton
        #canvas.create_window(50,200,window=b1)
        b1.place(x=50,y=200)


    def playerDrawFlash(self,canvas):
        if self.warningCounter>0:
            self.warningCounter-=1
            (x,y)=self.player.xPosition,self.player.yPosition
            r=10*self.player.radius
           # canvas.create_rectangle(100,100,200,200, fill = "red")
            canvas.create_oval(x-r,y-r,x+r,y+r,fill="red")
            


    def timerFired(self):
        if (not self.isGameOver):
            if self.screen== "play":
                self.moveEnemies()
                self.moveBullets()
                self.addEnemies()
                self.meetEnemies()
                self.killEnemies()
                #self.checkLevel()
                #self.eatBounus()

                self.addWeapen()

                #sefl.meetEnemies()
                # if the enemy got outside the screen
                self.cleanFrame()

                self.redrawAll()
                self.player.score+=10
            # elif self.screen=="Menu":
            #     # in the beginning Menu, we play start music
            #    # self.playStartMusic()

            #     #self.redrawAll()
            #     pass
            # elif self.screen=="EndLevel":
            #     # self.playLevelMusic()
            #     #self.redrawAll()
            #     pass
    

    def playStartMusic(self):
        CHUNK = 1024

        print "AAA"
        wf = wave.open("cello.wav", 'rb')

        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

        data = wf.readframes(CHUNK)

        while data != '':
            stream.write(data)
            data = wf.readframes(CHUNK)

        stream.stop_stream()
        stream.close()

        p.terminate()
    def addWeapen(self):
        width=self.width
        height=self.height
        (x,y)=(width,random.randrange(0,height-1,2*self.player.radius))




    def checkLevelChange(self):
        if self.player.score > self.levelScoreBound*self.level*1.1:
            self.level+=1


    def cleanFrame(self):
        # delete all the enemies that are outside the screen
        newEnemies=[]

        if len(self.Enemies)!=0:
            for enemy in self.Enemies:
                if self.isInScreen(enemy.xPosition,enemy.yPosition):
                    newEnemies.append(enemy)
        self.Enemies=newEnemies
        newBullets=[]
        
        if len(self.Bullets)!=0:
            for bullet in self.Bullets:
                if self.isInScreen(enemy.xPosition,enemy.yPosition):
                    newBullets.append(bullet)
        self.Bullets=newBullets






    def isInScreen(self,x,y):
        return (x>=0 and x<=self.width and y>=0 and y<=self.height)


    def killEnemies(self):
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
                    self.increaseScore(b,e)
                    listEnemies=copy.copy(self.Enemies)
                    break            

    def increaseScore(self,bullet,enemy):
        if isinstance(enemy,e.FlyBird):
            self.player.score+= 10 # every killed bird will increase 10
        elif isinstance(enemy,e.JumpSheep):
            self.player.score+= 20




    def moveEnemies(self):
        for enemy in self.Enemies:
            if isinstance (enemy,e.FlyBird):
                enemy.moveEnemy(self.canvas,self.player.xPosition,self.player.yPosition)
            elif isinstance (enemy,e.JumpSheep):
               # print enemy.xPosition,enemy.yPosition
                enemy.moveEnemy(self.canvas,self.width,self.height)

    def moveBullets(self):
        for b in self.Bullets:
            b.moveBullet(self.canvas)

    def addEnemies(self):
        # every time according to the counter we add enemies
        width=self.width
        height=self.height
        (x,y)=(width,random.randrange(0,height-1,2*self.player.radius))

        self.EnemyPresentCounter+=1
        # ever 10 times we need to add bird enemy
        if self.EnemyPresentCounter%self.EnemyBirdCyclceCoeff==0:
            if len(self.Enemies)< self.Dificulty:
                self.Enemies.append(e.FlyBird(x,y))

        # ever 5 times we need to add sheep which will jump every where
        if self.EnemyPresentCounter%self.EnemySheepCycleCoeff==0:
            if len(self.Enemies)< self.Dificulty:
                self.Enemies.append(e.JumpSheep(0,height))

    # check we have ever meet the enemy
    def meetEnemies(self):
        for e in self.Enemies:
            if self.player.isCollision(e):
                self.warningCounter=3
                self.minusLife()
                break


    def minusLife(self):
        self.player.life-=1
        if self.player.life<=0:
            self.isGameOver=True







game=Game()
game.run(1920,1200)