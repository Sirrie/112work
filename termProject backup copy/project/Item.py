from Tkinter import *
import math
class Item(object):
    def __init__(self,x,y,inputFileName=None):
        self.yPosition= y
        self.xPosition= x
        self.radius   = 10
        self.imageFile= PhotoImage(file=inputFileName)
        self.Velocityx=5
        self.Velocityy=5


    def drawItem(self,canvas):
        # draw the Item according to their postion
        r=self.radius
        cx=self.xPosition
        cy=self.yPosition
        (x0,y0,x1,y1)=(cx-r,cy-r,cx+r,cy+r)
        #canvas.create_rectangle(x0,y0,x1,y1,fill=self.color)
        canvas.create_image(cx,cy,image=self.imageFile)


    def moveItem(self,canvass):
        self.xPosition+=self.Velocityx
        self.yPosition+=self.Velocityy



    


#________________________Player_____________________#



class Player(Item):
    def __init__(self,x,y,inputFileName):
        self.yPosition= y
        self.xPosition= x
        self.radius   = 10
        self.imageFile= PhotoImage(file=inputFileName)
        self.life = 3


    def drawPlayer(self,canvas):
        # draw the Item according to their postion
        r=self.radius
        cx=self.xPosition
        cy=self.yPosition
        (x0,y0,x1,y1)=(cx-r,cy-r,cx+r,cy+r)
        #canvas.create_rectangle(x0,y0,x1,y1,fill=self.color)
        canvas.create_image(cx,cy,image=self.imageFile)

    def shoot(self,canvas,weapean):
        Weapen(self.xPosition,self.yPosition)



    def drawLife(self,canvas):
        width=canvas.width
        height=canvas.height

        
##________________enemis____________________#

class Enemy(Item):
    def __init__(self,x,y,inputFileName):
        self.xPosition=x
        self.yPosition=y
        self.radius =10
        self.imageFile = PhotoImage(file=inputFileName)
        

    def drawEnemy(self,canvas):
        cx=self.xPosition
        cy=self.yPosition
        canvas.create_image(cx,cy,image=self.imageFile)
    def moveEnemy(self,canvas):
        pass


class FlyBird(Enemy):
    def __init__(self,x,y):
        super(FlyBird,self).__init__(x,y,"images/bird.gif")

    def moveEnemy(self,canvas,x,y):
        dx=x-self.xPosition
        dy=y-self.yPosition
        # move towards the hamster
        VectorDistance= math.sqrt(dx**2+dy**2)
        dirX,dirY = (dx/VectorDistance*10,dy/VectorDistance*10)
        self.xPosition+=dirX
        self.yPosition+=dirY



    def drawEnemy(self,canvas):
       
        frequency =4
        speed =1
        r=self.radius
        cx=self.xPosition
        cy=self.yPosition
        (x0,y0,x1,y1)=(cx-r,cy-r,cx+r,cy+r)
        #canvas.create_rectangle(x0,y0,x1,y1,fill=self.color)
        canvas.create_image(cx,cy,image=self.imageFile)







###_______________weapen____________________#

class Weapen(Item):
    def __init__(self,x,y):
        super(Weapen,self).__init__(x,y)
        


    def moveWeapen(self,canvas):
        self.xPosition-=self.Velocityx
        

    


class Spit(Weapen):
    def __init__(self,x,y):
        super(Weapen,self).__init__(x,y,"images/bird.gif")
    


class RedBerry(Weapen):
    def __init__(self,x,y):
        super(Weapen,self).__init__(x,y,"images/1.gif")


