# events-example0.py
# Barebones timer, mouse, and keyboard events

from Tkinter import *
import copy



def tireMousePressed(event,canvas):
    tireRedrawAll(canvas)

def tireKeyPressed(event,canvas):
    if(event.char=="r"):
        tireInit(canvas)
    if(event.char=="q"):
        tireGameOver(canvas)
    if(event.char=="t"):
    # use the keypress to pause the game
        canvas.data.isPause=not canvas.data.isPause
    if not canvas.data.isGameOver:
        if(event.keysym=="Up"):
            rotateFallingPiece(canvas)
        elif (event.keysym=="Down"):
            moveFallingPiece(canvas,+1,0)
        elif(event.keysym=="Left"):
            moveFallingPiece(canvas,0,-1)
        elif(event.keysym=="Right"):
            moveFallingPiece(canvas,0,+1)
    
    tireRedrawAll(canvas)

def tireGameOver(canvas):
    canvas.data.isGameOver=True

def tireTimerFired(canvas):
    if not canvas.data.isPause:
        doTimerFired(canvas)

    delay = 250 # milliseconds
    def f():
       tireTimerFired(canvas)
    canvas.after(delay, f) # pause, then call timerFired again
    
def doTimerFired(canvas):
    fallingPieceRow=canvas.data.fallingPieceRow
    fallingPiece=canvas.data.fallingPiece
    # should put this first and then 
    
    if ((not moveFallingPiece(canvas,+1,0)) or 
    fallingPieceRow+len(fallingPiece)>=canvas.data.rows-1):
        placeFallingPiece(canvas)
        if(canvas.data.isGameOver==False):
            newFallingPiece(canvas)
        if (not moveFallingPiece(canvas,+1,0)):
            tireGameOver(canvas)
        removeFullRow(canvas)

    tireRedrawAll(canvas)  
    

# remove full row
def removeFullRow(canvas):
    rows =canvas.data.rows
    board=canvas.data.board
    newRow=rows-1

    for oldRow in xrange(rows-1,-1,-1):

        for e in board[oldRow]:
            #if not full
            if e =="blue":
                board[newRow]=copy.copy(board[oldRow])
                newRow-=1

                break
    # pay attention to the index and the real value
    counter=newRow+1
    print counter
    canvas.data.score+=counter**2


# put the piece on the board
def placeFallingPiece(canvas):
    fallingPiece=canvas.data.fallingPiece
    board =canvas.data.board
    fallingPieceRow=canvas.data.fallingPieceRow
    startRow=canvas.data.fallingPieceRow
    startCol=canvas.data.fallingLeftColum;
    for row in xrange(len(fallingPiece)):
        for col in xrange(len(fallingPiece[0])):
            if fallingPiece[row][col]:
                board[startRow+row][startCol+col]=canvas.data.fallingPieceColor
              

def rotateFallingPiece(canvas):
    (oldCenterRow,oldCenterCol)=fallingPieceCenter(canvas)
    presentPiece=canvas.data.fallingPiece
    (rows,cols)=(len(presentPiece),len(presentPiece[0]))
    # this will perform the rotation create 
    newPiece=[]
    for col in xrange(cols):newPiece+=[[True]*rows]
    for row in xrange(rows):
        for col in xrange(cols):
            
            newPiece[cols-1-col][row]=presentPiece[row][col]
    canvas.data.fallingPiece=newPiece
    # should change it first, and put it in the canvas.data will give new center
    (newCenterRow,newCenterCol)=fallingPieceCenter(canvas)
    canvas.data.fallingPieceRow+=oldCenterRow-newCenterRow
    canvas.data.fallingLeftColum+=oldCenterCol-newCenterCol
    
    if not fallingPieceIsLegal(canvas):
        canvas.data.fallingPieceRow-=oldCenterRow-newCenterRow
        canvas.data.fallingLeftColum-=oldCenterCol-newCenterCol
        canvas.data.fallingPiece=presentPiece
   



def fallingPieceCenter(canvas):
    (cx,cy)=(canvas.data.fallingPieceRow,canvas.data.fallingLeftColum+1)
    return(cx,cy)

 
def moveFallingPiece(canvas,drow,dcol):
    # evertime you move the falling shape down
    canvas.data.fallingLeftColum+=dcol
    canvas.data.fallingPieceRow+=drow
    if not fallingPieceIsLegal(canvas):
        canvas.data.fallingLeftColum+=-dcol
        canvas.data.fallingPieceRow+=-drow
        return False
    return True
        
# we can check the leagal status
def fallingPieceIsLegal(canvas):
    board=canvas.data.board
    fallingPiece=canvas.data.fallingPiece
    fallingLeftColum=canvas.data.fallingLeftColum
    fallingPieceRow=canvas.data.fallingPieceRow
    emptyColor=canvas.data.emptyColor
    for row in xrange(len(canvas.data.fallingPiece)):
        for col in xrange(len(canvas.data.fallingPiece[0])):
            # on the board
            if fallingPiece[row][col]==True:
                if (fallingLeftColum+col<0 or fallingPieceRow+row>=len(board) 
                    or fallingLeftColum+col>=len(board[0]) or
                     fallingPieceRow+row<0):
                    return False
                if board[row+fallingPieceRow][col+fallingLeftColum]!=emptyColor:
                    
                    return False
    return True

import random 
def newFallingPiece(canvas):
    fallingNumber=random.randint(0,len(canvas.data.tetrisPieces)-1)
    canvas.data.fallingPiece=canvas.data.tetrisPieces[fallingNumber]
    canvas.data.fallingPieceColor =canvas.data.tetrisPieceColors[fallingNumber]
    canvas.data.fallingPieceRow=0
    canvas.data.fallingLeftColum=canvas.data.cols/2 - len(canvas.data.        fallingPiece)/2


