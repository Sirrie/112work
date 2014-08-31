from Tkinter import *
import random
import copy
import math
import Item as item
import player as p
import enmies as e
import weapen as w
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

import ter as tp

# withOut Music Working

# add the function of choosing moseMotion or dot tracking
# the music functions are turned off
# with the function for 

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
        self.initImage()
        self.initMusic()
        # decide when to  add an enemy 
        self.EnemyCycleRound=10
        self.EnemyBirdCyclceCoeff=1
        self.EnemySheepCycleCoeff=2
        self.EnemyPresentCounter=0
        # in level 3 to count the shift
        self.timeCounter=0
        # decide the difficulty of the game, default is to gurantee 
        # 4 enemies on the 
        # screen 
        self.Difficulty       = 4
        # the barrier on the out side to be continued
        self.topBoxes   = []
        self.bottomBoxes= []
        # the enemis in the screeen
        self.Enemies=[]
        # bullets shooted by the player 
        self.Bullets=[]
        self.initLevel2Boss()
        # the list of the Weapens that may appear
        self.otherWeapens=[]
        self.weapenLife=0
        self.level =1# inital level
        self.screen = "Menu"
        self.isGameOver=False
        self.model = "MouseMotion"
        # initial the music flag for whether it is on or not
        self.isMenuMusicOn=False
        self.isLevel1MusicOn=False
        self.isLevel2MusicOn=False
        self.isLevel3MusicOn=False
        self.isGameOverMusicOn=False

        self.warningCounter=3
    


