from Tkinter import *
# Animation.py

import random
import math


###########################################
# Animation class
###########################################

class Animation(object):
    # Override these methods when creating your own animation
    def mousePressed(self, event): pass
    def keyPressed(self, event): pass
    def timerFired(self): pass
    def init(self): pass
    def redrawAll(self): pass
    
    # Call app.run(width,height) to get your app started
    def run(self, width=300, height=300):
        # create the root and the canvas
        root = Tk()
        self.width = width
        self.height = height
        self.canvas = Canvas(root, width=width, height=height)
        self.canvas.pack()
        # set up events
        def redrawAllWrapper():
            self.canvas.delete(ALL)
            self.redrawAll()
        def mousePressedWrapper(event):
            self.mousePressed(event)
            redrawAllWrapper()
        def keyPressedWrapper(event):
            self.keyPressed(event)
            redrawAllWrapper()
        root.bind("<Button-1>", mousePressedWrapper)
        root.bind("<Key>", keyPressedWrapper)
        # set up timerFired events
        self.timerFiredDelay = 250 # milliseconds
        def timerFiredWrapper():
            self.timerFired()
            redrawAllWrapper()
            # pause, then call timerFired again
            self.canvas.after(self.timerFiredDelay, timerFiredWrapper)
        # init and get timerFired running
        self.init()
        timerFiredWrapper()
        # and launch the app
        root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)
###--------------------------------------------------------------####
###########################################
# Utility functions
###########################################
# if u get stuck at the place when adding line u should go to see the comment
def make2dList(rows, cols):
    a=[]
    for row in xrange(rows): a += [[0]*cols]
    return a


