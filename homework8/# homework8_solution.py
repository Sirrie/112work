# homework8_solution.py

def redrawAll(canvas):
    canvas.data.delete(ALL)
    drawBottomShape(canvas)

def drawBottomShape(canvas):
    for i in xrange(len(canvas.data.shapes)):
        left = shapeLeft(canvas,i)
        drawShape(canvas,canvas.data.shapes[i],left,canvas.data.minY,
            left+canvas.data.shapeSize,canvas.data.height)




def shuffle(L):
    new=copy.copy(L)

def init(canvas):
    canvas.data.delay = 40
    canvas.data.shapeVals=[0,3,4,5,6]
    canvas.data.shapes=shuffle(canvas.data.shapeVals)
    canvas.data.shapeSize = shapeSize =40
    canvas.data.shapeMargin
    
    # use to flag for selected
    canvas.data.selection =None