##------------the part for object tracking ------------------------------##
        self.track = tp.TrackObject()
        #we should not call self.track.init() here, we need to init once it 
        # is chosen by another program

        # read from the file and check the highest score records
        self.initScoreRecord()
    def initImage(self):
        # load those images
        
        self.backGroundImage=PhotoImage(file="images/menu1.gif")
        self.endBackGroundImage=PhotoImage(file="images/end.gif")
        self.endWinBackGroundImage=PhotoImage(file="images/win.gif")
        self.guidePage = PhotoImage(file="images/guide.gif")
        self.level2BackGroundImage=PhotoImage(file="images/level2.gif")
        self.level1BackGroundImage =PhotoImage(file="images/level1_1.gif")
        self.level3BackGroundImage =PhotoImage(file="images/level3.gif")
        self.difficultyChoosePage   =PhotoImage(file="images/difficulty.gif")
        self.chooseModelBackGroundImage=PhotoImage(file="images/choose.gif")
        self.scoreBoardBackGround     = PhotoImage(file="images/score.gif")
    def initMusic(self):
         # initial the music part
        self.menuMusic=wavep.WavePlayerLoop("/Users/Sirrie/Dropbox/project/media/start.wav")
        self.level1Music=wavep.WavePlayerLoop("/Users/Sirrie/Dropbox/project/media/level1.wav")
        self.level2Music=wavep.WavePlayerLoop("/Users/Sirrie/Dropbox/project/media/level2.wav")
        self.level3Music=wavep.WavePlayerLoop("/Users/Sirrie/Dropbox/project/media/level3.wav")
        self.gameOverMusic=wavep.WavePlayerLoop("/Users/Sirrie/Dropbox/project/media/gameOver.wav")

   # code from David Kosbie's lecture note 
    def readFile(self,filename, mode="rt"):
        # rt stands for "read text"
        fin = contents = None
        try:
            fin = open(filename, mode)
            contents = fin.read()
        finally:
            if (fin != None): fin.close()
        return contents
    # code from David Kosbie's lecture note
    def writeFile(self,filename, contents, mode="wt"):
        # wt stands for "write text"
        fout = None
        try:
            fout = open(filename, mode)
            fout.write(contents)
        finally:
            if (fout != None): fout.close()
        return True

    # read from file where we store all the records in the file
    def initScoreRecord(self):
        print "try to read "
        try:
            s = self.readFile("Files/scoreRecord.txt")
            self.presentScore = (eval(s))
            self.presentScore=sorted(self.presentScore)
            (self.highestScore,self.heightScoreName)=self.presentScore[-1]
            print self.presentScore[-1],"the higestScore"
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
        leftBound=400
        rightBound=600
        centerBottom=300
        centerUpper=350
        yBound=600
        if self.screen == "Menu":
            # press the start buttton
            if x>leftBound and x<rightBound and y>centerBottom and y<centerUpper:
               # self.screen="Play"
                print "click to choose"
                self.screen="ChooseModel"
                self.playClickMusic()
            elif x<leftBound and y>centerUpper:
                self.screen="Guide"
            elif x>rightBound and y>centerUpper:
                self.screen="Difficulty"
        elif self.screen=="ChooseModel":
            if x<leftBound:
                self.screen="Play"
                self.model ="MouseMotion"
            else:
                self.screen="Play"
                self.model ="DotTracking"
                self.track.init()
        elif self.screen == "Guide":
            if x>0 and x<self.width and y>0 and y<self.height:
                self.screen="Menu"
        elif self.screen=="Difficulty":
            if  y<centerBottom:
                enemyNumber=2
                self.Difficulty = enemyNumber 
            elif x<leftBound and y>centerBottom and y<yBound:
                enemyNumber=3
                self.Difficulty = enemyNumber
            elif x>rightBound and y>centerBottom and y<yBound:
                enemyNumber=4
                self.Difficulty = enemyNumber
            self.screen="Menu"
            print self.Difficulty
        if self.isGameOver:
            if x>rightBound and y>centerBottom:
                self.screen="HighScoreBoard"
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
                self.Bullets.append(self.player.shoot())
                self.playShootMusic()
            elif(event.char == "k"):
                self.screen= "Play"
        # press r to restart the game
        if(event.char=="r"):
            self.init()
            self.stopAllMusic()
            self.screen="Menu"
            self.playMenuMusic()
            self.isGameOver=False
        elif(event.char=="t"):
            # AskString Box
            root3=Tk()
            self.inputName=tkSimpleDialog.askstring("Score Record","New High score please enter your name")


        self.redrawAll()
    # stop all threads of music
    def stopAllMusic(self):
        try:
            self.stopMenuMusic()
        except:
            print "fail menu"
        try:
            self.stopLevel1Music()
        except:
            print "faile level1"
        try:
            self.stopLevel2Music()
        except:
            print "faile level2"
        try:
            self.stopLevel3Music()
        except:
            print "fail level3"
            
        
    def mouseMotion(self,event):
        if self.model=="MouseMotion":
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
                    self.stopLevel1Music()
                    self.drawLevel2(self.canvas)
                    self.playLevel2Music()
                elif self.level==3:
                    self.stopLevel2Music()
                    self.drawLevel3(self.canvas)
                    self.playLevel3Music()
            # every time before we goto another level we just 
            elif self.screen == "Menu":
                self.drawMenu(self.canvas)
                self.playMenuMusic()
                self.isMenuMusicOn=True
            elif self.screen == "Guide":
               # self.stopMenuMusic()
                self.drawGuide(self.canvas)
            elif self.screen == "Difficulty":
                self.drawChooseDifficulty(self.canvas)
            elif self.screen == "ChooseModel":
                self.drawChooseModel(self.canvas)          
        elif self.screen=="Win":
            self.stopAllMusic()
            self.drawWinScreen(self.canvas)
            self.playGameOverMusic()
        elif self.screen=="HighScoreBoard":
            self.drawHighScoreBoard(self.canvas)
        else:

            self.stopAllMusic()
            self.drawGameOver(self.canvas)
            self.playGameOverMusic()

    

