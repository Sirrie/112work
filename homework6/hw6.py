# ChenSiyu + siyuchen --- Section N

######################################################################
# Place your non-autograded solutions below here!
######################################################################
'''
2012 midterm:
  1:
  a: true because when x&y == x|y, then x=y, then x^y=0
  b: false because if x=12, y=2,then 12%2==12>>2=0
  c: false, according to information theory, sorting should atleast take O(nlogn)
  d: false, when there could be some N, such as N =1
  e: true, fact
  f: false, as copy.deepcopy wiill do more things
  g: true,because lists is mutable, so it is unhashable, but set can be added to a list, 
  h: True
  I: False, you can use ancor to set the location of the text
  J: False, experts won't use magic numbers, this will be hard to debug and hard to retrive the code
  

  2: 
    a: if two string have the same letter, but different order they will have the same hashcode
    b: g(A):
        c=copy.deepcopy(A)
        f(c)
        return c
    c: use time function that we can record the time of the different input size and compare the running time results and guess the results.
       say input size as 100, we have the tim t1, we have the input size 1000, we have the t2, if t2/t1=10**3 we can say it is O(n**3)
      def f(n1)  
        start= time.time
        foo(x)
        end = time.time
        return end-start
      so we can use the above function to compute the time and get the compared results.
    d: 
    def f(n):
   (s, count) = (set(), 0)              O(1)
   for c in str(n):                     O(logn)
       if (c not in s): count += 1      O(1)
       s.add(c)                         O(1)
   return count                         total should be O(logn)

   e:sorted(list(T))[len(T)/2]  expresion: 3+5  stattement 3+5==7

  3: 
      1:7 5 t\t
      2:[1,4,5]
      3: [2,1,0,1,2]
      4: 10, 25 becuase len([1,4,1,4])==4, and len([1,4,1,4,1,4])==6 and we always find the sum in relative way
  4: 
    1: x should be 31 and y should be 30, because x-y=3, x^y =0b11, x|y =x=31 
    2: x should be length 5 and has 2 duplicates because the len(set(t))==3, and t[1],t[2]=t[4],t[3], so t could be [0,1,2,2,1]
    3: input could be [0,2,4,1,3,5] 
       as sorted (L)should be [0,1,2,3,4,5], and i loop fron 1,2,3,4,5,ok start from 0, so we find if L is not even, ok will turn to 1, and next odd will not jump into the if statement , first 3 could be even number and the last 3 can be the odd number 
    4:   as count==3, we find there are 3 digits in the list, and val should belarger than 0, and less than len(L), and L[val]=c, guees the digits are 1,2,3. so the input should be 

      [1,b,c,d,2,3]

    5:  as presented L should be 2d List, and rows=2,cols=4, this funciotn will assign the L[row][cols-1-col] backward  rows by rows and i will keep accumulating, so the resutl should be: [[6,4,2,0],[7,5,3,1]]



---------------------------------2013 Quiz5:---------------------------
1:a = [[1],[2]]
(b,c,d) = (a, copy.copy(a), copy.deepcopy(a))
print (a == b), (a == c), (a == d)
print (a is b), (a is c), (a is d)
print (a[0] is b[0]), (a[0] is c[0]), (a[0] is d[0])
 
a = [[1],[2]]
print "A",
try:
    print "B",
    b[0][0] += 10
    c[1][0] += 100
    d[1][1] += 1000
    a[0][0] += 10*1000
    print "C",
except:
    print "D",
print "E"
for L in [a,b,c,d]: print L
 
print "F"
a = [[1],[2]]
(b,c,d) = (a, copy.copy(a), copy.deepcopy(a))
a[0][0] += 1
b[0][0] += 2
c[1][0] += 3
d[1][0] += 4
a[0] = c[0]
b[0] = d[0]
for L in [a,b,c,d]: print L

the printing results are :
True True True
True False False
True True False
A B D E
[[1], [2]]
[[11], [102]]
[[11], [102]]
[[1], [2]]
F
[[1], [5]]
[[1], [5]]
[[4], [5]]
[[1], [6]]




2: reasoning over code:
 a: maximun in L[0] is 2 and L, n is from 0 to n-1, every row the elements number decreases
 so  L can be [[0,1,2],[0,1],[0]]
 b:  in the map we find there are 3 2, 2 3, and 1 0.
  so s1 should be [2,3,0], we find there are 3 2, so there must be 3 in 2, and 2 in 2, so s1 should be [2,0] and s2 should be [2,3]

---------------------------------------f12 hw7b------------------------------

def f1(a):
    n = len(a)
    assert(n == 3)  ----> n should be 3
    b = [([0]*n) for row in xrange(n)]--->b=[[0,0,0],[0,0,0],[0,0,0]]
    for i in xrange(n):
        b[i][i] = i
        b[i][n-1-i] = i+1
    return (b == a)        
  so b should be [[0,0,1],[0,2,0],[3,0,2]], so a should be [[0,0,1],[0,2,0],[3,0,2]]

def f2(a):
    assert ((len(a) == 2) and (len(a[0]) == 3))
    for c in xrange(len(a[0])):
        s = 0
        for r in xrange(len(a)):
            if (r > 0): assert(a[r][c] != a[r-1][c])
            s += a[r][c]
        assert(s == 5)
    return True   
                            
        a=[[2,1,3],[3,4,2]] because all colum sum to 5

def f3(a):
    assert(len(a) * len(a[0]) == 6)
    x = 0
    for r in xrange(3):
        for c in xrange(2):
            if ((r+c) % 2 == 0):
                x = 10*x + (a[r][c] % 10)
            else:
                assert(a[r][c] == 0)
    return (x == 42)
     see len(a)*len(a[0])==6 we can guess that a could be 2*3 or 3*2 matrix
     and then we find every time x should left shif one bit and then add one valuse so, a could be [[0,0],[0,4],[2,0]]

def f4(a):
    (rr,cc,r,c) = (len(a), len(a[0]), 0, 1)
    assert((rr*cc == 15) and (rr>cc>1))
    for i in xrange(rr*cc):
        assert(a[r][c] == i%7)
        if (c == 0): (r,c) = ((r-1)%rr,cc-1)
        else: (r,c) = (r, c-1)
    return True
    we can see  row a * col a ==15, and we find row > col so row is 5 and cols is 3, i is 0 to 14, so we can find that start from a[0][1]=0, for next round we go to a[0][0] which is 1,everytime,  if c==0,we go to the next column, go from right to left so we can guess, a=[[1,0,0],[6,5,4],[3,2,1],[0,6,5],[4,3,2]]


def f5(c):
    # Note that c is a non-rectangular ("ragged") 2d list!
    n = len(c)
    a = [[1]]
    for i in xrange(1,n):
        a.append([1]*(1+len(a[i-1])))
        for j in xrange(1,i):
            a[i][j] = a[i-1][j-1]+a[i-1][j]
    assert(a == c)
    this part is creating Pascal's triangle, so we have something like
            1
           1  1
          1 2  1
         1 3  3  1
        1 4  6 4  1   
      1 5 10 10 5 1

    b = [1]
    for i in xrange(1,n):
        s = 0
        for j in xrange(i):
            if (j < len(a[i-j])):    j in the row a[i-j]
                s += a[i-j][j]
        b.append(s)
    return b[-1] == 8

    in this place we find we need to add the sum of elements in the triangle :
    looping from the index that 
    i     j     i-j 
    1     0     1
    2     0     2
          1     1
    3     0     3
          1     2
          2     1
          it is like trace from the diagonals of the triangle 

    we should find that c should be the same as a, and the last element in b is 8 so we can guess the sum should be 8 we need to find the elements in a line that sum to 8, so we need to go through the diagnals and find 8=1+4+3 and then we get the a should be :
       [[1],
       [1,1],
       [1,2,1],
       [1,3,3,1],
       [1,4,6,4,1],
       [1,5,10,10,5,1]]

'''



