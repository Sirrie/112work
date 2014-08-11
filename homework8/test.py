from Tkinter import *
root = Tk()
canvas = Canvas(root, width=300, height=200)
canvas.pack()
canvas.create_oval((50, 50), (250, 150), fill="yellow")
#canvas.create_polygon([(50,30),(150,50),(250,30),(150,10)], fill="green")

fillColor="green"
r=20
cx=150
cy=150

(x0,y0,x1,y1)=(cx-r,cy-r,cx+r,cy+r)
print (x0,y0,x1,y1)
parameterx=0.25
canvas.create_polygon([(x0+parameterx*r,y0),(x1-parameterx*r,y0),(x1,cy),(x1-parameterx*r,y1),(x0+parameterx*r,y1),(x0,cy)],fill=fillColor)
print [(x0+parameterx*r,y0),(x1-parameterx*r,y0),(x1,cy),(x1-parameterx*r,y1),(x0+parameterx*r,y1),(x0,cy)]
root.mainloop()