####-------------------this part is realted to playing music --------------####
    def playMenuMusic(self):
        if not self.isMenuMusicOn:
            self.menuMusic.play()
            self.isMenuMusicOn=True
       
    def stopMenuMusic(self):
        self.menuMusic.stop()
        self.isMenuMusicOn=False

    def playLevel1Music(self):
        if not self.isLevel1MusicOn:
            self.level1Music.play()
            self.isLevel1MusicOn=True

       
    def stopLevel1Music(self):
        self.level1Music.stop()
        self.isLevel1MusicOn=False
        

    def playLevel2Music(self):
        if not self.isLevel2MusicOn:
            self.level2Music.play()
            self.isLevel2MusicOn=True
       
    def stopLevel2Music(self):
        self.level2Music.stop()
        self.isLevel2MusicOn=False

    def playLevel3Music(self):
        if not self.isLevel3MusicOn:
            self.level3Music.play()
            self.isLevel3MusicOn=True
       
    def stopLevel3Music(self):
        self.level3Music.stop()
        self.isLevel3MusicOn=False


    def playGameOverMusic(self):
        if not self.isGameOverMusicOn:
            self.gameOverMusic.play()
            self.isGameOverMusicOn=True
       
    def stopGameOverMusic(self):
        self.gameOverMusic.stop()
        self.isGameOverMusicOn=False
