from Tkinter import *
import math
from weapen import *

class Enemy(object):
    def __init__(self,x,y,inputFileName):
        self.xPosition=x
        self.yPosition=y
        self.radius =50
        self.imageFile = PhotoImage(file=inputFileName)
        



    
    def drawEnemy(self,canvas):
        cx=self.xPosition
        cy=self.yPosition
        canvas.create_image(cx,cy,image=self.imageFile)

    def isCollision(self,other):
        distanceOfTwoItem=math.sqrt((self.xPosition-other.xPosition)**2+(self.yPosition-other.yPosition)**2)
        # check whether two Items will collide
        if distanceOfTwoItem<=self.radius+other.radius:
            return True
        return False

    def moveEnemy(self,canvas):
        pass

class Cloud(Enemy):
    def __init__(self,x,y):
        super(Cloud,self).__init__(x,y,"images/cloud.gif")
        

class FlyBird(Enemy):
    def __init__(self,x,y):
        super(FlyBird,self).__init__(x,y,"images/bird.gif")

    def moveEnemy(self,canvas,x,y):
        dx=x-self.xPosition
        dy=y-self.yPosition
        # move towards the player
        VectorDistance= math.sqrt(dx**2+dy**2)
        dirX,dirY = (dx/VectorDistance*5,dy/VectorDistance*5)
        self.xPosition+=dirX
        self.yPosition+=dirY



    def drawEnemy(self,canvas):
        # birds only move towards the player
        r=self.radius
        cx=self.xPosition
        cy=self.yPosition
        (x0,y0,x1,y1)=(cx-r,cy-r,cx+r,cy+r)
        #canvas.create_rectangle(x0,y0,x1,y1,fill=self.color)
        canvas.create_image(cx,cy,image=self.imageFile)

class JumpSheep(Enemy):
    def __init__(self,x,y):
        super(JumpSheep,self).__init__(x,y,"images/sheep.gif")
        self.boundingLimit=200
        self.Velocityx=10
        self.Velocityy=20
        
    def moveEnemy(self,canvas,width,height):
        # make the sheep jumping
        self.xPosition+=self.Velocityx
        self.xPosition=self.xPosition%width
        self.yPosition-=self.Velocityy
        if self.yPosition<=self.boundingLimit or self.yPosition>=height:
            self.Velocityy=-self.Velocityy

    def drawEnemy(self,canvas):
        r=self.radius
        cx=self.xPosition
        cy=self.yPosition
        (x0,y0,x1,y1)=(cx-r,cy-r,cx+r,cy+r)
       # canvas.create_rectangle(cx-r,cy-r,cx+r,cy+r,fill="green")
        canvas.create_image(cx,cy,image=self.imageFile)


class Owl(Enemy):
    def __init__(self,x,y):
        super(Owl,self).__init__(x,y,"images/owl.gif")
        self.lifeLong=500
        self.Velocityx=-5
        self.radius = 80

    # the basic bullet the owl use
    def shootBullet(self):
        return Bullet(self.xPosition,self.yPosition)

    # another weapen the owl use 
    def shootLaser(self,x,y):
        return Laser(self.xPosition,self.yPosition,x,y)


    def moveEnemy(self):
        self.xPosition+=self.Velocityx

    def dcreaseLife(self,weapen):
        if weapen =="spit":
            self.lifeLong-=100
        elif weapen == "redBerry":
            self.lifeLong-=20