######################################################################
# Place your autograde solutions below here
######################################################################

#check whether it is a magic square
def isMagicSquare(twoDlist):
    (rows,cols)=(len(twoDlist),len(twoDlist[0]))
    if rows!=cols:return False
    lineSum=sum(twoDlist[0])
    for row in xrange(rows):
        #if not checkRow to check every row
        if sum(twoDlist[row])!=lineSum:
            return False
    for col in xrange(cols):
       # if not checkCol to check every col
        if sum([columElements[col] for columElements in twoDlist])!=lineSum:
            return False
        # check sum of every diagonals 1 forward, -1 backward
    if not checkDiag(twoDlist,lineSum,1):
        return False
    if not checkDiag(twoDlist,lineSum,-1):
        return False
    return True
# check sum of dialog
def checkDiag(twoDlist,lineSum,dir):
    (rows,cols)=(len(twoDlist),len(twoDlist))
    if rows!=cols:return False
    diagSum=0
    if dir >0:
      for i in xrange(rows):
          row = i*dir
          col = i*dir
          diagSum+=twoDlist[row][col]  
    else:
        for i in xrange(rows):
           row=i
           col=rows-i-1
           diagSum+=twoDlist[row][col]
    return diagSum==lineSum

# serach word with interge inside
def wordSearchWithIntegerWildcards(board,word):
    (rows, cols) = (len(board), len(board[0]))
    for row in xrange(rows):
        for col in xrange(cols):
            result = wordSearchFromCell(board, word, row, col)
            if (result != False):
                return result
    return False