####----------------this par relate with drawing ------------------###
    def drawHighScoreBoard(self,canvas):
        try:
            s = self.readFile("Files/scoreRecord.txt")
          
            self.presentScore = (eval(s))
            self.presentScore=sorted(self.presentScore)
            self.presentScore.reverse()
        except:
            print "The file does not exist yet"
        canvas.create_image(450,250,image=self.scoreBoardBackGround)
        wCellNumber=6
        hCellNumber=17
        widthCellSize= self.width/wCellNumber
        hightCellSize= self.height/hCellNumber
        topTen=10
        if len(self.presentScore)<topTen:
            lengthLimit= len(self.presentScore)
        else:
            lengthLimit= topTen

        canvas.create_text(widthCellSize*(2+1),hightCellSize,
            text="HighScoreBoard",font="Helvetica 30 bold",fill="snow")
        canvas.create_text(widthCellSize*2,hightCellSize*2,text="Name",
            font ="Helvetica 26 bold",fill="snow")
        canvas.create_text(widthCellSize*2*2,hightCellSize*2,text="Score",
            font="Hwlvetica 26 bold",fill="snow")




        for index in xrange(lengthLimit):
            (score,name)=self.presentScore[index]
            canvas.create_text(widthCellSize*2,
                hightCellSize*(index+wCellNumber),text=name,
                    font="Helvetica 20 bold",fill="snow")
            canvas.create_text(widthCellSize*2*2,
                hightCellSize*(index+wCellNumber),text=score,
                    font="Helvetica 20 bold",fill="snow")

    # draw the choose model page 
    def drawChooseModel(self,canvas):
        canvas.create_image(450,250,image=self.chooseModelBackGroundImage)
        canvas.create_text(450,250,text="Chose Mode",activefill="turquoise",
            fill="forest green",font="Helvetica 30 bold")
        canvas.create_text(200,350,text="MouseMotion",activefill="turquoise",
            fill="gold",font="Helvetica 30 bold")
        canvas.create_text(700,350,text="DotTracking",activefill="turquoise",
            fill="gold",font="Helvetica 30 bold")

    def drawChooseDifficulty(self,canvas):
        canvas.create_image(510,220,image=self.difficultyChoosePage)


    def drawGuide(self,canvas):
        canvas.create_image(510,250,image=self.guidePage)

    def drawWinScreen(self,canvas):
        canvas.create_image(500,220,image=self.endWinBackGroundImage)
    
    # for level1 just do 
    def drawLevel1(self,canvas):
        canvas.create_image(420,250,image=self.level1BackGroundImage)
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
            self.drawBossLife(canvas,enemy.lifeLong)
        # draw bullet from the player
        for bullet in self.Bullets:
            bullet.drawBullet(canvas)
        # draw bullet from boss
        for bullet in self.BossBullets:
            bullet.drawBullet(canvas)

        # draw the life length of the boss
        


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
            y=self.sinLine(box.centerX)
            box.drawBackGround(self.canvas,y)

        for box in self.bottomBoxes:
            box.drawBackGround(self.canvas,self.height)
        # for the bonus weapens we can eat it and change our weapen
        for weapen in self.otherWeapens:
            weapen.drawBullet(self.canvas)


        self.drawLevel(canvas)
        self.playerDrawFlash(canvas)
        self.player.drawPlayer(canvas)
        self.player.drawLife(canvas,self.width,self.height)
        self.player.drawScore(canvas,self.width,self.height)

    def sinLine(self,x):
        degree=1.0*(x+(self.timeCounter*3)%60)/self.width*2*math.pi*2
        gain=60
        y=math.sin(degree)*gain
    
        return y



    # draw the life of the present boss
    def drawBossLife(self,canvas,lifeLong):
        width =self.width
        height=self.height
        totalSize=9
        ratio=6.0/7.0
        canvas.create_text(width*ratio,height/totalSize,
            font="Purisa 30 bold",text="Boss Life: "+str(lifeLong))

    
    def drawLevel(self,canvas):
        msg=self.level
        totalSize=9
        canvas.create_text(self.width/2,self.height/totalSize,
            font="Purisa 30 bold",text="the Level is "+str(msg))

    def drawGameOver(self,canvas):
        canvas.create_image(500,220,image=self.endBackGroundImage)
        canvas.create_text(720,450,font="Helvetica 30 bold",activefill="SeaShell",fill="OrangeRed",text="Show HighScore")

    def drawMenu(self,canvas):
        canvas.create_image(450,260,image=self.backGroundImage)
        canvas.create_text(450,300,font="Helvetica 40 bold",activefill="Green",fill="Black",text="Start")
        canvas.create_text(100,450,font="Helvetica 30 bold",activefill="Green",fill="Black",text="Guide")
        canvas.create_text(800,450,font="Helvetica 30 bold",activefill="Green",fill="Black",text="Difficulty")

    def playerDrawFlash(self,canvas):
        if self.warningCounter>0:
            self.warningCounter-=1
            (x,y)=self.player.xPosition,self.player.yPosition
            r=10*self.player.radius
            canvas.create_oval(x-r,y-r,x+r,y+r,fill="red")
            
    def timerFired(self):
        # get the track information from the OpenCV input
        if self.model=="DotTracking":
            foo = self.track.getImage(self.track.cap)
            self.player.xPosition=foo[0]
            self.player.yPosition=foo[1]
        
        
        if (not self.isGameOver):
            if self.screen== "Play":
                if self.level==1:
                    self.timerFiredLevel1()
                elif self.level==2:
                    self.timerFiredLevel2()
                elif self.level==3:
                    self.timerFiredLevel3()
        else:
            # we have new high score 
            if self.player.score>self.highestScore:
                 # AskString Box
                root3=Tk()
                # take in the newest high score of the present player and then
                # save it to file
                self.inputName=tkSimpleDialog.askstring("Score Record","New High Score please enter your name")
                self.highestScore=self.player.score
                self.presentScore.append((self.player.score,self.inputName))
                contents=(repr(self.presentScore))
                self.writeFile("Files/scoreRecord.txt",contents)
                try:
                    s=self.readFile("Files/scoreRecord.txt")
                except:
                    print "the file doesn't exist"
                root3.destroy()

        self.redrawAll()

    def timerFiredLevel2(self):
        self.addPreviousPosition=not self.addPreviousPosition
        ratio = 6.0/7.0
        if self.Enemies == []:
            self.Enemies.append(e.Owl(self.width*ratio,self.height/2))
        if self.bossTimeCounter%self.bossMoveStartCount==0:
            #start a task choose the task type by randomlly generate something
            taskNumber=random.randint(2,len(self.bossTasks))-1
            self.bossPresentTask=self.bossTasks[taskNumber]
            self.BossBullets=[]
        self.bossTimeCounter+=2
        # everytime we add previous Position to the record therefore the boss
        # laser will track the player
        if self.addPreviousPosition:
            self.previousLocation.append((self.player.xPosition,
                    self.player.yPosition))
        task=self.bossPresentTask
        # every time change the task we need to clean the frame
        self.cleanFrame()
        if task=="move":
            # in this task we will
            self.moveBoss()
        elif task=="BulletShoot":
            
            # clean the bullets
            self.shootByBoss()
        elif task=="Lasershoot":
            countNumber=10
            # every ten times we generate a laser and keep it 
            if self.bossTimeCounter% countNumber==0:
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
                if ((abs(e.xPosition-x)<e.radius and 
                        abs(e.yPosition-y)<e.radius)):
                    self.Bullets.remove(b)
                    e.dcreaseLife(self.player.weapen)
                    self.increaseScore(b,e)
                    # if we killed the boss we will win
                    if e.lifeLong==0:
                        # if we kille the boss we will go to level3
                        self.level+=1

                    listEnemies=copy.copy(self.Enemies)
                    break  

    def meetBulletByBoss(self):
        distanceBound=10
        for bullet in self.BossBullets:
            if isinstance(bullet,w.Bullet):
                distance = math.sqrt((bullet.xPosition-self.player.xPosition)**2+(bullet.yPosition-self.player.yPosition)**2)
                if distance<self.player.radius:
                    self.minusLife()
            elif isinstance(bullet,w.Laser):
                distance= self.distanceToLine(bullet.startX,bullet.startY,bullet.targetX,bullet.targetY)
                if distance <=distanceBound:
                    self.minusLife()


    def distanceToLine(self,sx,sy,tx,ty):
        distance=500
        x,y=self.player.xPosition,self.player.yPosition
        startX=min(sx,tx)
        startY=min(sy,ty)
        endX  =max(sx,tx)
        endY  =max(sy,ty)
        # compute the distance from present player to the laser line
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
        shootTotalNumberByBoss=6
        # every 6 round we add a bullet
        self.owlShootCount+=1
        if self.owlShootCount == shootTotalNumberByBoss:
            self.owlShootCount=0
            for enemy in self.Enemies:
                bullettemp=enemy.shootBullet()
                self.BossBullets.append(bullettemp)
                print self.BossBullets
            
    # move all the bullets shooted by Boss
    def moveBulletsByBoss(self):
        for bb in self.BossBullets:
            if  isinstance(bb, w.Bullet):
                bb.moveBullet(self.player.xPosition,self.player.yPosition)
            


    def moveBoss(self):
        shifft=5
        # first update the velocity
        enemy = self.Enemies.pop()
        # owl only move beteewn the center and the outside
        if (enemy.xPosition<=self.width/2 or
                 enemy.xPosition>=self.width-enemy.radius):
            enemy.Velocityx=-enemy.Velocityx
            enemy.xPosition==self.width/2+shifft
        self.Enemies.append(enemy)

        for enemy in self.Enemies:
            enemy.moveEnemy()




    def timerFiredLevel1(self):
        self.moveEnemies()
        self.moveBullets()
        self.addEnemies()
        self.meetEnemies()
        self.killEnemies()
        self.checkLevel()
        self.addWeapen()
        # if the enemy got outside the screen
        self.cleanFrame()
        self.redrawAll()
        

    def timerFiredLevel3(self):
        self.timeCounter+=1
        self.moveEnemies()
        self.moveBullets()
        self.addEnemies()
        self.meetEnemies()
        self.killEnemies()
        self.checkLevel()
        self.addWeapen()
        self.changeWeapen()
        # add boxes to the top of the screen
        self.addBoxesObstacle()
        self.moveBoxesObstacle()
        # everytime we should guanrantee that we will 
        # if the enemy got outside the screen
        self.cleanFrame()
        winRule=200
        if self.player.score>winRule:
            self.screen="Win"
            self.isGameOver=True

        self.redrawAll()


    # play click music
    # code used from tutorial http://people.csail.mit.edu/hubert/pyaudio/docs/
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
    # code used from tutorial http://people.csail.mit.edu/hubert/pyaudio/docs/
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
        levelImproveScore=50
        if self.level==1:
            if self.player.score>levelImproveScore:
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
        if len(self.otherWeapens)<=3 and self.player.weapen=="spit":
            randomXplace=random.randint(1,self.width)
            randomYplace=random.randint(1,self.height)
            self.otherWeapens.append(w.RedBerry(randomXplace,randomYplace))
    # each time we change the Weapen if the player meet the weapen
    def changeWeapen(self):
        newOtherWeapens=[]
        weapenLifeLimit=10
        # once we change the weapen we only have 10 chances to shoot with new
        # weapen
        for bounusWeapen in self.otherWeapens:
            if self.checkMeetWeapen(bounusWeapen):
                self.weapenNameChange(bounusWeapen)
                self.weapenLife=weapenLifeLimit
               
            else:
                # those weapen didn't change we will add to new list
                newOtherWeapens.append(bounusWeapen)
        self.otherWeapens=newOtherWeapens


    # check whether we have eaten the weapen
    def checkMeetWeapen(self,bounusWeapen):
        x,y=self.player.xPosition,self.player.yPosition
       
        distance=math.sqrt((bounusWeapen.xPosition-x)**2+(bounusWeapen.yPosition-y)**2)
        distancelimit=40
        if distance<distancelimit:
            return True
        return False

    def weapenNameChange(self,bounusWeapen):
        if isinstance(bounusWeapen,w.RedBerry):
            self.player.weapen="redBerry"

    def addBoxesObstacle(self):
        (lower,upper)=(10,60)
        totalSize=9
        randomHight=random.randint(lower,upper)
        width    = self.width
        boxHeight= self.height/totalSize
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
                if ((abs(e.xPosition-x)<2*b.radius and 
                    abs(e.yPosition-y)<2*b.radius)):
                    self.Bullets.remove(b)
                    self.Enemies.remove(e)
                    self.increaseScore(b,e)
                    listEnemies=copy.copy(self.Enemies)
                    break  

    def increaseScore(self,bullet,enemy):
        birdScore=10
        sheepScore=20
        if isinstance(enemy,e.FlyBird):
            self.player.score+= birdScore # every killed bird will increase 10
        elif isinstance(enemy,e.JumpSheep):
            self.player.score+= sheepScore

    def moveEnemies(self):
        for enemy in self.Enemies:
            if isinstance (enemy,e.FlyBird):
                enemy.moveEnemy(self.canvas,self.player.xPosition,
                                self.player.yPosition)
            elif isinstance (enemy,e.JumpSheep):
             
                enemy.moveEnemy(self.canvas,self.width,self.height)

    def moveBullets(self):
        for b in self.Bullets:
            b.moveBullet(self.canvas)

    def addEnemies(self):
        # every time according to the counter we add enemies
        width=self.width
        height=self.height
        (x,y)=(width,random.randrange(0,height-1,2*self.player.radius))
        # if we have owl in the place we will find the 
        if len(self.Enemies)==1:
            enemyTemp=self.Enemies[0]
            if isinstance(enemyTemp,e.Owl):
                self.Enemies.pop()
        self.EnemyPresentCounter+=1
        # ever 10 times we need to add bird enemy
        if self.EnemyPresentCounter%self.EnemyBirdCyclceCoeff==0:
            if len(self.Enemies)< self.Difficulty:
                self.Enemies.append(e.FlyBird(x,y))

        # ever 5 times we need to add sheep which will jump every where
        if self.EnemyPresentCounter%self.EnemySheepCycleCoeff==0:
            if len(self.Enemies)< self.Difficulty:
                self.Enemies.append(e.JumpSheep(0,height))
    # check we have ever meet the enemy-[]
    def meetEnemies(self):
        warningCounterInitalNumber=3
        for e in self.Enemies:
            if self.player.isCollision(e):
                self.warningCounter=warningCounterInitalNumber
                self.minusLife()
                break
    def minusLife(self):
        self.player.life-=1
        if self.player.life<=0:
            self.isGameOver=True
            self.stopAllMusic()


game=Game()
game.run(900,500)
