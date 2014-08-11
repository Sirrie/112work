#hw5.py
'''
def f1(a):                    
    assert(len(a) == 8)                             
    s = 0                                           
    for i in xrange(0, 8, 2):                       
        assert(a[i] > s)
        s += a[i]   
        print str(s)                  
        assert(str(s) == a[i+1])                    
    return True
print f1([1,'1',2,'3',4,'7',8,'15'])

def f3(n):
    result = 0
    a = [9]
    while (result < 999):
        a += [(1+a[-1])]
        b = [str(a[i]) for i in xrange(len(a))]
        s = "".join(b)
        result = int(s)
    return (result == n)
print f3(91011)

def f4(a):
    n = len(a)
    assert(n == 3)
    b = [([0]*n) for row in xrange(n)]
    for i in xrange(n):
        b[i][i] = i
        b[i][n-1-i] = i+1
    return b         

a=[[0,0,1],[0,0,2],[0,0,3]]
print len(a)
print f4([[0,0,1],[0,0,2],[0,0,3]])


def f(a):
    a=[42]
    return a
a=[1,2,3]
b=f(a)

print a
print b

'''


def dotProduct(a,b):
    assert((len(a)!=0)==True)
    assert((len(b)!=0)==True)
    assert((len(a)==len(b))==True)
    for c in a:
        assert(type(c)==int)
    for c in b:
        assert(type(c)==int)
    total=0
    for i in xrange(len(a)):
        total+=a[i]*b[i]
    assert(type(total)==int)
    return total
print dotProduct([1,2,3],[4,5,6])


def solvesCryptarithm(puzzle,solution):
    checkPuzzle=dividePuzzle(puzzle)
    puzzleLength  =3
    checkPuzzleInt=[]
    for i in xrange(puzzleLength):
        checkPuzzleInt.append(trans2Digit(checkPuzzle[i],solution))
    intA =checkPuzzleInt[0]
    intB =checkPuzzleInt[1]
    intC =checkPuzzleInt[2]
    return intA+intB==intC

def dividePuzzle(puzzle):
    stringA=""
    stringB=""
    stringC=""
    isA = True
    isB = False
    isC = False
    for c in puzzle:
        if c=="+":
            isA=False
            isB=True    
        elif c=="=":
            isB=False
            isC=True
        elif isA:
            stringA+=c
        elif isB:
            stringB+=c
        elif isC:
            stringC+=c
    return [stringA,stringB,stringC]
print dividePuzzle("A+B=C")

def trans2Digit(str,solution):
    result=[]
    for c in str:
        result.append(searchDigit(c,solution))
    result="".join(result)
    return int(result)


def searchDigit(c,solution):
    for i in range(len(solution)):
        if c ==solution[i]:
            return str(i)
    return '-1'

print trans2Digit("SEND","OMY--ENDRS")

print solvesCryptarithm("SEND+MORE=MONEY","OMY--ENDRS") 


def aeraOfPolygon(points):
    xPoints = []
    yPoints = []
    for x in points:
        xPoints+= [x[0]]
        yPoints+= [x[1]]
    xLeftShift = shift(xPoints,1)
    yLeftShift = shift(yPoints,1)
    aera=-dotProduct(xPoints,yLeftShift)+dotProduct(yPoints,xLeftShift)
    aera=aera/2.0
    return aera
# shift list to left n bit, negeative ones means right shift
def shift(lst,n):
    return lst[n:]+lst[:n]

def dotProduct(a,b):
    assert((len(a)!=0)==True)
    assert((len(b)!=0)==True)
    assert((len(a)==len(b))==True)
    for c in a:
        assert(type(c)==int)
    for c in b:
        assert(type(c)==int)
    total=0
    for i in xrange(len(a)):
        total+=a[i]*b[i]
    assert(type(total)==int)
    return total

s=[(4,10), (9,7), (11,2), (2,2)]

print aeraOfPolygon(s)