# search word from cell
def wordSearchFromCell(board, word, startRow, startCol):
    for dir in xrange(8):
        result = wordSearchFromCellInDirection(board, word, startRow,\
         startCol, dir)
        if (result != False):
            return result
    return False
#!!!! very important logic design:::should go over 
def wordSearchFromCellInDirection(board, word, startRow, startCol, dir):
    (rows, cols) = (len(board), len(board[0]))
    dirs = [ (-1, -1), (-1, 0), (-1, +1),
             ( 0, -1),          ( 0, +1),
             (+1, -1), (+1, 0), (+1, +1) ]
    (drow,dcol)=dirs[dir]
    # i for the loop in the matrix
    i=0
    # j for the loop in the word
    j=0
    while(j<len(word)):
        row = startRow+i*drow
        col = startCol+i*dcol
        # first we need to check whether we have run out of this board
        if (row<0) or row>=rows or (col<0) or col>=cols:return False
        temp= board[row][col]
    # second we need to see wether this input is an int if it is we jump  
        # temp steps before that we should check wehther present character #matches the word
        if type(temp)==int:
            j+=temp      
        else:
            # we should first check whether the two words matches 
            if temp!=word[j]: return False 
            j+=1    
        i+=1   
    # if we jump out of the word that means we cannont guarantee the 
    if j>len(word):return False
    return True
# loop through the board to check the validation of the tour
def isKingsTour(board):
    (rows,cols)=(len(board),len(board[0]))
    for row in xrange(rows):
        for col in xrange(cols):
            result = tourSearchFromCell(board, row, col)
            if result==False:return False
    return True
# on the board from the startingRow and starting Col check the validation of 
# of tour,loop trougb 8 directions
def tourSearchFromCell(board,startRow,startCol):
    directions = 8
    for dir in xrange(directions):
      present = board[startRow][startCol]
      if present not in xrange(1,len(board)**2+1):
        return False
      # if it is the largest number return True
      if present==len(board)**2:
        return True
      result=tourSearchFromCellInDirection(board,present,startRow,startCol,dir)
      if result==True:
        return True
    return False
# for one direction check the validation of the tour
def tourSearchFromCellInDirection(board, present, startRow, startCol, dir):
    (rows, cols) = (len(board), len(board[0]))
    dirs = [ (-1, -1), (-1, 0), (-1, +1),
             ( 0, -1),          ( 0, +1),
             (+1, -1), (+1, 0), (+1, +1) ]
    (drow,dcol)=dirs[dir]
    row = startRow+drow
    col = startCol+dcol
    if not (row<0 or row>=rows or col<0 or col>=cols):
      return board[row][col]==present+1
 # check the validation of 1d list   
import math   
def areLegalValues(value):
    upperBound=len(value)
    if math.sqrt(upperBound)%1 !=0:return False
    seen=set()
    for val in value:
      if val>upperBound:return False
      #if val =0 it doesn't matter
      if val !=0:
        if val in seen:
          return False
        else:
          seen.add(val) # put in a set and then check the duplication
    return True


#check the validation of one Row
def isLegalRow(board,row):
    (rows,cols)=(len(board),len(board[0]))
    rowCopy = board[row]
    return areLegalValues(rowCopy)
# check the validation of one column
def isLegalCol(board,col):
    (rows,cols)=(len(board),len(board[0]))
    colList=[board[i][col] for i in xrange(rows)]
    return areLegalValues(colList)
# check the validation of one Block
def isLegalBlock(board,block):
    (rows,cols)=(len(board),len(board[0]))
    blockSize=int(math.sqrt(rows))
    startRow=blockSize*(block/blockSize)
    startCol=blockSize*(block%blockSize)
    valList=[]
    for i in xrange(blockSize):
        for j in xrange(blockSize):
            valList.append(board[startRow+i][startCol+j])
    return areLegalValues(valList)
