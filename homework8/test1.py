'''
homework8
andrewID: siyuchen



'''


from Tkinter import *
import math
import random
import copy
###-----------------------------------------------------------------------####

## game of snake
def snakeMousePressed(canvas,event):
    snakeRedrawAll(canvas)

def snakeKeyPressed(canvas,event):
    canvas.data.ignoreNextTimerEvent=True
    if (event.char=="q"):
        gameOver(canvas)
    elif(event.char=="r"):
        init(canvas)
    elif(event.char=="d"):
        canvas.data.inDebugMode = not canvas.data.inDebugMode
    # check if is not game over we should trace all key press situations
    if(canvas.data.isGameOver==False):
        if(event.keysym=="Up"):
            moveSnake(canvas,-1,0)
        elif (event.keysym=="Down"):
            moveSnake(canvas,1,0)
        elif(event.keysym=="Left"):
            moveSnake(canvas,0,-1)
        elif(event.keysym=="Right"):
            moveSnake(canvas,0,1)
    snakeRedrawAll(canvas)

def moveSnake(canvas,drow,dcol):
    snakeBoard=canvas.data.snakeBoard
    (rows,cols)=(len(snakeBoard),len(snakeBoard[0]))
    # use first try and then check method
    canvas.data.snakeDrow=drow
    canvas.data.snakeDcol=dcol
    headRow=canvas.data.headRow
    headCol=canvas.data.headCol
    newHeadRow=canvas.data.headRow+drow
    newHeadCol=canvas.data.headCol+dcol
   
    # check if the snake is outside the board gameover
    if ((newHeadRow <0 )or (newHeadCol<0) or (newHeadRow>= rows) 
        or (newHeadCol>=cols)):
        gameOver(canvas)
    # if the new head reaches the snake itself gameOver()
    elif snakeBoard[newHeadRow][newHeadCol]>0:
        gameOver(canvas)
    # if the new position is food just eat it
    elif snakeBoard[newHeadRow][newHeadCol]==-1:# eat food
        snakeBoard[newHeadRow][newHeadCol]=snakeBoard[headRow][headCol]+1
        canvas.data.headRow=newHeadRow
        canvas.data.headCol=newHeadCol
        placeFood(canvas)# after eatting food we should place food on that place 
    else:                                       # move 
        snakeBoard[newHeadRow][newHeadCol]=snakeBoard[headRow][headCol]+1
        canvas.data.headRow=newHeadRow
        canvas.data.headCol=newHeadCol
        removeTail(canvas)
    
# to loop through the whole snake and minus 1 to get tail moved
def removeTail(canvas):
    snakeBoard = canvas.data.snakeBoard
    rows=len(snakeBoard)
    cols=len(snakeBoard[0])
    for row in range(rows):
        for col in range(cols):
            if (snakeBoard[row][col]>0):
                snakeBoard[row][col]-=1


def gameOver(canvas):
    canvas.data.isGameOver=True



def snakeTimerFired(canvas):
    ignoreThisTimeEvent=canvas.data.ignoreNextTimeEvent
    canvas.data.ignoreNextTimeEvent=False
    if(canvas.data.isGameOver == False):
       #!!!!very important when the game is not over, we should 
       #ignore this time event because keypress has already change the 
       # direction
        (drow,dcol)=(canvas.data.snakeDrow,canvas.data.snakeDcol)
        if not ignoreThisTimeEvent:
            moveSnake(canvas,drow,dcol)
            snakeRedrawAll(canvas)
    delay=150
    canvas.after(delay,lambda :snakeTimerFired(canvas))

def snakeRedrawAll(canvas):
    canvas.delete(ALL)
    drawSnakeBoard(canvas)
    if canvas.data.isGameOver:
        canvas.create_text(150,150,text="GAME  OVER", font=("Helvetica",32,"bold"))

