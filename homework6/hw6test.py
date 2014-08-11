#hw6test.py
# wordSearch.py
# This code was developed in class on Tue 19-Feb-2013.
# As such, it may not contain perfect style, and may
# even contain a small bug here or there (usual disclaimer).

def wordSearch(board, word):
    (rows, cols) = (len(board), len(board[0]))
    for row in xrange(rows):
        for col in xrange(cols):
            result = wordSearchFromCell(board, word, row, col)
            if (result != None):
                return result
    return None

def wordSearchFromCell(board, word, startRow, startCol):
    for dir in xrange(8):
        result = wordSearchFromCellInDirection(board, word, startRow, startCol, dir)
        if (result != None):
            return result
    return None

def wordSearchFromCellInDirection(board, word, startRow, startCol, dir):
    (rows, cols) = (len(board), len(board[0]))
    dirs = [ (-1, -1), (-1, 0), (-1, +1),
             ( 0, -1),          ( 0, +1),
             (+1, -1), (+1, 0), (+1, +1) ]
    dirNames = [ "up-left", "up", "up-right",
                 "left"   ,       "right",
                 "down-left", "down", "down-right" ]
    (drow,dcol) = dirs[dir]    
    for i in xrange(len(word)):
        row = startRow + i*drow
        col = startCol + i*dcol
        if ((row < 0) or (row >= rows) or (col < 0) or (col >= cols) or
            (board[row][col] != word[i])):
            return None
    return (word, (startRow, startCol), dirNames[dir])

def testWordSearch():
    board = [ [ 'd', 'o', 'g' ],
              [ 't', 'a', 'c' ],
              [ 'o', 'a', 't' ],
              [ 'u', 'r', 'k' ],
            ]
    print wordSearch(board, "dog") # True
    print wordSearch(board, "cat") # True
    print wordSearch(board, "tad") # True
    print wordSearch(board, "cow") # False

#testWordSearch()
def f(s):
    (u,i) = ([],-1)
    while True:
        i += 1
        if (i >= len(s)): break
        elif (i % 3 == 0): continue
        if (s[i] == s[(i+4)%len(s)]): u += [i]
    return u
print f("dog-done")
def f(t):
  return ((len(t) == 5) and
          (t[1:3] == t[-1:-3:-1]) and
          (len(set(t)) == 3))
print f([0,1,2,2,1])
def f(L):
    assert(sorted(L) == range(6))
    ok = 0
    for i in xrange(1,len(L)):
        if (L[i]%2 != ok):
            if (ok == 1):
                return False
            ok = 1
    return True
print f([0,2,4,1,3,5])

def f(L):
    count = 0
    for val in L:
        if (type(val) != str):
            count += 1
            c = chr(ord("a")+val)
            if ((val < 0) or
                (val >= len(L)) or
                (L[val] != c)):
                return False
    return (count == 3)
print f([1,'b','c','d',2,3])
def f(L):
    (rows,cols) = (len(L), len(L[0]))
    assert((rows == 2) and (cols == 4))
    i = 0
    for col in xrange(cols):
        for row in xrange(rows):
            assert(L[row][cols-1-col] == i)
            i += 1
    return True
print f([[6,4,2,0],[7,5,3,1]])
print "end"
import copy
a = [[1],[2]]
(b,c,d) = (a, copy.copy(a), copy.deepcopy(a))
print (a == b), (a == c), (a == d)
print (a is b), (a is c), (a is d)
print (a[0] is b[0]), (a[0] is c[0]), (a[0] is d[0])
 
a = [[1],[2]]
print "A",
try:
    print "B",
    b[0][0] += 10
    print "hereris a",a
    print "hereis b",b
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


def f(L):
    # Assume L is a ragged (non-rectangular!) 2d list
    return (max(L[0]) == 2) and L == [range(len(L)-n) for n in xrange(len(L))]
print f([[0,1,2],[0,1],[0]])


def mostFrequent(a):
    maxValue = None
    maxCount = 0
    counts = dict()
    for element in a:
        count = 1 + counts.get(element,0)
        print ('element',element,"count",count)
        counts[element] = count
        if (count > maxCount):
            maxCount = count
            maxValue = element
    return maxValue

print mostFrequent([2,5,3,4,6,4,2,4,5])  # prints 4