from Tkinter import *
import random
import copy
import math
#import pygame
#import track as track
import Item as item
import player as p
import enmies as e
import weapen as w
#import bounus as b
import wavePlayerloop as wavep
import background as bc

import threading
import wave
import time
import sys
import pyaudio

import tkMessageBox
import tkSimpleDialog

import urllib
import os

#import ter as tp
#  the first version of working game,
# withOut Music Working but file read and modify working
# to play music we have to keep all the thingsa tag we cannot call it every time
# without any 
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
        self.timerFiredDelay = 100 # milliseconds
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
        self.backGroundImage=PhotoImage(file="images/menu.gif")
        self.endBackGroundImage=PhotoImage(file="images/end.gif")
        self.endWinBackGroundImage=PhotoImage(file="images/win.gif")
        self.guidePage = PhotoImage(file="images/guide.gif")
        self.level2BackGroundImage=PhotoImage(file="images/level2.gif")
        self.level1BackGroundImage =PhotoImage(file="images/level1.gif")
        self.level3BackGroundImage =PhotoImage(file="images/level3.gif")
        self.difficultyChoosePage   =PhotoImage(file="images/difficulty.gif")
        # decide when to 
        self.EnemyCycleRound=10
        self.EnemyBirdCyclceCoeff=1
        self.EnemySheepCycleCoeff=2


        self.EnemyPresentCounter=0
        # decide the diciculty of the game, to gurantee 5 enemies on the screen
        self.Difficulty       = 4
        
        # the barrier on the out side  to be continued
        self.topBoxes   = []
        self.bottomBoxes= []

        self.Enemies=[]
        self.Bullets=[]

        self.initLevel2Boss()
        
        # the list of the Weapens that may appear
        self.otherWeapens=[]
        self.weapenLife=0
        # new weapen only have 10 bullets
        self.weapenLife  =10 

        self.level =1 # test the level2
        self.screen = "Menu"
        self.isGameOver=False
        self.initScoreRecord()
        
        self.menuMusic=wavep.WavePlayerLoop("/Users/Sirrie/Dropbox/project/media/start.wav")
        self.level1Music=wavep.WavePlayerLoop("/Users/Sirrie/Dropbox/project/media/level1.wav")
        # self.level2Music=wavep.WavePlayerLoop("/Users/Sirrie/Dropbox/project/media/level2.wav")
        # self.level3Music=wavep.WavePlayerLoop("/Users/Sirrie/Dropbox/project/media/level3.wav")
        # self.gameOverMusic=wavep.WavePlayerLoop("/Users/Sirrie/Dropbox/project/media/gameOver.wav")


        self.isMenuMusicOn=False
        self.isLevel1MusicOn=False
        self.isLevel2MusicOn=False
        self.isLevel3MusicOn=False
        self.isGameOverMusicOn=False

        self.warningCounter=3
       # self.initGameOverPage()
        # Open the file and read from the file