def printInstructions():
    print "Snake!"
    print "Use the arrow keys to move the Snake"
    print "Stay on the board !"
    print "And don't crash into yourself"
    print "Press 'd' for debug mode."  
    print "Press 'r' to restart."
    return

def drawSnakeBoard(canvas):
    snakeBoard = canvas.data.snakeBoard
    rows=len(snakeBoard)
    cols=len(snakeBoard[0])
    for row in range(rows):
        for col in range(cols):
            drawSnakeCell(canvas,snakeBoard,row,col)
    

def drawSnakeCell(canvas,snakeBoard,row,col):
    margin = 5
    cellSize =30
    left=margin + col * cellSize
    right=margin + (col+1)*cellSize
    top = margin+row*cellSize
    bottom=top+cellSize
    # fill the original places with "white" color
    canvas.create_rectangle(left,top,right,bottom,fill="white")
    if(snakeBoard[row][col]>0):
        canvas.create_oval(left,top,right,bottom,fill="blue")
    elif snakeBoard[row][col]==-1:
        canvas.create_oval(left,top,right,bottom,fill="green")
    if(canvas.data.inDebugMode==True):
        canvas.create_text(left+cellSize/2,top+cellSize/2,text=str(snakeBoard[row][col]))


import random

def placeFood(canvas):
    snakeBoard=canvas.data.snakeBoard
    boardLimit=len(snakeBoard)-1
    boardWidthLimit=len(snakeBoard[0])-1
    # randomly generate food and place it 
    (row,col)=(random.randint(0,boardLimit),random.randint(0,boardWidthLimit))
    while snakeBoard[row][col]>0:
        (row,col)=(random.randint(0,boardLimit),random.randint(0,boardLimit))
    snakeBoard[row][col] = -1
    canvas.data.snakeBoard = snakeBoard

# generate the snakeBoard
def loadSnakeBoard(canvas):
    rows=canvas.data.rows
    cols=canvas.data.cols
    temp=[]
    # generate a new blank board
    for row in xrange(rows):
       temp+=[[0]*cols]
    (centerRow,centerCol)=(rows/2,cols/2)
    temp[centerRow][centerCol]=1
    canvas.data.snakeBoard=temp
    canvas.data.ignoreNextTimeEvent=False
    findSnakeHead(canvas)
    placeFood(canvas)
    
def findSnakeHead(canvas):
    # use a maximum value to denote snakehead
    snakeBoard = canvas.data.snakeBoard
    rows=len(snakeBoard)
    cols=len(snakeBoard[0])
    headRow=0
    headCol=0
    maxValue=0
    for row in range(rows):
        for col in range(cols):
            if snakeBoard[row][col] > maxValue:
                maxValue=snakeBoard[row][col]
                headRow=row
                headCol=col
    canvas.data.headRow = headRow
    canvas.data.headCol = headCol
    
    

def init(canvas):
    printInstructions()
    loadSnakeBoard(canvas)
    canvas.data.inDebugMode=False
    canvas.data.isGameOver=False
    # new values to make animation
    canvas.data.snakeDrow=0
    canvas.data.snakeDcol=-1
    # if we initial it as 0,0 it will alway stucked

    snakeRedrawAll(canvas)

def snakeRun(rows,cols):
    # create the root and the canvas
    root = Tk()
    margin = 5
    cellSize = 30
    canvasWidth = 2*margin + cols*cellSize
    canvasHeight = 2*margin + rows*cellSize
    canvas = Canvas(root, width=canvasWidth, height=canvasHeight)
    canvas.pack()
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    canvas.data.rows=rows
    canvas.data.cols=cols

    init(canvas)
    # set up events
    root.bind("<Button-1>", lambda event: snakeMousePressed(canvas,event))
    root.bind("<Key>", lambda event:snakeKeyPressed(canvas,event))
    snakeTimerFired(canvas)
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)


####--------------------------------------------------------------------####

