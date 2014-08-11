# connect4.py
# This code was developed in recitation on Fri 7-Oct-2011.
# As such, it may not contain perfect style, and may
# even contain a small bug here or there (usual disclaimer).

# A simple game of connect4 with a text interface
# based on the wordSearch code written in class.

def playConnect4():
    rows = 6
    cols = 7
    puzzle = makePuzzle(rows, cols)
    player = "X"
    moveCount = 0
    printPuzzle(puzzle)
    while (moveCount < rows*cols):
        moveCol = getMoveCol(puzzle, player)
        moveRow = getMoveRow(puzzle, moveCol)
        puzzle[moveRow][moveCol] = player
        printPuzzle(puzzle)
        if checkForWin(puzzle, player):
            print "*** Player %s Wins!!! ***" % player
            return
        moveCount += 1
        player = "O" if (player == "X") else "X"
    print "*** Tie Game!!! ***"

def makePuzzle(rows, cols):
    return [ (["-"] * cols) for row in xrange(rows) ]

def printPuzzle(puzzle):
    # replace the wordSearch version with this one, better-suited for connect4
    rows = len(puzzle)
    cols = len(puzzle[0])
    print
    # first print the column headers
    print "   ",
    for col in xrange(cols):
        print str(col+1).center(3),
    print
    # now print the board
    for row in range(rows):
        print "   ",
        for col in xrange(cols):
            print puzzle[row][col].center(3),
        print

def getMoveCol(puzzle, player):
    cols = len(puzzle[0])
    while True:
        response = raw_input("Enter player %s's move (column number) --> " %
                             (player))
        try:
            moveCol = int(response)-1  # -1 since user sees cols starting at 1
            if ((moveCol < 0) or (moveCol >= cols)):
                print ("Columns must be between 1 and %d." % (cols)),
            elif (puzzle[0][moveCol] != "-"):
                print "That column is full!",
            else:
                return moveCol
        except:
            # they did not even enter an integer!
            print "Columns must be integer values!",
        print "Please try again."

def getMoveRow(puzzle, moveCol):
    # find first open row from bottom
    rows = len(puzzle)
    for moveRow in xrange(rows-1, -1, -1):
        if (puzzle[moveRow][moveCol] == "-"):
            return moveRow
    # should never get here!
    assert(False)

def checkForWin(puzzle, player):
    winningWord = player * 4
    return (wordSearch(puzzle, winningWord) != None) # that was easy!

##############################################
# taken from wordSearch.py
##############################################

# wordSearch.py
# This code was developed in class on Tue 4-Oct-2011.
# As such, it may not contain perfect style, and may
# even contain a small bug here or there (usual disclaimer).

def wordSearch(puzzle, word):
    rows = len(puzzle)
    cols = len(puzzle[0])
    for startRow in xrange(rows):
        for startCol in xrange(cols):
            solution = wordSearch1(puzzle, word, startRow, startCol)
            if (solution != None):
                return solution
    return None

def wordSearch1(puzzle, word, startRow, startCol):
    rows = len(puzzle)
    cols = len(puzzle[0])
    for drow in xrange(-1,2):
        for dcol in xrange(-1, 2):
            if ((drow != 0) or (dcol != 0)):
                solution = wordSearch2(puzzle, word, startRow, startCol,
                                       drow, dcol)
                if (solution != None):
                    return solution
    return None

def wordSearch2(puzzle, word, startRow, startCol, drow, dcol):
    rows = len(puzzle)
    cols = len(puzzle[0])
    for i in xrange(len(word)):
        cWord = word[i]
        puzzleRow = startRow+i*drow
        puzzleCol = startCol+i*dcol
        if ((puzzleRow < 0) or (puzzleRow >= rows) or
            (puzzleCol < 0) or (puzzleCol >= cols)):
            return None
        cPuzzle = puzzle[puzzleRow][puzzleCol]
        if (cWord != cPuzzle):
            return None
    # found it!
    return (startRow, startCol, (drow, dcol))

playConnect4()