# check whether the whole suduku is leagel
def isLegalSudoku(board):
    (rows,cols)=(len(board),len(board[0]))
    blockSize=int(math.sqrt(rows))
    for row in xrange(rows):
        if isLegalRow(board,row)==False:
            return False
    for col in xrange(cols):
        if isLegalCol(board,col)==False:
            return False
    for block in xrange(blockSize):
        if not isLegalBlock(board,block):return False
    return True
# compute the best score for all the score records
def bestQuiz(a):
    if a==[]:return None
    for c in a:
        if c==[]:return None
    (rows,cols)=(len(a),len(a[0]))
    scoreList=computeScore(a)
    if scoreList==None:return None
    maxScore=max(scoreList)
    index=scoreList.index(maxScore)
    return index
#return average score for all the score records
def computeScore(a):
    (rows,cols)=(len(a),len(a[0]))
    scoreList=[]
    for col in xrange(cols):
        colList=[a[i][col] for i in xrange(rows)]
        colSum=0
        counter=0
        for e in colList:
            if e==-1:
                continue
            colSum+=e
            counter+=1
        if counter==0: return None 
        scoreList.append(float(colSum)/float(counter))
    return scoreList

def friendsOfFriends(d):
    # create a new set to store all the 
    newD=dict()
    for person in d:
      # for ever person create a new set
        newD[person]=set()
        #loop through all friends of 
        friends = d[person]
        # for every friend in friends we get none direct firends
        for friend in friends:
            noneDirictFriends=d[friend]
            for noneDirect in noneDirictFriends:
                if noneDirect not in friends and noneDirect is not person: 
                    newD[person].add(noneDirect)
    return newD


#-----------------------------------------------------------------------------#
# many of the functions are from case study
def make2dList(rows,cols):
    a =[]
    for row in xrange(rows): a+=[[0]*cols]
    return a

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

def getRemove(board):
    print "\n*******************"
    printBoard(board)

    while True:
        prompt = "Enter remove position:"
        move = raw_input(prompt).upper()
        if((len(move)!=2) or (not move[0].isalpha())
           or (not move[1].isdigit())):
            print "Sorry,you should enter something like A2 or d3 to move"
        else:
            col = ord(move[0])-ord("A")
            row = int(move[1])-1 
            # get the real position in the board 2dlist
            if (not isLegalRemove(board,row,col)):
                print "You can't remove item here, try again."
            else:
                return (row,col)
# check whether it is legalRemove
def isLegalRemove(board,row,col):
    (rows,cols)=(len(board),len(board[0]))
    if(row<0 or row>=rows or col<0 or col>=cols or board[row][col]!=0):
        return False
    return True


# make the remove action
def makeRemove(board,rowx,colx):
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
            print "come to tie"
            break
        elif((hasMove(board,currentPlayer)==True)
             and(hasMove(board,otherPlayer)==False)):
            print("Player " +
                  getPlayerLabel(currentPlayer)+" wins!")
            break
        elif((hasMove(board,currentPlayer)==False)
             and(hasMove(board,otherPlayer)==True)):
            print ("Player " +getPlayerLabel(otherPlayer)+" wins!")
            break
        else:
            (row,col)=getMove(board,currentPlayer)
            makeMove(board,currentPlayer,row,col)
            # and there must still somewhere to flip
            (rowx,colx)=getRemove(board)
            makeRemove(board,rowx,colx)
            (currentPlayer,otherPlayer)=(otherPlayer,currentPlayer)
            #switch the player
            #print "Switch Player"
    print "Goodbye~"

######################################################################
##### ignore_rest: The autograder will ignore all code below here ####
######################################################################


def testCheckDiag():
    print "testcheckdiag........."
    assert(checkDiag([[1,2,3],[4,5],[7,8,9]],12,1)==False)
    assert(checkDiag([[2,7,6],[9,5,1],[4,3,8]],15,1)==True)
    assert(checkDiag([[1,3,5],[4,4,4]],9,1)==False)
    print "Passed................"

def testCheckIsMagicSquare():
    print "test isMagicSquare........"
    assert(isMagicSquare([[1,2,3],[4,5,],[7,8,9]])==False)
    assert(isMagicSquare([[1,2,3],[4,5,6],[7,8,9]])==False)
    assert(isMagicSquare([[2,7,6],[9,5,1],[4,3,8]])==True)
    assert(isMagicSquare([[1,3,5],[4,4,4]])==False)
    assert(isMagicSquare([[12769, 4, 8836], [6724, 5476, 9409], [2116, 16129, 3364]])==False)
    assert(isMagicSquare([[0],[0]])==False)
    assert(isMagicSquare([[42]])==True)
    print "Passed................"



