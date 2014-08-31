class Player(object):
    def __init__(self,x,y):
        self.yPosition=y
        self.xPosition=x
        self.radius   = 10
        self.life   = 10

    def drawPlayer(self,canvas):
        r=self.radius
        cx=self.xPosition
        cy=self.yPosition
        (x0,y0,x1,y1)=(cx-r,cy-r,cx+r,cy+r)
        canvas.create_rectangle(x0,y0,x1,y1,fill=self.color)