## game of tetrises
def tetriseMousePressed(event,canvas):
    tetriseRedrawAll(canvas)

def tetriseKeyPressed(event,canvas):
    if(event.char=="r"):
        tetriseInit(canvas)
    if(event.char=="q"):
        tetriseGameOver(canvas)
    if(event.char=="t"):
    # use the keypress to pause the game
        canvas.data.isPause=not canvas.data.isPause
    if not canvas.data.isGameOver:
    # if the game is not over, we just react with the different key press
        if(event.keysym=="Up"):
            rotateFallingPiece(canvas)
        elif (event.keysym=="Down"):
            moveFallingPiece(canvas,+1,0)
        elif(event.keysym=="Left"):
            moveFallingPiece(canvas,0,-1)
        elif(event.keysym=="Right"):
            moveFallingPiece(canvas,0,+1)
    tetriseRedrawAll(canvas)

def tetriseGameOver(canvas):
    canvas.data.isGameOver=True


# remove full row
def removeFullRow(canvas):
    rows =canvas.data.rows
    board=canvas.data.board
    # we need a newRow to record the rows we should draw in a new board
    newRow=rows-1
    for oldRow in xrange(rows-1,-1,-1):
        for e in board[oldRow]:
            #if not full
            if e =="blue":
                #!!!important thing should use copy.copy, other wise it is only
                # a reference 
                board[newRow]=copy.copy(board[oldRow])
                newRow-=1
                break
    # pay attention to the index and the real value
    counter=newRow+1
    canvas.data.score+=counter**2


# put the piece on the board
def placeFallingPiece(canvas):
    fallingPiece=canvas.data.fallingPiece
    board =canvas.data.board
    fallingPieceRow=canvas.data.fallingPieceRow
    startRow=canvas.data.fallingPieceRow
    startCol=canvas.data.fallingLeftColum;
    # store the falling piece color information on the board
    for row in xrange(len(fallingPiece)):
        for col in xrange(len(fallingPiece[0])):
            if fallingPiece[row][col]:
                board[startRow+row][startCol+col]=canvas.data.fallingPieceColor
              
# rotate counterClockWise
def rotateFallingPiece(canvas):
    (oldCenterRow,oldCenterCol)=fallingPieceCenter(canvas)
    presentPiece=canvas.data.fallingPiece
    (rows,cols)=(len(presentPiece),len(presentPiece[0]))
    # this will perform the rotation create a new one and copy from the
    # old piece
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
    # check if it is legal placement
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
    canvas.data.fallingPieceRow +=drow
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
            # for every True place in the falling Piece
            if fallingPiece[row][col]==True:
                if (fallingLeftColum+col<0 
                    or fallingPieceRow+row>=len(board) 
                    or fallingLeftColum+col>=len(board[0]) or
                     fallingPieceRow+row<0):
                    return False
            # check whether there is empty place for the new Piece
                if (board[row+fallingPieceRow][col+fallingLeftColum]!=emptyColor): 
                    return False
    return True

def newFallingPiece(canvas):
    # randomly generate falling pieces
    fallingNumber = random.randint(0,len(canvas.data.tetrisPieces)-1)
    canvas.data.fallingPiece = canvas.data.tetrisPieces[fallingNumber]
    canvas.data.fallingPieceColor =canvas.data.tetrisPieceColors[fallingNumber]
    canvas.data.fallingPieceRow = 0
    canvas.data.fallingLeftColum=canvas.data.cols/2 - len(canvas.data.        fallingPiece)/2


def tetriseTimerFired(canvas):
    # realize pause function 
    if not canvas.data.isPause:
        doTimerFired(canvas)
    delay = 250 # milliseconds
    def f():
       tetriseTimerFired(canvas)
    canvas.after(delay, f) # pause, then call timerFired again
    