def testWordSearchWithIntegerWildcards():
    board = [ [ 'p', 'i', 'g' ],
              [ 's',   2, 'c' ],
            ]
    print "test wordSearchWithIntegerWildcards......"
    assert(wordSearchWithIntegerWildcards(board,"cat")==True)
    assert(wordSearchWithIntegerWildcards(board,"co")==True)
    assert(wordSearchWithIntegerWildcards(board,"cow")==True)
    print "Passed............"

def testWordSearchFromCellInDiriction():
    board = [ [ 'p', 'i', 'g' ],
              [ 's',   2, 'c' ],
              ]
             
    print " test wordSearchFromCellInDiriction()..."
    assert(wordSearchFromCellInDirection(board,"cat",1,2,3)==True)
    assert(wordSearchFromCellInDirection(board,"cat",1,1,3)==False)
    assert(wordSearchFromCellInDirection(board,"co",1,2,3)==False)
    assert(wordSearchFromCellInDirection(board,"co",1,1,2)==True)
    assert(wordSearchFromCellInDirection(board,"cow",1,2,3)==True)
    assert(wordSearchFromCellInDirection(board,"cows",1,2,3)==True)
    print "Passed......."

def testWordSearchFromCell():
  #wordSearchFromCell(board, word, startRow, startCol):
    board = [ [ 'p', 'i', 'g' ],
                [ 's',   2, 'c' ],
                ]
    print "test wordSearchFromCell........."
    assert(wordSearchFromCell(board,"cat",1,2)==True)
    assert(wordSearchFromCell(board,"cat",1,1)==False)
    assert(wordSearchFromCell(board,"co",1,2)==False)
    assert(wordSearchFromCell(board,"co",1,1)==True)
    print  "Passed.........."

def testIsKingsTour():
    board=[[3,2,1],
            [6,4,9],
            [5,7,8],]
    board1=[[1,2,3],
    [7,4,8],
    [6,5,9],]
    board2=[[3,2,1],[6,4,0],[5,7,8]]
    print "test Iskingtour   ..........."
    assert(isKingsTour(board)==True)
    assert(isKingsTour(board1)==False)
    assert(isKingsTour(board2)==False)
    print "Passed............."


def testTourFromCell():

    board=[[3,2,1],
            [6,4,9],
            [5,7,8]]
    board1=[[1,2,3],
    [7,4,8],
    [6,5,9],]
    print "test toursearchFromCell............."
    assert(tourSearchFromCell(board,1,1)==True)
    assert(tourSearchFromCell(board,1,0)==True)
    assert(tourSearchFromCell(board,2,1)==True)
    assert(tourSearchFromCell(board1,0,1)==True)
    print "Passed............................"




def testTourSearchFromCellInDirectioin():
    board=[[3,2,1],
            [6,4,9],
            [5,7,8]]
    print "test tourSearchFromCellInDirection......."
    assert(tourSearchFromCellInDirection(board,2,0,1,3)==True)
    assert(tourSearchFromCellInDirection(board,1,0,2,3)==True)
    assert(tourSearchFromCellInDirection(board,4,1,1,5)==True)
    print "Passed.........."

def testAreLegalValues():
    print "test are Leagal Valuse....."
    assert(areLegalValues([1,0,0,2])==True )
    assert(areLegalValues([1,2,3,4,0])==False)
    assert(areLegalValues([1,1,0,0,0])==False)
    assert(areLegalValues([1,2,3,4,5,6,7,8,9])==True)
    print "Passed....................."

def testIsLeagalRow():
  board=[
  [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]]
  board2=[[1,2,3,1],[2,3,1,0],[1,3,2,4],[1,0,0,0]]
  print "test testIsLeagalRow ......."
  assert(isLegalRow(board,1)==True)
  assert(isLegalRow(board,2)==True)
  assert(isLegalRow(board,3)==True)
  assert(isLegalRow(board2,0)==False)
  print "Pssed............"


def testIsLeagalCol():
  board=[
  [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]]
  board2=[[1,2,3,1],[2,3,1,0],[1,3,2,4],[1,0,0,0]]
  print "test isLegalCol......."

  assert(isLegalCol(board,4)==True)
  assert(isLegalCol(board,5)==True)
  assert(isLegalCol(board,6)==True)
  print "Passed............"

