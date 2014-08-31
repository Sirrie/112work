from Tkinter import *
import math
import random


class BackGround(object):
    def __init__(self,x,y,length):
        self.centerX=x
        self.centerY=y
        self.xPosition=x
        self.yPosition=y
        self.length = length
        self.VelocityX=20
        self.someImageFile=PhotoImage("images/cloud.gif")
    

    def drawBackGround(self,canvas,height):
        print height,"present height"
        self.centerY=height
        canvas.create_rectangle(self.centerX,0,self.centerX+self.VelocityX,
            self.centerY,fill="LightSkyBlue",outline="LightSkyBlue")
    

    def moveBackGround(self):
        self.centerX-=self.VelocityX


class TopBoxes(BackGround):
    def __init__(self,x,y,length):
        super(TopBoxes,self).__init__(x,y,length)

class BottomBoxes(BackGround):
    def __init__(self,x,y,length):
        super(BottomBoxes,self).__init__(x,y,length)
    def drawBackGround(self,canvas,height):
        canvas.create_rectangle(self.centerX,height-self.length,self.centerX+self.VelocityX,height,fill="gold",outline="yellow")