def doTimerFired(canvas):
    # enclapse the timerFired functions
    fallingPieceRow=canvas.data.fallingPieceRow
    fallingPiece=canvas.data.fallingPiece
    # should put this first and then check whether we have the chance to 
    # do that
    if ((not moveFallingPiece(canvas,+1,0)) or 
    fallingPieceRow+len(fallingPiece)>=canvas.data.rows-1):
        placeFallingPiece(canvas)
        if(canvas.data.isGameOver==False):
            newFallingPiece(canvas)
    # try and test method, if we find the falling piece can't move, 
    # the game is over
        if (not moveFallingPiece(canvas,+1,0)):
            tetriseGameOver(canvas)
        removeFullRow(canvas)
    tetriseRedrawAll(canvas)     




def tetriseRedrawAll(canvas):
    canvas.delete(ALL) 
    # draw the board
    canvas.create_rectangle(0,0,canvas.data.width+2*canvas.data.margin,
        canvas.data.height+2*canvas.data.margin,fill="orange")
    tetriseDrawGame(canvas)
    drawScore(canvas)
    
def drawScore(canvas):
    # draw score on the board left place
    canvas.create_text(canvas.data.margin/2,canvas.data.margin/2,anchor=NW,text="Score"+str(canvas.data.score),fill="blue",font=("Purisa",12))

def tetriseDrawGame(canvas):
    tetriseDrawBoard(canvas)
    drawFallingPiece(canvas)
    # draw gameover information
    if canvas.data.isGameOver:
        canvas.create_text(canvas.data.width/2,canvas.data.cellSize,text="Game Over",fill="red",font="Times 32 italic")
    # draw pause information
    elif canvas.data.isPause:
        canvas.create_text(canvas.data.width/2,canvas.data.cellSize,text="Pause",fill="red",font="Times 32 italic")
    
    
def drawFallingPiece(canvas):
    fallingPiece=canvas.data.fallingPiece
    fallingPieceColor=canvas.data.fallingPieceColor
    fallingPieceRow=canvas.data.fallingPieceRow
    fallingleftColum=canvas.data.fallingLeftColum
    startMargin=canvas.data.margin
    # should get the margin, and add the margin to the box
    for row in xrange(len(fallingPiece)):
        for col in xrange(len(fallingPiece[0])):
            if fallingPiece[row][col]==True:
                (x0,y0,x1,y1)=getBoundingBox(canvas,fallingPieceRow+row,fallingleftColum+col)
                (x0,y0,x1,y1)=(x0+startMargin,y0+startMargin,x1+startMargin,y1+startMargin)
                tetriseDrawCell(canvas,x0,y0,x1,y1,fallingPieceColor)

    

# draw the whole board
def tetriseDrawBoard(canvas):
    (rows,cols)=(canvas.data.rows,canvas.data.cols)
    startMargin=canvas.data.margin
    for row in xrange(rows):
        for col in xrange(cols):
            color= canvas.data.board[row][col]
            (x0,y0,x1,y1)=getBoundingBox(canvas,row,col)
            (x0,y0,x1,y1)=(x0+startMargin,y0+startMargin,x1+startMargin,y1+startMargin)
            tetriseDrawCell(canvas,x0,y0,x1,y1,color)

# draw two rectangles at a given place          
def tetriseDrawCell(canvas,x0,y0,x1,y1,color):
    canvas.create_rectangle(x0,y0,x1,y1,fill="black")
    diff=2
    canvas.create_rectangle(x0+diff,y0+diff,x1-diff,y1-diff,fill=color)

# helper function to calculate the place of the box cell
def getBoundingBox(canvas,row,col):
    cellSize=canvas.data.cellSize
    x0 = col * cellSize
    y0 = row * cellSize
    x1 = x0 + cellSize
    y1 = y0 + cellSize
    return (x0, y0, x1, y1)