def testIsLeagalBlock():
  board=[
  [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
  ]
  board2=[[1,2,3,1],[2,3,1,0],[1,3,2,4],[1,0,0,0]]
  board3=[[1, 0, 0, 0], [0, 1, 0, 0], [3, 2, 1, 0], [0, 0, 4, 2]]
  print " test isLegalBlock......."
  assert(isLegalBlock(board,2)==True)
  assert(isLegalBlock(board,3)==True)
  assert(isLegalBlock(board2,1)==False)
  assert(isLegalBlock(board3,0)==False)
  print "Passed..................."

def testIsLegalSudoku():
  board=[
  [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
  ]
  board2=[[1,2,3,1],[2,3,1,0],[1,3,2,4],[1,0,0,0]]
  board3=[[0,4,1,0],[1,3,0,0],[4,0,0,2],[3,0,0,1]]
  board4=[[1, 0, 0, 0], [0, 1, 0, 0], [3, 2, 1, 0], [0, 0, 4, 2]]
  print "test isLeagalSudoku......"
  assert(isLegalSudoku(board)==True)
  assert(isLegalSudoku(board2)==False)
  assert(isLegalSudoku(board3)==True)
  assert(isLegalSudoku(board4)==False)
  print "Passed............"
def testBestQuiz():
  a = [ [ 88,  80, 91 ],
        [ 68, 100, -1 ]
      ]
  b=[[12,34,44],[12,12,12]]
  c=[[-1,-1],[-1,-1]]
  print"test bestquiz..........."
  assert(bestQuiz(a)==2)
  assert(bestQuiz(b)==2)
  assert(bestQuiz([])==None)
  assert(bestQuiz(c)==None)
  print "Passed..........."

def testComputeScore():
  a = [ [ 88,  80, 91 ],
        [ 68, 100, -1 ]
      ]
  b=[[12,34,44],[12,12,12]]
  c=[[1,2,-1],[1,2,1]]
  print "test computeSocer ...."
  assert(computeScore(a)==[78.0,90.0,91.0])
  assert(computeScore(b)==[12.0,23.0,28.0])
  assert(computeScore(c)==[1.0,2.0,1.0])
  print "Passed.............."



def testFriendsOfFriends():
  a=["b","c","d"]
  b=["a","d","e"]
  c=['a','d','f']
  d=['a','b','c']
  e=['b']
  f=['c']

  Dictionary={'a':set(a),'b':set(b),'c':set(c),'d':set(d),'e':set(e),'f':set(f)}

  d=dict()
  d["fred"] = set(["wilma", "betty", "barney", "bam-bam"])
  d["wilma"] = set(["fred", "betty", "dino"])
  d["dino"]=set(['wilma'])
  d["barney"]=set(["fred"])
  d["bam-bam"]=set(["fred"])
  d["betty"]=set(["fred","wilma"])
  print " test friends........"
  assert(friendsOfFriends(Dictionary)=={'a': set(['e', 'f']), 'c': set(['b']), \
    'b': set(['c']), 'e': set(['a', 'd']), 'd': set(['e', 'f']), \
    'f': set(['a', 'd'])})
  assert(friendsOfFriends(d)=={'barney': set(['bam-bam', 'wilma', 'betty']),\
   'dino': set(['betty', 'fred']), 'fred': \
   set(['dino']), 'betty': set(['dino', 'bam-bam', 'barney']), \
   'bam-bam': set(['wilma', 'betty', 'barney']), \
   'wilma': set(['bam-bam', 'barney'])})

  d2=dict()
  d['s']=set(['m'])
  d['m']=set(['k','s'])
  d['k']=set(['m'])
  assert(friendsOfFriends(d2)=={})

  print "Passed........"
def testAll():
    testCheckDiag()
    testCheckIsMagicSquare()
    testWordSearchWithIntegerWildcards()
    testWordSearchFromCellInDiriction()
    testWordSearchFromCell()
    testIsKingsTour()
    testTourFromCell()
    testTourSearchFromCellInDirectioin()
    testAreLegalValues()
    testIsLeagalRow()
    testIsLeagalCol()
    testIsLeagalBlock()
    testIsLegalSudoku()
    testBestQuiz()
    testComputeScore()
    testFriendsOfFriends()

def main():
    testAll()
    playIsola()

if __name__== "__main__":
    main()







