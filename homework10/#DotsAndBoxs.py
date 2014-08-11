#DotsAndBoxs.py

#oop game

from Tkinter import *
# Animation.py

import random


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

def make2dList(rows, cols):
    a=[]
    for row in xrange(rows): a += [[0]*cols]
    return a

###########################################
# BoardGame class
###########################################

class BoardGame(Animation):
    def getCurrentPlayer(self):
        return self.currentPlayer

    def changeePlayers(self):
        self.currentPlayer += 1
        if (self.currentPlayer > self.totalPlayers):
            self.currentPlayer = 1
    
    def cellPressed(self, row, col):
        print "cell pressed: (%d, %d)" % (row, col)
       # self.board[row][col] = self.getCurrentPlayer()
        dotState=3
        self.board[row][col]=dotState # set it tobe dot
        self.changePlayers()

    def mousePressed(self, event):
        if (self.isOnBoard(event.x, event.y)):
            (row, col) = self.getCellFromLocation(event.x, event.y)
            self.cellPressed(row, col)

    def redrawAll(self):
        self.drawTitle()
        self.drawPlayersTurn()
        self.drawBoard()

    def drawTitle(self):
        self.canvas.create_text(self.width/2, self.titleMargin/2, text=self.title, font=self.titleFont, fill=self.titleFill)
        self.canvas.create_line(0, self.titleMargin, self.width, self.titleMargin, fill=self.titleFill)

    def drawPlayersTurn(self):
        msg = "Player %d's turn" % self.currentPlayer
        self.canvas.create_text(self.boardMargin, self.titleMargin/2, text=msg, font=self.playersTurnFont, anchor=W)

    def drawBoard(self):
        for row in xrange(self.rows):
            for col in xrange(self.cols):
                self.drawCell(row, col)

    def drawCell(self, row, col):
        (x0, y0, x1, y1) = self.getCellBounds(row, col)
        self.canvas.create_rectangle(x0, y0, x1, y1, fill=self.cellBorderColor)
        content = self.board[row][col]
        #self.canvas.create_text((x0+x1)/2,(y0+y1)/2,text=content)                
        self.drawCellContents(row, col, self.getCellContentsBounds(row, col))
        self.canvas.create_text((x0+x1)/2,(y0+y1)/2,text=content)

    def drawCellContents(self, row, col, bounds):
        (x0, y0, x1, y1) = bounds
        self.canvas.create_rectangle(x0, y0, x1, y1, fill=self.cellBackgroundColor)
        color = self.getCellColor(row, col)
        if (color != None):
            if (self.fillCellsWithCircles == True):
                (cx, cy) = ((x0+x1)/2, (y0+y1)/2)
               # print (cx,cy,row,col,self.board[row][col])
                r = int(0.4*self.cellSize)
                self.canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill=color)
            else:
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)

    def getCellColor(self, row, col):
        value = self.board[row][col]
        if (type(value) == str):
            # string values should be color names, like "blue", etc...
            return value
        elif (type(value) == int):
            assert(-2 < value < len(self.cellColors))
            return self.cellColors[value]
        else:
            raise Exception("Unknown board value: %r" % value)        

    def isOnBoard(self, x, y):
        (boardX0, boardY0, boardX1, boardY1) = self.getBoardBounds()
        return ((x >= boardX0) and (x <= boardX1) and
                (y >= boardY0) and (y <= boardY1))

    def getCellFromLocation(self, x, y):
        (boardX0, boardY0, boardX1, boardY1) = self.getBoardBounds()
        row = (y - boardY0) / self.cellSize
        col = (x - boardX0) / self.cellSize
        return (row, col)
        
    def getBoardBounds(self):
        boardX0 = self.boardMargin
        boardX1 = self.width - self.boardMargin
        boardY0 = self.titleMargin + self.boardMargin
        boardY1 = self.height - self.boardMargin
        return (boardX0, boardY0, boardX1, boardY1)

    def getCellBounds(self, row, col):
        (boardX0, boardY0, boardX1, boardY1) = self.getBoardBounds()
        cellX0 = boardX0 + col*self.cellSize
        cellX1 = cellX0 + self.cellSize
        cellY0 = boardY0 + row*self.cellSize
        cellY1 = cellY0 + self.cellSize
        return (cellX0, cellY0, cellX1, cellY1)

    def getCellContentsBounds(self, row, col):
        (cellX0, cellY0, cellX1, cellY1) = self.getCellBounds(row, col)
        cm = self.cellMargin
        return (cellX0+cm, cellY0+cm, cellX1-cm, cellY1-cm)
 
    def __init__(self, title, rows, cols, cellSize=30):
        self.title = title
        self.rows = rows
        self.cols = cols
        self.cellSize = cellSize
        self.titleFont = "Arial 14 bold"
        self.playersTurnFont = "Arial 10"
        self.titleMargin = 40
        self.titleFill = "blue"
        self.boardMargin = 10
        self.cellMargin = 0
        self.board = make2dList(rows, cols)
        self.cellBorderColor = "black"
        self.cellBackgroundColor = "green"
        self.cellColors = [None, "black", "white"]
        self.fillCellsWithCircles = True
        self.totalPlayers = 2
        self.currentPlayer = 1

    def run(self):
        width = self.cols*self.cellSize + 2*self.boardMargin
        height = (self.rows * self.cellSize) + self.titleMargin + 2*self.boardMargin
        super(BoardGame, self).run(width, height)

