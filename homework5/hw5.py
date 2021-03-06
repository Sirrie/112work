# ChenSiyu + siyuchen --- Section N

######################################################################
# Place your non-autograded solutions below here!
######################################################################
'''
1.  [50  pts, 10 pts each]  For each of the following functions f, find values of the parameters so that f will return True.  Circle your answers.

def f1(a):                    
    assert(len(a) == 8)								length of a should be 8
    s = 0											s=0
    for i in xrange(0, 8, 2):						x 0 2 4 6, 
        assert(a[i] > s)
        s += a[i]                     
        assert(str(s) == a[i+1])                    
    return True
    i find the trens that a0>0, a1=a0,s=a0 assume a0=1, thus a1=1,s=1;then a2>1=2, s=3,a3=s=3; a4>s=4, a5=s=7,a6>s=8,a7=s=15, as for odd a we should be str so a=[1,'1',2,'3',4,'7',8,'15']


def f2(a):
    b = sorted(a)
    assert(b == range(len(a)))
    i = a.index(b[1])
    return (b[1:6:2] == a[i:i+3])
     b is a non-destructive copy of a, so we find las b1,b3,b5==a[i:i+3];
     so we find that len(b)=len(a), we also find that if b is [1,2,3,4,5,6], because i=1 a can be [1,2,4,6,3,5]






def f3(n):
    result = 0
    a = [9]
    while (result < 999):
        a += [(1+a[-1])]
        b = [str(a[i]) for i in xrange(len(a))]
        s = "".join(b)
        result = int(s)
    return (result == n)
       becase in first loop a[9]->a[9,10], b=['9','10'],s='910',result=910, and we find a[9,10]->a[9,10,11], b=['9','10,'11'],s='91011',result=91011 stop the loop
n=91011




def f4(a):
    n = len(a)
    assert(n == 3)
    b = [([0]*n) for row in xrange(n)]
    for i in xrange(n):
        b[i][i] = i
        b[i][n-1-i] = i+1
    return (b == a)         
 n=3 len(a)=3 so  there are 3 lists in a, every list is [X,X,X] form and as we can see b[0][0]==0,b[0][2]=1,b[1][1]=1,b[1][1]=2, b[2][2]=2, b[2][0]=3,there for b is ([0,0,1],[0,2,0],[3,0,2]), so a should be the same as b, so a is ([0,0,1],[0,2,0],[3,0,2])

2.  [10 pts]  Say you have a destructive function f(a), which takes a 1d list a.  Write the function g(a) which also takes a 1d list a, but is the non-destructive equivalent of f(a).

    
    import copy
    g(a):
    	c=copy.copy(a)
    	f(c)
    	return c



3.
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
'''

######################################################################
# Place your autograde solutions below here
######################################################################

#

def solvesCryptarithm(puzzle,solution):
	checkPuzzle=dividePuzzle(puzzle)
	puzzleLength  =3
	checkPuzzleInt=[]
	# first devide the puzzle into different parts 
	for i in xrange(puzzleLength):
		checkPuzzleInt.append(trans2Digit(checkPuzzle[i],solution))
	# then deCryptarith the puzzle into different int 
	# then check the result whether can be the sum of the intA and intB can be  the sum of the result of intC
	intA =checkPuzzleInt[0]
	intB =checkPuzzleInt[1]
	intC =checkPuzzleInt[2]
	return intA+intB==intC

# helper function to divide the puzzle into 3 parts and store them in a list
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

# translate a string by referring to solution to an integer
def trans2Digit(str,solution):
	result=[]
	for c in str:
		result.append(searchDigit(c,solution))
	result="".join(result)
	return int(result)

# search through the solution and find the int of the character
def searchDigit(c,solution):
	for i in range(len(solution)):
		if c ==solution[i]:
			return str(i)
	return '-1'

def aeraOfPolygon(points):
    xPoints = []
    yPoints = []
    for x in points:
        #!!!!!!!attention  int can't be iterable so we should change it into list
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
# dotProduct function 
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






######################################################################
##### ignore_rest: The autograder will ignore all code below here ####
######################################################################


def testsolveCryptarithm():
	print "test Cryptarithm......"
	assert(solvesCryptarithm("SEND+MORE=MONEY","OMY--ENDRS")==True)

	print "Passed........."

def almostEqual(x,y):
	epilon=0.00001
	return abs(x-y)<epsilon