def makeBoard(canvas):
    # make board at the right place 
    colors=["blue","red","white","green","gray"]
    board = [[""]*canvas.data.cols for _ in xrange(canvas.data.rows)]
    for row in xrange(canvas.data.rows):
        for col in xrange(canvas.data.cols):
            board[row][col] = colors[0]
    return board

def tetriseInit(canvas):
    canvas.data.board=makeBoard(canvas)
    tetriseInitPiece(canvas)
    canvas.data.emptyColor="blue"
    canvas.data.isGameOver=False
    canvas.data.score=0
    canvas.data.isPause=False
    newFallingPiece(canvas)


def tetriseInitPiece(canvas):
    #Seven "standard" pieces (tetrominoes)
    iPiece = [[ True,  True,  True,  True]] 
    jPiece = [[ True, False, False ],[ True, True,  True]]
    lPiece = [[ False, False, True],[ True,  True,  True]]  
    oPiece = [[ True, True],[ True, True]] 
    sPiece = [[ False, True, True],[ True,  True, False ]]  
    tPiece = [[ False, True, False ],[ True,  True, True]]
    zPiece = [[ True,  True, False ],[ False, True, True]]
    tetrisPieces = [ iPiece, jPiece, lPiece, oPiece, sPiece, tPiece, zPiece ]
    tetrisPieceColors = [ "red", "yellow", "magenta", "pink", "cyan", "green", "orange" ]
    canvas.data.tetrisPieces=dict()
    canvas.data.tetrisPieceColors=dict()
    counter=0
    # put all the tetrisPieces into a dictionary thus we can call each one 
    # according to their number and get it
    for e in tetrisPieces:
        canvas.data.tetrisPieces[counter]=e
        counter+=1
    counter=0
    for e in tetrisPieceColors:
        canvas.data.tetrisPieceColors[counter]=e
        counter+=1
    

def runtetrises(rows,cols):
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
    tetriseInit(canvas)
    # set up events
    root.bind("<Button-1>",lambda event: tetriseMousePressed(event,canvas))
    root.bind("<Key>", lambda event:tetriseKeyPressed(event,canvas))
    tetriseTimerFired(canvas)
    # and launch the app
    root.mainloop()  
    # This call BLOCKS (so your program waits until you close the window!)

####--------------------------------------------------------------------####
#game of invasion shapes
def invaMousePressed(event,canvas):
    # when you press the mouse once you find the index of the shape 
    # that you click on you can first change the color and then the 
    # second time swap it
    selectedShape=clickSelectedShape(event,canvas)
    mouseClickCounter=canvas.data.mouseClickCounter
    if selectedShape!=None:
        mouseClickCounter+=1
        if mouseClickCounter==1:
            #changeShapeColor(canvas,selectedShape)
            canvas.data.selectedShape=selectedShape
            canvas.data.previous=selectedShape
            canvas.data.mouseClickCounter=mouseClickCounter
        elif mouseClickCounter==2:
            swapShape(canvas,selectedShape)
            # every time after I check I should update the starNumber and check
            # is gameover and if game is not over we should generate new 
            # falling shapes
            if checkMatch(canvas):
                canvas.data.starNumber+=1
                if canvas.data.starNumber <0 or canvas.data.starNumber==5:
                    canvas.data.isGameOver=True
                else:
                    newFallingShapes(canvas)
            mouseClickCounter=0
            canvas.data.mouseClickCounter=mouseClickCounter
            canvas.data.selectedShape=None
    # check whether the falling shapes and the bottom shapes match        
    invaRedrawAll(canvas)


# return the selected index of the shape
def clickSelectedShape(event,canvas):
    bottomShapes=canvas.data.bottomShapes
    (x,y)=(event.x,event.y)
    print (x,y)
    counter=0
    r=canvas.data.r
    for (bx,by) in bottomShapes:
        (top,bottom,left,right)=(by-r,by+r,bx-r,bx+r)
       # we should check that y should be smaller than the bottom but 
       #larger than the top
        if (( x>left and x<right) and (y<bottom and y>top)):
            return counter
        counter+=1
    return None