##------------the part for object tracking ------------------------------##
        # self.track = tp.TrackObject()
        # self.track.init()

    
   
    def readFile(self,filename, mode="rt"):
        # rt stands for "read text"
        fin = contents = None
        try:
            fin = open(filename, mode)
            contents = fin.read()
        finally:
            if (fin != None): fin.close()
        return contents

    def writeFile(self,filename, contents, mode="wt"):
        # wt stands for "write text"
        fout = None
        try:
            fout = open(filename, mode)
            fout.write(contents)
        finally:
            if (fout != None): fout.close()
        return True


    def initScoreRecord(self):
        print "try to read "
        try:
            s = self.readFile("Files/joke.txt")

            print s
            self.presentScore = eval(self.readFile("Files/joke.txt"))
            sorted(self.presentScore)
            self.HigestScore=self.presentScore[0]

        except:
            print "The file does not exist yet (as we hoped!)"
        


    def initLevel2Boss(self):
        # init the bossbullets
        self.BossBullets=[]
        
        self.addPreviousPosition=True
        # init the total time that boss begane to active
        self.bossTimeCounter=0
        # init the count for boss to wait before moving 
        self.bossMoveStartCount=120
        self.taskTimeCount=0
        self.owlShootCount=0
        self.bossShootStartCount=100
        # record the previous locations of the player
        self.previousLocation=[]
        self.bossTasks=['wait','move','BulletShoot','Lasershoot']
        self.bossPresenTask="wait"      



    def mousePressed(self,event):
        (x,y)=(event.x,event.y)
      
        if self.screen == "Menu":
            # press the start buttton
            if x>400 and x<600 and y>300 and y<350:
                self.screen="Play"
                self.playClickMusic()
            elif x<200 and y>400:
                self.screen="Guide"
            elif x>200 and y>400:
                self.screen="Difficulty"
        elif self.screen=="Difficulty":
            if x>300 and x<600 and y<300:

                self.Difficulty = 2
                print self.Difficulty,"click"
            elif x<300 and y>300 and y<600:
                self.Difficulty = 3 
                print self.Difficulty,"click"
            elif x>600 and y>300 and y<600:
                self.Difficulty = 4
                print self.Difficulty,"click"
            else:
                self.screen="Menu"
        self.redrawAll()


    def keyPressed(self,event):
        if not self.isGameOver:
            if (event.char=="s"):
                print "key pressed",self.weapenLife
                if self.weapenLife>0:
                    self.weapenLife-=1
                # after used up the specail weapen, we change back to default
                # weapen
                if self.weapenLife<=0:
                    self.player.weapen="spit"
                print self.player.weapen,self.player.shoot()
                self.Bullets.append(self.player.shoot())
                self.playShootMusic()

                #self.shootByBoss()
            elif(event.char == "k"):
                self.screen= "Play"
        # press r to restart the game
        if(event.char=="r"):
            self.init()
            self.screen="Menu"
        elif(event.char=="t"):
            # AskString Box
            root3=Tk()
            self.inputName=tkSimpleDialog.askstring("Score Record","enter your name")
            print self.inputName,self.player.score
            contents = [(89,'BOb'),(90,'Teddy'),(80,'Wenny'),(self.player.score,self.inputName)]
            self.writeFile("Files/joke.txt", repr(contents))
            try:
                s = self.readFile("Files/joke.txt")
                print s,eval(s)
            except:
                print "The file does not exist yet (which would be strange now!)"

        self.redrawAll()

        
    def mouseMotion(self,event):
        x =event.x_root
        y =event.y_root
        # chech whether it is beyond the obstacles
        forced = self.checkBoxesObstacle(x,y)

        # keep the hamster in the window
        if forced == False:
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
        
        

    def checkBoxesObstacle(self,x,y):
        # bound the position of the box
        for box in self.topBoxes:
            if x>box.centerX and x <box.centerX+box.VelocityX and y<box.length+self.height/9:
                self.player.yPosition=box.centerY + self.height/9
                return True
        for box in self.bottomBoxes:
            if x>box.centerX and x <box.centerX+box.VelocityX and y>-box.length+self.height:
                self.player.yPosition=-2*box.centerY + self.height
                return True

        return False

    def redrawAll(self):
        self.canvas.delete(ALL)
        if not self.isGameOver:
            if self.screen=="Play":
                self.stopMenuMusic()
                if self.level==1:
                    self.drawLevel1(self.canvas)
                    self.playLevel1Music()
                elif self.level==2:
                    
                    self.drawLevel2(self.canvas)
                elif self.level==3:
                    
                    self.drawLevel3(self.canvas)

            elif self.screen == "Menu":
                #print "drawMenu", self.screen,self.player
                self.drawMenu(self.canvas)
                self.playMenuMusic()
                self.isMenuMusicOn=True
            elif self.screen == "Guide":
                #self.stopMenuMusic()
                self.drawGuide(self.canvas)
            elif self.screen == "Difficulty":
                self.drawChooseDifficulty(self.canvas)

            
        elif self.screen=="Win":
            self.drawWinScreen(self.canvas)
        else:

            self.drawGameOver(self.canvas)
       # self.stopLevel3Music()
       

    def drawChooseDifficulty(self,canvas):
        canvas.create_image(500,220,image=self.difficultyChoosePage)


    def drawGuide(self,canvas):
        canvas.create_image(500,220,image=self.guidePage)


    def playMenuMusic(self):
        if not self.isMenuMusicOn:
            self.menuMusic.play()

       
    def stopMenuMusic(self):
        self.menuMusic.stop()
        self.isMenuMusicOn=False

    def playLevel1Music(self):
        if not self.isLevel1MusicOn:
            self.level1Music.play()
            self.isLevel1MusicOn=True

    def drawWinScreen(self,canvas):
        canvas.create_image(500,220,image=self.endWinBackGroundImage)

    # for level1 just do 
    def drawLevel1(self,canvas):
         # draw the warning funciton of the 
        self.playerDrawFlash(canvas)
        self.player.drawPlayer(canvas)
        self.player.drawLife(canvas,self.width,self.height)
        self.player.drawScore(canvas,self.width,self.height)
       # draw enemies
        for enemy in self.Enemies:
            enemy.drawEnemy(canvas)
        # draw bullets
        for bullet in self.Bullets:
            bullet.drawBullet(canvas)

        self.drawLevel(canvas)

    def drawLevel2(self,canvas):
        canvas.create_image(500,200,image=self.level2BackGroundImage)
        # in level2 we have a big wol enemy and then we can fight with it
        self.player.drawPlayer(canvas)
        self.player.drawLife(canvas,self.width,self.height)
        self.player.drawScore(canvas,self.width,self.height)
        # draw the level of the game
        self.drawLevel(canvas)
         # draw enemies
        for enemy in self.Enemies:
            enemy.drawEnemy(canvas)
            self.drawEnemyLife(enemy.lifeLong)
        # draw bullet from the player
        for bullet in self.Bullets:
            bullet.drawBullet(canvas)
        # draw bullet from boss
        for bullet in self.BossBullets:
            bullet.drawBullet(canvas)

        # draw the life length of the boss
        self.drawBossLife(canvas)


    def drawLevel3(self,canvas):
         # draw the background of level3
        canvas.create_image(500,200,image=self.level3BackGroundImage)
       # draw enemies
        for enemy in self.Enemies:
            enemy.drawEnemy(canvas)
        # draw bullets
        for bullet in self.Bullets:
            bullet.drawBullet(canvas)
        # draw the boxes on the top 
        for box in self.topBoxes:
            box.drawBackGround(self.canvas)

        for box in self.bottomBoxes:
            box.drawBackGround(self.canvas,self.height)
        
        # for the bonus weapens we can eat it and change 
        for weapen in self.otherWeapens:
        #   print weapen.xPosition,weapen.yPosition
        
            weapen.drawBullet(self.canvas)


        self.drawLevel(canvas)
        self.playerDrawFlash(canvas)
        self.player.drawPlayer(canvas)
        self.player.drawLife(canvas,self.width,self.height)
        self.player.drawScore(canvas,self.width,self.height)




    # draw the life of the present boss
    def drawBossLife(self,lifeLong):
        canvas=self.canvas
        width =self.width
        height=self.height
        canvas.create_text(width*6.0/7.0,height/9,font="Purisa",text="Boss Life: "+str(lifeLong))

    
    def drawLevel(self,canvas):
        msg=self.level
        canvas.create_text(self.width/2,self.height/9,text="the Level is "+str(msg))

    def drawGameOver(self,canvas):
        canvas.create_image(500,220,image=self.endBackGroundImage)

    def drawMenu(self,canvas):
        #imageFile=PhotoImage(file="images/hamster.gif")
        
        canvas.create_image(500,220,image=self.backGroundImage)
        #canvas.create_rectangle(0,0,self.width,self.height,fill="pink")
        
        


    def playerDrawFlash(self,canvas):
        if self.warningCounter>0:
            self.warningCounter-=1
            (x,y)=self.player.xPosition,self.player.yPosition
            r=10*self.player.radius
           # canvas.create_rectangle(100,100,200,200, fill = "red")
            canvas.create_oval(x-r,y-r,x+r,y+r,fill="red")
            


    def timerFired(self):
        # get the track information from the OpenCV input
        # foo = self.track.getImage(self.track.cap)
        # self.player.xPosition=foo[0]
        # self.player.yPosition=foo[1]
        
        
        if (not self.isGameOver):

            if self.screen== "Play":
                if self.level==1:
                    self.timerFiredLevel1()
                elif self.level==2:
                    self.timerFiredLevel2()
                elif self.level==3:
                    self.timerFiredLevel3()

             




    def timerFiredLevel2(self):
        self.addPreviousPosition=not self.addPreviousPosition
        if self.Enemies == []:
            self.Enemies.append(e.Owl(self.width*6.0/7.0,self.height/2))
           # self.Enemies= e.Owl(self.width*6.0/7.0,self.height/2)
        

        if self.bossTimeCounter%self.bossMoveStartCount==0:
            #start a task choose the task type
            taskNumber=random.randint(2,len(self.bossTasks))-1
            self.bossPresentTask=self.bossTasks[taskNumber]
            self.BossBullets=[]
        self.bossTimeCounter+=2

        if self.addPreviousPosition:
            self.previousLocation.append((self.player.xPosition,self.player.yPosition
                ))
        self.bossPresentTask ="Lasershoot"

        task=self.bossPresentTask
        #task="Lasershoot"
        # every time change the task we need to clean the frame
        self.cleanFrame()
        if task=="move":
            #print "come to this"
            self.moveBoss()
        elif task=="BulletShoot":
            
            # clean the bullets
            #
            self.shootByBoss()
        elif task=="Lasershoot":
            
            if self.bossTimeCounter% 10==0:
                self.laserByBoss()

        else:
            pass

        # everytime check the whether we will meet the 
        self.meetEnemies()
        # if there are bullets move bullets
        self.moveBullets()
        # if boss will shoot at the player
        self.moveBulletsByBoss()
        # check whether we meet the bullets, if we meet the bullets we need to minus life of the player
        self.meetBulletByBoss()
        # kill the boss then it will update the life length of the boss
        self.killBoss()
        # check whether we can finish this level
       



    def laserByBoss(self):
        targetLocationX,targetLocationY=self.previousLocation.pop(0)
        for enemy in self.Enemies:
            self.BossBullets=[]
            self.BossBullets.append(enemy.shootLaser(targetLocationX,targetLocationY))



    def killBoss(self):
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
                if ((abs(e.xPosition-x)<e.radius and abs(e.yPosition-y)<e.radius)):
                    self.Bullets.remove(b)
                    e.dcreaseLife(self.player.weapen)
                    self.increaseScore(b,e)
                    # if we killed the boss we will win
                    if e.lifeLong==0:
                        #self.screen="win"
                        #self.isGameOver=True
                        # if we kille the boss we will go to level3
                        self.level+=1

                    listEnemies=copy.copy(self.Enemies)
                    break  



       # self.checkLevel()
    def meetBulletByBoss(self):
        for bullet in self.BossBullets:
            if isinstance(bullet,w.Bullet):
                distance = math.sqrt((bullet.xPosition-self.player.xPosition)**2+(bullet.yPosition-self.player.yPosition)**2)
                if distance<self.player.radius:
                    self.minusLife()
            elif isinstance(bullet,w.Laser):
               # print self.player.xPosition,self.player.yPosition,bullet.targetX,bullet.targetY,"this is the position"
                distance= self.distanceToLine(bullet.startX,bullet.startY,bullet.targetX,bullet.targetY)
               # print distance, "the distance of the player and the laser"
                if distance <=10:
                    self.minusLife()


    def distanceToLine(self,sx,sy,tx,ty):
        distance=500
        
        x,y=self.player.xPosition,self.player.yPosition
        startX=min(sx,tx)
        startY=min(sy,ty)
        endX  =max(sx,tx)
        endY  =max(sy,ty)

        if x>=startX-10 and x<=endX+10 and y>=startY-10 and y<=endY+10:
            a=ty-sy
            b=sx-tx
            c=sx*(sy-ty)+sy*(tx-sx)
            denominator=math.sqrt(a**2+b**2)
            x0=self.player.xPosition
            y0=self.player.yPosition
            distance=abs(a*x0+b*y0+c)*1.0/denominator
        return distance


   # generate bullets by Boss
    def shootByBoss(self):
        print "here"
        # every 6 round we add a bullet
        self.owlShootCount+=1
        if self.owlShootCount == 6:
            self.owlShootCount=0
            for enemy in self.Enemies:
                bullettemp=enemy.shootBullet()
                self.BossBullets.append(bullettemp)
                print self.BossBullets
            
    # move all the bullets shooted by Boss
    def moveBulletsByBoss(self):
        for bb in self.BossBullets:
            print "moving b"
            if  isinstance(bb, w.Bullet):
                bb.moveBullet(self.player.xPosition,self.player.yPosition)
            


    def moveBoss(self):
        # first update the velocity
        enemy = self.Enemies.pop()
        # owl only move beteewn the center and the outside
        if enemy.xPosition<=self.width/2 or enemy.xPosition>=self.width-enemy.radius:
            #self.Enemies(0).Velocityx=-self.Enemies.Velocityx
            enemy.Velocityx=-enemy.Velocityx
            enemy.xPosition==self.width/2+5
        self.Enemies.append(enemy)
      #  print enemy.xPosition,enemy.Velocityx,"time counter"
        for enemy in self.Enemies:
            enemy.moveEnemy()




    def timerFiredLevel1(self):
        self.moveEnemies()
        self.moveBullets()
        self.addEnemies()
        self.meetEnemies()
        self.killEnemies()
        self.checkLevel()
        #self.eatBounus()
        self.addWeapen()
        # if the enemy got outside the screen
        self.cleanFrame()

        self.redrawAll()
        #self.player.score+=10

    def timerFiredLevel3(self):
        self.moveEnemies()
        self.moveBullets()
        self.addEnemies()
        self.meetEnemies()
        self.killEnemies()
        self.checkLevel()
        #self.eatBounus()
        self.addWeapen()
        self.changeWeapen()
        # add boxes to the top of the screen
        self.addBoxesObstacle()
        self.moveBoxesObstacle()
        # everytime we should guanrantee that we will 
    



        # if the enemy got outside the screen
        self.cleanFrame()

        self.redrawAll()


    # play click music
    def playClickMusic(self):
        CHUNK = 1024
        wf = wave.open("media/click.wav", 'rb')
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

    def playShootMusic(self):
            CHUNK = 1024
            wf = wave.open("media/shoot.wav", 'rb')
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
    #check the level updated for this level 
    def checkLevel(self):
        if self.level==1:
            if self.player.score>50:
                self.level=2
                self.cleanLevel()


    def cleanLevel(self):
        self.Enemies=[]
        self.Bullets=[]
      
     # add weapen to the game that we can  eat and change the weapen  
    def addWeapen(self):
        width=self.width
        height=self.height
        (x,y)=(width/2,random.randrange(0,height-1,2*self.player.radius))
        # it there is no weapen to change we need to add one new bounus weapen
        # we have 3 chances to change the weapen if we want
        print "present player weapen status",self.player.weapen
        if len(self.otherWeapens)<=3 and self.player.weapen=="spit":
            randomXplace=random.randint(1,self.width)
            randomYplace=random.randint(1,self.height)
            self.otherWeapens.append(w.RedBerry(randomXplace,randomYplace))
    # each time we change the Weapen if the player meet the weapen
    def changeWeapen(self):
        newOtherWeapens=[]
        for bounusWeapen in self.otherWeapens:
            if self.checkMeetWeapen(bounusWeapen):
                self.weapenNameChange(bounusWeapen)
                self.weapenLife=10
               
            else:
                # those weapen didn't change we will add to new list
                newOtherWeapens.append(bounusWeapen)
        self.otherWeapens=newOtherWeapens


    # check whether we have eaten the weapen
    def checkMeetWeapen(self,bounusWeapen):
        x,y=self.player.xPosition,self.player.yPosition
       
        distance=math.sqrt((bounusWeapen.xPosition-x)**2+(bounusWeapen.yPosition-y)**2)
        if distance<40:
            return True
        return False

    def weapenNameChange(self,bounusWeapen):
        if isinstance(bounusWeapen,w.RedBerry):
            self.player.weapen="redBerry"



    def addBoxesObstacle(self):
        randomHight=random.randint(10,60)
        width    = self.width
        boxHeight= self.height/9

        self.topBoxes.append(bc.TopBoxes(width,boxHeight,randomHight))
        self.bottomBoxes.append(bc.BottomBoxes(width,boxHeight,randomHight))
    
    def moveBoxesObstacle(self):
        for box in self.topBoxes:
            box.moveBackGround()
        for box in self.bottomBoxes:
            box.moveBackGround()


    # every time after the leve update we clean the whole frame
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

        newTopBoxes = []
        if len(self.topBoxes)!=0:
            for box in self.topBoxes:
               if self.isInScreen(box.xPosition,box.yPosition):
                newTopBoxes.append(box)


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
                # if the bullet meet the enemy, we will increase 
                # we will increase the score of the player
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
            if len(self.Enemies)< self.Difficulty:
                self.Enemies.append(e.FlyBird(x,y))

        # ever 5 times we need to add sheep which will jump every where
        if self.EnemyPresentCounter%self.EnemySheepCycleCoeff==0:
            if len(self.Enemies)< self.Difficulty:
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
game.run(900,500)
