def wordSearch(board,word):
    (rows, cols)=(len(board),len(board[0]))
    for row in xrange(rows):
        for col in xrange(cols):
            result=searchFromCell(board,word,row,col)
            if result!=None:
                return result
    return None

def searchFromCell(board,word,startRow,startCol):
    (rows,cols)=(len(board),len(board[0]))
    for dir in xrange(8):
        result=searchFromDiriction(board,word,startRow,startCol,dir)
        if result!=None:
            return result
    return None

def searchFromDiriction(board,word,startRow,startCol,dir):
    (rows,cols)=(len(board),len(board[0]))
    dirs=[(-1,-1),(-1,0),(-1,+1),\
          (0,-1),         (0,1),\
          (1,-1),(1,0),(1,1)]
    dirNames=["left-up","up","right-up",\
                "left",       "right",\
                "left-down","down","right-down"]
    (drow,dcol)=dirs[dir]
    print(drow,dcol,startRow,startCol)
    for i in xrange(len(word)):
        row= startRow+i*drow
        col= startCol+i*dcol
        print ("direction",row,col,dir)
        if ((row>=rows) or (col>=cols) or(row<0) or(col<0) or (board[row][col]!=word[i])):
            return None
    return (word,(startRow,startCol),dirNames[dir])


def testWordSearch():
    board = [ [ 'd', 'o', 'g' ],
              [ 't', 'a', 'c' ],
              [ 'o', 'a', 't' ],
              [ 'u', 'r', 'k' ],
            ]
  #  print wordSearch(board, "dog") # True
   # print wordSearch(board, "cat") # True
    #print wordSearch(board, "tad") # True
    print wordSearch(board, "cow") # False

testWordSearch()