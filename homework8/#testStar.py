# drawStar.py

import math

from Tkinter import *
root = Tk()
canvas = Canvas(root, width=500, height=500)
canvas.pack()

def drawStar(canvas, cx, cy, rInner, rOuter, n, fillColor):
    if (rInner == None):
        thetaInner = math.radians(90 + 360/(2*n))
        thetaOuter = math.radians(90 + 2*360/(2*n))
        rInner = rOuter*math.sin(thetaOuter)/math.sin(thetaInner)
    pts = []
    for step in xrange(2*n):
        theta = math.radians(90 + step*360/(2*n))
        r = rOuter if (step % 2 == 0) else rInner
        x = cx + r*math.cos(theta)
        y = cy - r*math.sin(theta)
        pts += [(x,y)]
    canvas.create_polygon(pts, fill=fillColor)

drawStar(canvas, 150, 150, 20, 150, 20, "red")

canvas.create_oval(300, 50, 500, 250, fill="darkBlue")
drawStar(canvas, 400, 150, None, 100, 5, "lightBlue")

drawStar(canvas, 250, 350, None, 100, 6, "green")
drawStar(canvas, 250, 350, None,  75, 6, "darkGreen")

root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)