# change the shape collor if it is chosen
def changeShapeColor(canvas,selectShape):
    # updatae the color that has been chosen
    bottomShapes=canvas.data.bottomShapes
    (cx,cy)=bottomShapes[selectShape]
    color=canvas.data.shapeColors[0]
    canvas.data.bottomShapes[selectShape]=(cx,cy)

def invaKeyPressed(event,canvas):
    if(event.char=="r"):
        invaInit(canvas)
    invaRedrawAll(canvas)

# we need to swap the target chosen  place
def swapShape(canvas,selectShape):
    presentShapes=canvas.data.bottomShapes
    previous=canvas.data.previous
    # swap those things
    (presentShapes[previous],presentShapes[selectShape])=(presentShapes[selectShape],presentShapes[previous])   
    canvas.data.bottomShapes=presentShapes

def moveFallingShapes(canvas):
    # move falling Shapes step by step
    fallingShapes=canvas.data.newFallingShapes
    cellHeight=canvas.data.cellHeight
    for index in xrange(len(fallingShapes)):
        (cx,cy)=fallingShapes[index]
        fallingShapes[index]=(cx,cy+cellHeight/10)
    canvas.data.newFallingShapes=fallingShapes  

def checkMatch(canvas):
    bottomShapes=canvas.data.bottomShapes
    fallingShapes=canvas.data.newFallingShapes
    # when falling shapes get to the bottom check wether they are the same as
    # the bottom ones
    xFalling=[]
    xBottom=[]
    for i in xrange(len(bottomShapes)):
        (xf,yf)=fallingShapes[i]
        (xb,yb)=bottomShapes[i]
        xFalling.append(xf)
        xBottom.append(xb)
    return xFalling==xBottom

def newFallingShapes(canvas):
    # geneerate new falling shapess
    # we should use copy.copy
    bottomShapes=copy.copy(canvas.data.bottomShapes)
    random.shuffle(bottomShapes)
    newShapes=bottomShapes
    for index in xrange(len(newShapes)):
        (cx,cy)=newShapes[index]
        newShapes[index]=(cx,canvas.data.r)
    canvas.data.newFallingShapes=newShapes
   
def invaTimerFired(canvas):
    #newFallingShapes(canvas)
    if(canvas.data.isGameOver==False):
        moveFallingShapes(canvas)
        # check if it has already get to the bottom
        fallingShapes=canvas.data.newFallingShapes
        bottomShapes=canvas.data.bottomShapes
        (cx,cy)  =fallingShapes[0]
        (cx0,cy0)=bottomShapes[0]
        # when go to the bottom, starNumber should -1
        # we should check when the fallingshapes reaches the bottom
        if cy==cy0:
            if not checkMatch(canvas):
                canvas.data.starNumber-=1
            # check whether the game ends
            if (canvas.data.starNumber <0 or 
                canvas.data.starNumber==canvas.data.winStarNumber):
                canvas.data.isGameOver=True
            else:
                newFallingShapes(canvas)
        invaRedrawAll(canvas)
    #whether or not game is over, call next timerFired
    # we should decrease the speed if we need the game to be easier
    delay = 100+150/(2+canvas.data.starNumber) # milliseconds
    def f():
        invaTimerFired(canvas)
    canvas.after(delay, f) # pause, then call timerFired again

def invaRedrawAll(canvas):
    canvas.delete(ALL)
    drawBottonShapes(canvas)
    drawFallingShapes(canvas)
    drawStars(canvas)
    #in redrawAll, you can draw the present game information
    # I use starNumber to denote the game states: the starNumber denote the 
    # the number that se find match times
    cx = canvas.data.canvasWidth/2
    cy = canvas.data.canvasHeight/2
    if canvas.data.isGameOver==True:
        if canvas.data.starNumber==canvas.data.winStarNumber:
            canvas.create_text(cx,cy,text="YOU WIN",font=("Helvetica",32,"bold"))
        if canvas.data.starNumber==-1:
            canvas.create_text(cx,cy,text="YOU LOSE",font=("Helvetica",32,"bold"))

