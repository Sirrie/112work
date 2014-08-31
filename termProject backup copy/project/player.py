from Tkinter import *

import math
from weapen import *

class Player(object):
    def __init__(self,x,y,inputFileName):
        self.yPosition= y
        self.xPosition= x
        self.radius   = 10
        self.weapen   = "spit"

        self.imageFile= PhotoImage(file=inputFileName)
        self.lifeImageFile=PhotoImage(file="images/heart.gif")
        self.life = 3
        self.score= 0


    def drawPlayer(self,canvas):
        # draw the Item according to their postion
        r=self.radius
        cx=self.xPosition
        cy=self.yPosition
        (x0,y0,x1,y1)=(cx-r,cy-r,cx+r,cy+r)
        #canvas.create_rectangle(x0,y0,x1,y1,fill=self.color)
        canvas.create_image(cx,cy,image=self.imageFile)

    def isCollision(self,other):
        distanceOfTwoItem=math.sqrt((self.xPosition-other.xPosition)**2+(self.yPosition-other.yPosition)**2)
        # check whether two Items will collide
        if distanceOfTwoItem<=self.radius+other.radius:
            return True
        return False

    def shoot(self):
        if self.weapen == "spit":
            print "add spit"
            return Spit(self.xPosition,self.yPosition)
        elif self.weapen == "redBerry":
            print "add RedBerry"
            return RedBerry(self.xPosition,self.yPosition)



    def drawLife(self,canvas,width,height):
        cellSize = width /20
        for index in xrange(self.life):
            canvas.create_image(cellSize+index*cellSize,cellSize,image=self.lifeImageFile)


    def drawScore(self,canvas,width,height):
        totalSize=9
        ratio=4.0/5.0
        canvas.create_text(width*ratio,height/totalSize,
            font="Purisa 30 bold",text="Score :"+str(self.score))

        