def tireRedrawAll(canvas):
    canvas.delete(ALL) 
    # draw the board
    canvas.create_rectangle(0,0,canvas.data.width+2*canvas.data.margin,
        canvas.data.height+2*canvas.data.margin,fill="orange")
    tireDrawGame(canvas)
    drawScore(canvas)
    
def drawScore(canvas):

    canvas.create_text(canvas.data.margin/2,canvas.data.margin/2,anchor=NW,text="Score"+str(canvas.data.score),fill="blue",font=("Purisa",12))

def tireDrawGame(canvas):
    tireDrawBoard(canvas)
    if canvas.data.isGameOver:
        canvas.create_text(canvas.data.width/2,canvas.data.cellSize,text="Game Over",fill="red",font="Times 32 italic")
    elif canvas.data.isPause:
        canvas.create_text(canvas.data.width/2,canvas.data.cellSize,text="Pause",fill="red",font="Times 32 italic")
    else:
        drawFallingPiece(canvas)
    
    
def drawFallingPiece(canvas):
    fallingPiece=canvas.data.fallingPiece
    fallingPieceColor=canvas.data.fallingPieceColor
    fallingPieceRow=canvas.data.fallingPieceRow
    fallingleftColum=canvas.data.fallingLeftColum
    startMargin=canvas.data.margin
    # should get the margin and should print all the things here find what happened
    for row in xrange(len(fallingPiece)):
        for col in xrange(len(fallingPiece[0])):
            if fallingPiece[row][col]==True:
                (x0,y0,x1,y1)=getBoundingBox(canvas,fallingPieceRow+row,fallingleftColum+col)
                (x0,y0,x1,y1)=(x0+startMargin,y0+startMargin,x1+startMargin,y1+startMargin)
                tireDrawCell(canvas,x0,y0,x1,y1,fallingPieceColor)

    

# draw the whole board
def tireDrawBoard(canvas):
    (rows,cols)=(canvas.data.rows,canvas.data.cols)
    startMargin=canvas.data.margin
    for row in xrange(rows):
        for col in xrange(cols):
            color= canvas.data.board[row][col]
            (x0,y0,x1,y1)=getBoundingBox(canvas,row,col)
            (x0,y0,x1,y1)=(x0+startMargin,y0+startMargin,x1+startMargin,y1+startMargin)
            tireDrawCell(canvas,x0,y0,x1,y1,color)

# draw two rectangles at a given place          
def tireDrawCell(canvas,x0,y0,x1,y1,color):
    canvas.create_rectangle(x0,y0,x1,y1,fill="black")
    diff=2
    canvas.create_rectangle(x0+diff,y0+diff,x1-diff,y1-diff,fill=color)


def getBoundingBox(canvas,row,col):
    cellSize=canvas.data.cellSize
    x0 = col * cellSize
    y0 = row * cellSize
    x1 = x0 + cellSize
    y1 = y0 + cellSize
    return (x0, y0, x1, y1)



def makeBoard(canvas):
    colors=["blue","red","white","green","gray"]
    board = [[""]*canvas.data.cols for _ in xrange(canvas.data.rows)]
    for row in xrange(canvas.data.rows):
        for col in xrange(canvas.data.cols):
            board[row][col] = colors[0]
    return board

def tireInit(canvas):
    canvas.data.board=makeBoard(canvas)

    #Seven "standard" pieces (tetrominoes)
    iPiece = [
        [ True,  True,  True,  True]
    ]
      
    jPiece = [
        [ True, False, False ],
        [ True, True,  True]
    ]
      
    lPiece = [
        [ False, False, True],
        [ True,  True,  True]
    ]
      
    oPiece = [
        [ True, True],
        [ True, True]
    ]
      
    sPiece = [
        [ False, True, True],
        [ True,  True, False ]
    ]
      
    tPiece = [
        [ False, True, False ],
        [ True,  True, True]
    ]

    zPiece = [
        [ True,  True, False ],
        [ False, True, True]
    ]
    tetrisPieces = [ iPiece, jPiece, lPiece, oPiece, sPiece, tPiece, zPiece ]
    tetrisPieceColors = [ "red", "yellow", "magenta", "pink", "cyan", "green", "orange" ]
    canvas.data.tetrisPieces=dict()
    canvas.data.tetrisPieceColors=dict()
    counter=0
    for e in tetrisPieces:
        canvas.data.tetrisPieces[counter]=e
        counter+=1
    counter=0
    for e in tetrisPieceColors:
        canvas.data.tetrisPieceColors[counter]=e
        counter+=1
    canvas.data.emptyColor="blue"
    canvas.data.isGameOver=False
    canvas.data.score=0
    canvas.data.isPause=False
    newFallingPiece(canvas)

def runTires(rows,cols):
    # create the root and the canvas
    root = Tk()
    margin=30
    cellSize= 30
    canvasWidth = 2*margin + cols*cellSize
    canvasHeight = 2*margin + rows*cellSize
    canvas=Canvas(root,width=canvasWidth,height=canvasHeight)
    canvas.pack()
    root.resizable(width=0,height=0)
    class Struct: pass
    canvas.data = Struct()
    canvas.data.margin= margin
    canvas.data.rows= rows
    canvas.data.cols= cols
    canvas.data.width=canvasWidth
    canvas.data.height=canvasHeight
    canvas.data.cellSize=cellSize
    tireInit(canvas)
    # set up events
    root.bind("<Button-1>",lambda event: tireMousePressed(event,canvas))
    root.bind("<Key>", lambda event:tireKeyPressed(event,canvas))
    tireTimerFired(canvas)
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)
#-----------------------------------------------------------------------#
runTires(15,10)