def drawBottonShapes(canvas):
    # draw the botton shapes at the bottom
    shapeLocations=canvas.data.bottomShapes
    shapeColors=canvas.data.shapeColors 
    selectedShape=canvas.data.selectedShape
    for i in xrange(len(shapeLocations)):
        if i == selectedShape:
            color="red"
        else:
            color = shapeColors[i+1]
        (cx,cy)= shapeLocations[i]

        drawShape(canvas,cx,cy,i,color)

# directly draw the shapes
def drawShape(canvas,cx,cy,n,fillColor):
    r=canvas.data.r
    (x0,y0,x1,y1)=(cx-r,cy-r,cx+r,cy+r)
    if n==0:
        #to do drawTriangle(x0,y0,x1,y1)  accroding to the input
        canvas.create_polygon([((x0+x1)/2,y0),(x0,y1),(x1,y1)],fill=fillColor)
    elif n==1:
        #to do drawSquare(x0,y0,x1,y1) according to the input
        canvas.create_polygon([(x0,y0),(x0,y1),(x1,y1),(x1,y0)],fill=fillColor)
    elif n==2:
        #to do drawPentagram(x0,y0,x1,y1)according to the input
        parameterx=0.5
        #parametery=0.82
        canvas.create_polygon([(cx-r,cy),(cx,cy-r),(cx+r,cy),(cx+parameterx*r,y1),(cx-parameterx*r,y1)],fill=fillColor)
    elif n==3:
        #to do drawHexagon(x0,y0,x1,y1) according to the input
        parameterx=0.5
        canvas.create_polygon([(x0+parameterx*r,y0),(x1-parameterx*r,y0),(x1,cy),(x1-parameterx*r,y1),(x0+parameterx*r,y1),(x0,cy)],fill=fillColor)
    else:
        canvas.create_oval(x0,y0,x1,y1,fill=fillColor)

def drawFallingShapes(canvas):
    fallingShapes=canvas.data.newFallingShapes
    shapeColors=canvas.data.shapeColors
    for i in xrange(len(fallingShapes)):
        color = shapeColors[i+1]
        (cx,cy)= fallingShapes[i]
        drawShape(canvas,cx,cy,i,color)


def drawStars(canvas):
    # draw the star on the left 2 cells
    cellNumber=5
    (x0,y0,x1,y1)=(0,0,canvas.data.cellWidth*2,canvas.data.cellHeight)
    starCellSize=(x1-y1)/cellNumber
    starCenter=[]
    for i in xrange(cellNumber):
        starCenter.append((starCellSize/2+i*starCellSize,starCellSize))
    r=canvas.data.r
    counter=canvas.data.starNumber
    for (cx,cy)in starCenter:
        # draw the star's background
        drawStar(canvas,cx,cy,None,r/2,cellNumber,"black")
        if counter >0:
            drawStar(canvas,cx,cy,None,r/2-2,cellNumber,"yellow")
            counter-=1
        else:
            # draw the inner white thus it will look transparent
            drawStar(canvas,cx,cy,None,r/2-2,cellNumber,"white")

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

def invaInit(canvas):
    invaInitBoard(canvas)
    invaInitVirables(canvas)
    newFallingShapes(canvas)
    invaRedrawAll(canvas)


