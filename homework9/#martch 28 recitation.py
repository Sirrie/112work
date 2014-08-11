#martch 28 recitation.py'
from fractions import *

class MyFraction(object):
    def __init__(self,numerator,denominator):
        #it's a constructor
        self.numerator = numerator 
        self.denominator = denominator
        self.reduce()

    def reduce(self):
        g = gcd(self.numerator,self.denominator)
        self.numerator /=g
        self.denominator /=g

    def __add__(self,other):
        g = gcd(self.denominator,other.denominator)
        p = self.denominator * other.denominator
        lcm = p / g
        n1 = self.numerator * lcm / self.denominator
        n2 = self.numerator * lcm / other.denominator

        return MyFraction(n1+n2,lcm)

    def __mul__(self,other):
        return MyFraction(self.numerator*other.numerator,self.denominator*other.denominator)

    def __repr__(self):
################ eval(repr(obj)==obj)
        return "MyFraction(" +repr(self.numerator)+","+repr(self.denominator)+")"

    def __str__(self):
        return str(self.numerator)+"/"+str(self.denominator)

myfrac=MyFraction(231,23121)
print myfrac
print str(myfrac)
print repr(myfrac)
print eval(repr(myfrac))
# print will call str


print gcd(23,31)

a="1"
print repr(a)
a =1 
print repr(a) # gives back only string 


# Animation().run()
# Bird
# Wall
''' create a Bird class:
     the property  we have in a bird 
     class Bird(object):
        def __init__(self):
            self.y = 100
            self.x = 75
            self.dy = 0
        def flap(self):
            self.dy = -5

        def update(self):
            acceleration = 0.3
            self.y += self.dy
            self.dy += acceleration

        def draw(self,canvas):
            # draw bird
            width = 20
            (x,y) = (self.x, self.y)
            canvas.create_rectangle(x-width/2,y-width/2,x+width/2,y+with/2.fill="blue")

        def collide(self):
            lkjkdfs


    class Wall(object):
        def __init__(self,f):
            self.visible = f
            self.x =325
        def draw(self):

        def 

    def keyPressed(canvse):

    def timerFired(canvas):
        canvas.data.bird.draw()





'''
