from Tkinter import *
import math
class Weapen(object):
    def __init__(self,x,y,inputFileName=None):
        self.xPosition=x
        self.yPosition=y
        self.radius  =10
        self.imageFile= PhotoImage(file=inputFileName)
        self.VelocityX=7

    def isCollision(self,other):
        distanceOfTwoItem=math.sqrt((self.xPosition-other.xPosition)**2+(self.yPosition-other.yPosition)**2)
        # check whether two Items will collide
        if distanceOfTwoItem<=self.radius+other.radius:
            return True
        return False
        
    def moveBullet(self,canvas):
        self.xPosition+=self.VelocityX

    def drawBullet(self,canvas):
        cx,cy=self.xPosition,self.yPosition
        canvas.create_image(cx,cy,image=self.imageFile)



class Spit(Weapen):
    def __init__(self,x,y):
        super(Spit,self).__init__(x,y,"images/spit.gif")
        

   # def drawBullets(self,canvas):
        # cx,cy=self.xPosition,self.yPosition
        # canvas.create_oveal(cx-2,cy-2,cx+2,cy+2,fill="yello")


class RedBerry(Weapen):
    def __init__(self,x,y):
        super(RedBerry,self).__init__(x,y,"images/RedBerry.gif")
        


class Bullet(Weapen):
    def __init__(self,x,y):
        super(Bullet,self).__init__(x,y,"images/Bullet.gif")
        self.dirX=-10

    # shoot towards the player
    def moveBullet(self,playerX,playerY):
        dx=playerX-self.xPosition
        dy=playerY-self.yPosition
        # move towards the player
        VectorDistance= math.sqrt(dx**2+dy**2)
        dirX,dirY = (dx/VectorDistance*10,dy/VectorDistance*10)
        self.xPosition+=self.dirX
        self.yPosition+=dirY

class Laser(Weapen):
    def __init__(self,sx,sy,tx,ty):
        self.startX=sx
        self.startY=sy
        self.targetX=tx
        self.targetY=ty
        self.xPosition=(sx+tx)*1.0/2
        self.yPosition=(sy+ty)*1.0/2

    def drawBullet(self,canvas):
        r = 5
        sx=self.startX
        sy=self.startY
        tx=self.targetX
        ty=self.targetY
        canvas.create_polygon((sx,sy),(sx,sy-r),(tx,ty-r),(tx,ty),fill="green")