def invaInitBoard(canvas):
    canvas.data.cellNumber=7
    cellNumber=canvas.data.cellNumber
    canvas.data.cellWidth=canvas.data.canvasWidth/canvas.data.cellNumber
    cellWidth=canvas.data.cellWidth
    cellHeight=canvas.data.canvasHeight/canvas.data.cellNumber
    canvas.data.cellHeight=cellHeight
    # initialize the cell colors 
    canvas.data.shapeColors=["red","yellow","green","blue","purple","brown"]
    shapes=[]
    # generate different tuples to store the location of the shapse
    # everytime, we draw the first triangle ....but the location changes
    for e in xrange(canvas.data.cellNumber-2):
        print e
        shapes.append(((cellWidth/2)+(e+2)*cellWidth,cellHeight*(cellNumber-1)))
    canvas.data.bottomShapes=shapes

def invaInitVirables(canvas):   
    canvas.data.r=canvas.data.cellWidth/2/2
    # use this to denote the selected shape
    canvas.data.previous=None
    canvas.data.selectedShape=None
    # use this to denote the  match times 
    canvas.data.starNumber=0
    canvas.data.mouseClickCounter=0
    canvas.data.winStarNumber=5
    canvas.data.isGameOver=False




########### copy-paste below here ###########

def runInvasion(width,height):
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    canvas.data.canvasWidth=width
    canvas.data.canvasHeight=height
    invaInit(canvas)
    # set up events
    root.bind("<Button-1>", lambda event:invaMousePressed
        (event,canvas))
    root.bind("<Key>",lambda event: invaKeyPressed(event,canvas))
    invaTimerFired(canvas)
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)



####--------------------------------------------------------------------####



###-------test----------functions--------------------------------------####

def testRemoveFullRow():
    testFirst()
    testSecond()
    testThird()

def testFirst():
    root = Tk()
    canvasTest=Canvas(root,width=300,height=200)
    canvasTest.pack()
    root.canvasTest=canvasTest.canvasTest=canvasTest

    class Struct:pass
    canvasTest.data=Struct()
    canvasTest.data.rows=2
    canvasTest.data.cols=3
    canvasTest.data.score=0
    canvasTest.data.margin=30
    canvasTest.data.cellSize=30
    canvasTest.data.board=[["blue","blue","blue"],["red","red","red"]]
    removeFullRow(canvasTest)
    tetriseDrawBoard(canvasTest)
    root.mainloop()
    print "if we see all blue we passed the test "

def testSecond():    
    rootAgain=Tk()
    canvasTest=Canvas(rootAgain,width=300,height=200)
    canvasTest.pack()
    rootAgain.canvasTest=canvasTest.canvasTest=canvasTest
    class Struct:pass
    canvasTest.data=Struct()
    canvasTest.data.rows=3
    canvasTest.data.cols=3
    canvasTest.data.score=0
    canvasTest.data.margin=30
    canvasTest.data.cellSize=30
    canvasTest.data.board=[["blue","blue","blue"],["red","red","blue"],["red","red","red"]]
    removeFullRow(canvasTest)
    tetriseDrawBoard(canvasTest)
    rootAgain.mainloop()
    print "if we see 2 line blue and 1line red we passed the test"

def testThird():
    rootThird=Tk()
    canvasTest=Canvas(rootThird,width=300,height=200)
    canvasTest.pack()
    rootThird.canvasTest=canvasTest.canvasTest=canvasTest
    class Struct:pass
    canvasTest.data=Struct()
    canvasTest.data.rows=4
    canvasTest.data.cols=3
    canvasTest.data.score=0
    canvasTest.data.margin=30
    canvasTest.data.cellSize=30
    canvasTest.data.board=[["blue","blue","blue"],["red","red","blue"],["red","red","red"],["red","blue","red"]]
    removeFullRow(canvasTest)
    tetriseDrawBoard(canvasTest)
    rootThird.mainloop()
    print "if we see 2 line blue and 2line red we passed the test"

def testRotateFallingPiece():
    pass


def testAll():
    testRotateFallingPiece()
    #testRemoveFullRow()    


def main():
    testAll()


if __name__=="__main__":
    main()




snakeRun(8,16)
runtetrises(15,10)
runInvasion(1000,800)