class DotAndBox(BoardGame):
    def __init__(self,rows,cols,maxSecondsPerTurn):
        title="DotAndBox"
        super(DotAndBox,self).__init__(title,(2*rows+1),(2*cols+1),50)

    def keyPressed(self,event):
        if (event.char=='r'):
            print "hhhhhhhh"
            self.init()

    def drawPlayersTurn(self):
        # copied from Othello...  Maybe this belongs in BoardGame?
        msg = "Player:"
        self.canvas.create_text(self.boardMargin, self.titleMargin/2, text=msg, font=self.playersTurnFont, anchor=W)
        r = self.boardMargin
        cx = self.boardMargin+60 # magic number...
        cy = self.titleMargin/2
        color = self.cellColors[self.currentPlayer]
        self.canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill=color)

    def redrawAll(self):
        super(DotAndBox, self).redrawAll()
        if (self.errMsg != None):
            self.canvas.create_text(self.width/2, self.height/2, text=self.errMsg,font=self.errFont, fill=self.errColor)

    # def cellPressed(self, row, col):
    #     self.errMsg = None
    #     #first we should do the self.press part of it
    #     if (self.selection != None):
    #         if(self.board[row][col]==0):
    #             self.selection=(row,col)
    #         else:
    #             self.errMsg = "can't select the place"
    #     else:
    #         print 
    #         (row0,col0)=self.selection
    #         self.board[row][col]=3 # it is chozon

    #         self.selection = None

       # checkBoxWinning(self.board,self.currentPlayer,row,col)

        # us should do changePlayer or not


    def checkBoxWinning(board,currentPlayer,row,col):
        (rows,cols)=(len(board),len(board[0]))
        if (row-1 >=0 and col-1>=0 and row<rows and col<cols and board[row][col]==3 and board[row][col+2]==3 and board[row-1][col+1] and board[row+1][col+1]==3):
            #board[row][col+1]=
            pass


            self.selection = None

    def drawCellContents(self, row, col, bounds):
        if (self.selection == (row,col)):
            self.cellBackgroundColor = self.selectedCellBackgroundColor
        else:
            self.cellBackgroundColor = self.cellBackgroundColors[1+(row+col)%2]
        super(DotAndBox, self).drawCellContents(row, col, bounds)


    def init(self):
        print "hello~"
        #reset the game
        self.board=make2dList(self.rows,self.cols)
        self.Player=1
        for row in xrange(0,self.rows,2):
            for col in xrange(row%2, self.cols, 2):
                self.board[row][col] = 3
        for row in xrange(1,self.rows,2):
            for col in xrange(1,self.cols,2):
                self.board[row][col]= 4
        
        self.selection = None
        self.cellColors = [None, "yellow", "purple","pink","green"]
        self.cellBackgroundColors = [None, "white", "cyan"]
        self.selectedCellBackgroundColor = "green"
        self.errMsg = None
        self.errFont = "Arial 14 bold"
        self.errColor = "red"



def runDotAndBox(rows,cols,maxSecondsPerTurn=0):
    game=DotAndBox(rows,cols,maxSecondsPerTurn)
    game.run()

runDotAndBox(4,4)
