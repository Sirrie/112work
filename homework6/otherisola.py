def make2dList(rows,cols):
    a =[]
    for row in xrange(rows): a+=[[0]*cols]
    return a
    # make a 2dList with all inital value of 0

def getMove(board,player):
    #print the board first
    print "\n*******************"
    printBoard(board)
    while True:
        prompt = "Enter mover for player"+ getPlayerLabel(player) +":"
        move = raw_input(prompt).upper()
        if((len(move)!=2) or (not move[0].isalpha())
           or (not move[1].isdigit())):
            print "Sorry,you should enter something like A2 or d3 to move"
        else:
            col = ord(move[0])-ord("A")
            row = int(move[1])-1 
            # get the real position in the board 2dlist
            if (not isLegalMove(board,player,row,col)):
                print "You can't move here, try again."
            else:
                return (row,col)

def isLegalMove(board,player,row,col):
    (rows,cols)=(len(board),len(board[0]))
    if not(0<=row<rows and 0<=col<cols): return False
    if board[row][col]!= 0: return False
    return hasMoveFromCell(board,player,row,col)

def hasMove(board,player):
    #check if has move
    (rows,cols)=(len(board),len(board[0]))
    for row in xrange(rows):
        for col in xrange(cols):
            if hasMoveFromCell(board,player,row,col):
                return True
    return False

def hasMoveFromCell(board,player,row,col):
    # check if is adjasent to the player
    for dir in xrange(8):
        if (hasMoveFromCellInDirection(board,player,row,col,dir)):
            return True
    return False

def hasMoveFromCellInDirection(board,player,row,col,dir):
    (rows,cols)=(len(board),len(board[0]))
    dirs =[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    rowd = row+dirs[dir][0]
    cold = col+dirs[dir][1]
    if((0<=rowd<rows and 0<=cold<cols) and (board[rowd][cold]==player)
      and (board[row][col]==0)):
        return True #find it!
    return False
       
def makeMove(board,player,row,col):
    (rows,cols)=(len(board),len(board[0]))
    for dir in xrange(8):
        if(hasMoveFromCellInDirection(board,player,row,col,dir)):
            makeMoveInDirection(board,player,row,col,dir)
            return 
    return

def makeMoveInDirection(board,player,row,col,dir):
    (rows,cols)=(len(board),len(board[0]))
    board[row][col] = player
    dirs =[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    row0 = row +dirs[dir][0]
    col0 = col+ dirs[dir][1]
    if((0<=row0<rows and 0<=col0<cols) and (board[row0][col0]==player)):
        if (row0==0 or row0==rows-1) and (col0==cols/2):
            board[row0][col0] = 3 #check if it's the initial point
        else: board[row0][col0] = 0
        return 
    return 

def printBoard(board):
    (rows,cols)=(len(board),len(board[0]))
    printColLabels(board)
    for row in xrange(rows):
        print "%2d"%(row+1),
        for col in xrange(cols):
            print getPlayerLabel(board[row][col]),
        print "%2d"%(row+1)
    printColLabels(board)

def printColLabels(board):
    (rows,cols)=(len(board),len(board[0]))
    print "  ",
    for col in xrange(cols):print chr(ord("A")+col),
    print

def getPlayerLabel(player):
    labels = ["-","X","O","#"]
    return labels[player]

def getFlip(board):
    print "\n*******************"
    printBoard(board)

    while True:
        prompt = "Enter flip position:"
        move = raw_input(prompt).upper()
        if((len(move)!=2) or (not move[0].isalpha())
           or (not move[1].isdigit())):
            print "Sorry,you should enter something like A2 or d3 to move"
        else:
            col = ord(move[0])-ord("A")
            row = int(move[1])-1 
            # get the real position in the board 2dlist
            if (not isLegalFlip(board,row,col)):
                print "You can't flip here, try again."
            else:
                return (row,col)

def isLegalFlip(board,row,col):
    (rows,cols)=(len(board),len(board[0]))
    if (0<=row<rows and 0<=col<cols and board[row][col]==0):
        return True
    return False



def makeFlip(board,rowx,colx):
    board[rowx][colx] = 3
    return 
    

def playIsola():
    #create the intial board
    board=make2dList(7,7)
    board[0][3] = 1
    board[6][3] = 2
    #initial the position
    (currentPlayer,otherPlayer) = (1,2)
    # play the game untill it's over
    while True:
        #over condition
        if ((hasMove(board,currentPlayer)==False) 
            and(hasMove(board,otherPlayer)==False)):
            print "Well, its a tie"
            break
        elif((hasMove(board,currentPlayer)==True)
             and(hasMove(board,otherPlayer)==False)):
            print("So you give up and Player " +
                  getPlayerLabel(currentPlayer)+" wins!")
            break
        elif((hasMove(board,currentPlayer)==False)
             and(hasMove(board,otherPlayer)==True)):
            print ("Player " +getPlayerLabel(currentPlayer)+" wins!")
            break
        else:
            (row,col)=getMove(board,currentPlayer)
            makeMove(board,currentPlayer,row,col)
            # and there must still somewhere to flip
            (rowx,colx)=getFlip(board)
            makeFlip(board,rowx,colx)
            (currentPlayer,otherPlayer)=(otherPlayer,currentPlayer)
            #switch the player
            #print "Switch Player"
    print "Goodbye~"