class DotAndBox(Animation):
    def __init__(self,rows,cols,maxSecondsPerTurn=0):
        self.rows=rows
        self.cols=cols
        self.maxSecondsPerTurn=maxSecondsPerTurn
        
    # init all the virables
    def init(self):
        self.makeDotAndBoxBoard()
        self.legalMove=[]
        self.linesBug=set()
        self.presentPlayer=1
        # see this kind of the 
        self.selectedDots=None
        self.isGameOver=False
    # create the  total DotAndBoxBoard and help to draw the dots   
    def makeDotAndBoxBoard(self):
        self.cellSize=500/(self.rows)
        self.boardMargin=100
        self.dotRadius=10
        self.titleMargin=10
        self.firstClickRow=None
        self.firstClickCol=None
        self.leagleMoves=[]
        self.clickcounter=0
        self.isDotSelcted=False
        self.selectedLine=[]
        self.scorePlayers=[0,0]
        self.timeCounter=0
        self.flashCount=0
        rows,cols=self.rows,self.cols
        # create a box to store the things in the box
        a=[]
        for row in xrange(rows-1):a+=[[0]*(cols-1)]
        self.wholeBoxes=a
        # create a board that will store all the 
        a=[]
        for row in xrange(rows):a+=[[0,0]*cols]
        board=a
        for row in xrange(rows):
            for col in xrange(cols):
                cx= self.boardMargin+self.cellSize*col
                cy= self.boardMargin+self.titleMargin+self.cellSize*row
                board[row][col]=(cx,cy)
        self.board=board
   
    def mousePressed(self,event):
        if(self.isOnBoard(event.x,event.y)):
            x,y=event.x,event.y
            # find the dot that is clicked
            for row in xrange(self.rows):
                for col in xrange(self.cols):
                    dotX,dotY=self.board[row][col]
                    distance = math.sqrt(abs(dotX-x)**2+abs(dotY-y)**2)
                    if distance<=self.dotRadius*2:
                        # get the row and col of the dot that is clicked
                       self.firstClickRow,self.firstClickCol=row,col
           # if we find the dot that is clicked call dotPressFunction
            if (self.firstClickCol!=None and self.firstClickRow!=None):
                self.dotPress(self.firstClickRow,self.firstClickCol)

    # first time you press the dot and you will  show the possible legal 
    #  move of the next dot
    def dotPress(self,row,col):
        # record the dot that is used before and then go to link the
        # check there isn't a dot clicked so we store the row and col in
        # the self.selectedDots
        if self.isDotSelcted==False:
            self.selectedDots=(row,col)
            self.isDotSelcted=True
            # get all the is the leagle move of the chosen dot
            self.flagLeagleMove(row,col)
        else:
            # if there already has a selected dot 
            (startRow,startCol)=self.selectedDots
            # everytime you should check the validation of the second circled
            # dot, if it is in the leagleMoves you add the line in the linebug
            #but if it is not in the leaglMoves you should clean the selected 
            #dot and then start a new select dot
            if list((row,col))in self.leagleMoves:
                self.linesBug.add((startRow,startCol,row,col))
                self.linesBug.add((row,col,startRow,startCol))
                # everytime after you add a line you should check whether it has formed a box
                self.checkBoxes()
                self.checkGameOver()
                # every time you add a line you change a player
                self.changePlayer()
            # every time after click the second time, just start a nother turn
            self.selectedDots=[]
            self.isDotSelcted=False
    # when all boxes are closed that is game over
    def checkGameOver(self):
        (rows,cols)=(self.rows-1,self.cols-1)
        for row in xrange(rows):
            for col in xrange(cols):
                if self.wholeBoxes[row][col]==0:
                    self.isGameOver=False
                    return
        self.isGameOver=True
    # check whether the box belongs to one player
    def checkBoxes(self):
        box=self.wholeBoxes
        (rows,cols)=(self.rows-1,self.cols-1)
        hasBoxesClosed=False
        for row in xrange(rows):
            for col in xrange(cols):
                # get the 4 points of the box
                leftUpPoint=(row,col)
                rightUpPoint=(row,col+1)
                leftBottomPoint=(row+1,col)
                rightBottomPoint=(row+1,col+1)
                if self.wholeBoxes[row][col]==0:
                    if self.closedBox(leftUpPoint,rightUpPoint,leftBottomPoint,rightBottomPoint):
                        self.wholeBoxes[row][col]=self.presentPlayer
                        self.scorePlayers[self.presentPlayer-1]+=1
                        hasBoxesClosed=True
        if hasBoxesClosed:
            #change the player for one more time so we go back to the present player
            self.changePlayer()
            #self.timeCounter=0



    def closedBox(self,leftUpPoint,rightUpPoint,leftBottomPoint,rightBottomPoint):
        # check the four lines according to their 4 points
        lines=[]
        lines.append(list((leftUpPoint,rightUpPoint)))
        lines.append(list((rightUpPoint,rightBottomPoint)))
        lines.append(list((rightBottomPoint,leftBottomPoint)))
        lines.append(list((leftBottomPoint,leftUpPoint)))
        for e in lines:
            if sum(tuple(e),()) not in self.linesBug:
                return False
        return True

    def changePlayer(self):
        self.presentPlayer+=1
        if self.presentPlayer>2:
            self.presentPlayer=1
        #everytime you change a player u should reset the timeCounter
        self.timeCounter=0
        

    # helper function to get all possible leagleMove according to the input 
    # row and col
    def flagLeagleMove(self,row,col):
        self.leagleMoves=[]
        dirs = [  (-1, 0),( 0, -1), ( 0, +1), (+1, 0) ]
        for (drow,dcol) in dirs:
            tryRow,tryCol=drow+row,dcol+col
            if(tryRow >=0 and tryCol>=0 and tryRow<self.rows and tryCol<self.cols):
                if (row,col,tryRow,tryCol)not in self.linesBug:
                    self.leagleMoves.append([tryRow,tryCol])

   #helper function to check if it is on the board

    def isOnBoard(self,x,y):
        (boardX0, boardY0, boardX1, boardY1) = self.getBoardBounds()
        return ((x >= boardX0) and (x <= boardX1) and
                (y >= boardY0) and (y <= boardY1))

    # helper function to get the board bounds and check   
    def getBoardBounds(self):
        boardX0 = self.boardMargin
        boardX1 = self.width - self.boardMargin
        boardY0 = self.titleMargin + self.boardMargin
        boardY1 = self.height - self.boardMargin
        return (boardX0, boardY0, boardX1, boardY1)

    def keyPressed(self,event):
        if (event.char=="r"):
            self.init()
    
    def timerFired(self):
        if not self.isGameOver:
            self.timeCounter+=1
            millisecondsTrans=1000
            if self.timeCounter*self.timerFiredDelay>self.maxSecondsPerTurn*1000:
                self.flashCount+=1
                # every time flash 
                if self.flashCount>10:
                    self.flashCount=0
                    self.changePlayer()
    
    def redrawAll(self):
        if not self.isGameOver:
            self.drawBoard()
            self.drawLeagleMove()
            self.drawLine()
            self.drawPlayer()
            self.drawBoxes()
            self.drawScore()
            self.drawWarning()
        else:
            score1,score2=(self.scorePlayers)
            if score1!=score2:
                if score1>score2:
                    winner=1
                elif score1<score2:
                    winner=2
                error="GAME OVER press R to restart the winner is "+str(winner)
            else:
                error="GAME OVER press R to restart the game Tie"
            self.canvas.create_text(self.cellSize*self.rows/2,self.cellSize*self.cols/2,text=error,fill="red")
        pass

    def drawWarning(self):
        if self.flashCount%2>0:
            error="PLEASE QUICK"
            self.canvas.create_rectangle(0,0,self.width,self.height,fill="white")
            self.canvas.create_text(self.cellSize*self.rows/2,self.cellSize*self.cols/2,text=error,fill="red")

    def drawBoxes(self):
        (rows,cols)=(self.rows-1,self.cols-1)
        for row in xrange(rows):
            for col in xrange(cols):
                # get the 4 points of the box
                positionx,positiony=self.board[row][col]
                cellSize=self.cellSize
                self.canvas.create_text(positionx+cellSize/2,positiony+cellSize/2,text=self.wholeBoxes[row][col])

    
    # draw the score according to the playsers
    def drawScore(self):
        showMessage="the socre of Player1 and Player2 is "+str(self.scorePlayers)
        self.canvas.create_text(self.boardMargin*2,self.boardMargin/2,anchor=SW,text=showMessage)


    #print the player information    
    def drawPlayer(self):
        present="present Player"+str(self.presentPlayer)
        self.canvas.create_text(self.boardMargin/2,self.boardMargin/2,text=present)


    def drawLine(self):
        if self.isDotSelcted:
            self.canvas.create_text(self.boardMargin*5,self.boardMargin,text="select another dot to add a line")
        for (sr,sc,er,ec) in self.linesBug:
            (sx,sy)=self.board[sr][sc]
            (ex,ey)=self.board[er][ec]
            self.canvas.create_line(sx,sy,ex,ey)

    def drawLeagleMove(self):
        r=self.dotRadius
        leagleMoves=self.leagleMoves
        if len(leagleMoves)>0:
            for (row,col) in self.leagleMoves:
                (cx,cy)=self.board[row][col]
                self.canvas.create_oval(cx-r,cy-r,cx+r,cy+r,fill="yellow")
    def drawBoard(self):
        r=self.dotRadius
        for row in xrange(self.rows):
            for col in xrange(self.cols):
                (cx,cy)=self.board[row][col]
                self.canvas.create_oval(cx-r,cy-r,cx+r,cy+r,fill="black")


def runDotAndBOx(rows,cols,maxSecondsPerTurn=10):
    game=DotAndBox(rows,cols,maxSecondsPerTurn)
    game.run(600,600)

runDotAndBOx(3,3)