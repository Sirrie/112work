# siyuchen: section N, siyuchen

# group member:     zujung,skathara,zed
#------------------------------------------------------------#

'''
Fall 2013 midterm:
1:
  a: False because x=11111111 all will result in -1
  b: False -x =~x+1
  c: True
  d: True  because nothing
  e: False  the sorting is compiled in C  
  f: True    a and b are aliases to the same variable
  g: False the function pop will return things
  h: False  there should be 2^K rows
  i: False   int are immutable
  j: True  according to DeMorgan's Law, that's True
2:
  a:
    def f(n):
       for x in range(0, n, 42):         O(n)
           y = n                          O(1)
           while (y > 0):                 
               y /= 42                     O(logn)
               print (x,y)

                                so the total is O(nlogn)
b:
     def g(a):
      n = len(a)                          O(n)
      for x in xrange(0, n, len(str(n))): 
          a[x%n] += 5                     O(1)
          a.sort()                        O(logn)
          if (a[0] == 5): print "amazing!" O(1)
                                     so the total is O(nlogn)

c:
    x%2   x-((x>>1)<<1)   int(bin(x)[-1])  x&(-1)&1

d:  lin2 uses numbered virables
    lin3 uses numbered virables
    there is no comment for the whole function
    line 5 is not effective

e:   to use time function 
      def G(n):
         s= time.time()
         f(n)
         e= time.time()
       return e-s
    we input large input n =1000, get t1 and set input n2=10000,get t2, and then check t2/t1 == 10**42
f: 0,1,
g:   def drowHour(cx,cy,r,hour):
         hourAngle=math.pi/2-2*math.pi*hour/12
         hourRadius=r
         hourX=int(round(cx+hourRadius*math.cos(hourAngle)))
         hourY=int(round(cy+hourRadius*math.sin(hourAngle)))
         canvas_line(cx,cy,hourX,hourY)

h:  merge sort is devided into two steps, the first step, we call  mergesort recursively and the second step we merge the two sorted arry, every time for merge it takes O(n) times but we have logn steps to split the whole array into different ones, step by step. therefore the total cost is O(nlogn)

j:  "\" \ means ignore the following quote so this string haven't end ,so python doesn't know what to do.

3: 
  1:it will print aaeeggggi
  2: it will print ['0b01','0b110','0b1011']
  3: [5,4,3,2,1] as we find the a is [2,4,1,3,5] the sorting will return reversed version 
  4:it will print 
    <  23>
    <1234>
    <   1>

5: it will draw five rectangles but finally we can only see 
    three rectangles, one (0,0,250,250), one (100,100,350,350) and (200,200,250,250)
4:
  1:we find x+y should be 2 and x is 2's n times, so guess y=3, so x=17,when 16 right shift 3 bit, it wiil print 2
  2: t length should be 4 and then t[i]*i deal with letters and the other part deal with letters so t could be ['5','x',5,'y'], s could be ['9','1','5','3']
  4: like we done it before, the first part only deal with them seperately
  so we can find the c should be [3,5] and a[3] should be 5 ,so we find the a[5]should be 5
  so a can be [6,8,2,5]

5: free response:

def partiallyMergesorted(lst,passNum):
    step = 2**passNum
    for i in xrange(0,len(lst),step):
        partialList=lst[i:i+step]
        if not checkSorted(partialList):
            return False
    return True

#check every sublist is sorted 
def checkSorted(list):
    length=len(list)
    for i in xrange(length-1):
        if list[i]>list[i+1]:
            return False
    return True

6:
def encode(lst):
    processedStr=""
    #escape all the none letter
    for c in lst:
        if c.isalpha():
            processedStr+=c.upper()
    result="42"
    for c in processedStr:
        distance=ord(c)-ord('A')
        if distance<10:
            addDistance="0"+str(distance)
        else:
            addDistance=str(distance)
        result+=addDistance
    return int(result)

'''


#------------------------------------------------------------#
def isValidHand(hand):
    ValidRank="23456789TJQK"
    ValidSuit="DSHC"
    # check the length doesn't equal 5 cards
    if len(hand)!=14:
        return False
    for i in xrange(len(hand)):
    # check rank
        if i%3==0:
            if hand[i] not in ValidRank:
                return False
    # check suit
        if i%3==1:
            if hand[i] not in ValidSuit:
                return False
        if i%3==2:
            if hand[i]!=" ":
                return False
    return True

def isFlush(hand):
    validSuit="DSHC"
    if not isValidHand(hand):
        return False
    if isValidHand(hand):
        suit=hand[1]
        # loop to check every elment of the hand
        for i in xrange(1,len(hand),3):
            if hand[i]!=suit:
                return False
    return True

def isRoyalFlush(hand):
    specialRank="TJQKA"
    if isValidHand(hand):
        # loop to check every suit of the card
        for i in xrange(0,len(hand),3):
            if hand[i] in specialRank:
                return True
    return False

def hasPair(hand):
    if isValidHand(hand):
        for i in xrange(0,len(hand),3):
            for j in xrange(i,len(hand),3):
                if hand[j]==hand[i]:
                    return True
    return False


def multiplyPolynomials(p1,p2):
    length1=len(p1)
    length2=len(p2)
    p1.reverse()
    p2.reverse()
    result=[0]*(length1+length2-1)
    for i in xrange(length1):
        for j in xrange(length2):
            result[i+j]+=p1[i]*p2[j]
    # we should reverse the list
    result.reverse()
    return result
    
def averageColor(rgbList):
    blueSum=0;
    greenSum=0;
    redSum=0;
    for rgb in rgbList:
        blueSum+=rgb&255
        greenSum+=(rgb>>8)&255
        redSum+=(rgb>>16)&255
    # compute avrage sum
    blueAvg=blueSum/len(rgbList)
    greenAvg=greenSum/len(rgbList)
    redAvg=redSum/len(rgbList)
    RGBAVG=blueAvg+(greenAvg<<8)+(redAvg<<16)
   # return average color 
    return RGBAVG

import copy
# check if it is magic square
def isMagic(matrix):
    (rows,cols)=(len(matrix),len(matrix[0]))
    checkSum=sum(matrix[0])
    for row in xrange(rows):
        if sum(matrix[row])!=checkSum:
            return False
    for col in xrange(cols):
        allCols=[matrix[row][col] for row in xrange(rows)]
        if sum(allCols)!=checkSum:
            return False
    return True

# loop through all possible position exchange and then chan
def makeMagic(matrix):
    newMatrix=copy.deepcopy(matrix)
    (rows, cols)=(len(matrix),len(matrix[0]))
    for i in xrange(rows):
        for j in xrange(cols):
            for k in xrange(rows):
                for l in xrange(cols):
                    newMatrix=copy.deepcopy(matrix)
                    if i!=k or j!=l:
                        (newMatrix[i][j],newMatrix[k][l])=(newMatrix[k][l],\
                            newMatrix[i][j])
                    if isMagic(newMatrix):
                        return newMatrix
    return None

def numberOfUniqueValue(d):
    s=set()
    for key in d:
        s.add(d[key])
    print s
    return len(s)
# draw Grid according to the requirements
def drawGrid(canvas, x0, y0, x1, y1):
    if x1-x0>200:size=1
    else:size=0
    width=x1-x0
    height=y1-y0
    initialNumbera=4
    initialNumberb=8
    if size==1:
        rowNumber=initialNumbera
        colNumber=initialNumberb
    else:
        rowNumber=initialNumberb
        colNumber=initialNumbera
    cellwidth=width/colNumber
    cellheight=height/rowNumber
    drawGridHelper(canvas,size,colNumber,rowNumber,cellwidth,cellheight)
# drawhelper to draw rectangle
def drawGridHelper(canvas,size,colNumber,rowNumber,cellwidth,cellheight):
    number=1
    if size==1:
        for row in xrange(rowNumber):
            for col in xrange(colNumber):
                drawRectangle(canvas,row,col,cellwidth,cellheight,number,size)
                number+=1
    else:
        for col in xrange(colNumber):
            for row in xrange(rowNumber,-1,-1):
                drawRectangle(canvas,row,col,cellwidth,cellheight,number,size)
                number+=1


# helper function for drawing rectangle
def drawRectangle(canvas,row,col,cellwidth,cellheight,number,size):
    x0=col*cellwidth
    y0=row*cellheight
    x1=x0+cellwidth
    y1=y0+cellheight
    if size==1:
        if (row+col)%2==0:
            color = 'pink'
        else:
            color = 'purple'
    else:
        if (row+col)%2==0:
            color = 'black'
        else:
            color = 'white'
    canvas.create_rectangle(x0,y0,x1,y1,fil=color)
    canvas.create_text(x0+cellwidth/2,y0+cellheight/2,text=str(number),\
        fill='red')
 

#-----------------------------------------------------------------------------#
def testIsMagic():
    print "test isMagic........"
    assert(isMagic([[1,2,3],[4,5,],[7,8,9]])==False)
    assert(isMagic([[1,2,3],[4,5,6],[7,8,9]])==False)
    assert(isMagic([[2,7,6],[9,5,1],[4,3,8]])==True)
    assert(isMagic([[1,3,5],[4,4,4]])==False)
    assert(isMagic([[42]])==True)
    print "Passed................"

def testNumberOfUniqueValue():
    print "test numberOfUniqueValue........"
    assert(numberOfUniqueValue({'dog':1,'cat':2,'cici':3,'titi':3})==3)
    assert(numberOfUniqueValue({1:2,2:2,3:2,4:4,5:5,6:4})==3)
    assert(numberOfUniqueValue({2:3,6:4,3:3,4:5,5:5,7:6})==4)
    print "Passed........................."



def testAverageColor():
    print "test averageColor........."
    print averageColor([0,11,2222,3455])
    assert(averageColor([12,13,14])==13)
    assert(averageColor([14,25,22])==20)
    assert(averageColor([0,11,2222,3455])==1358)
    print "Passed....................."
def testMultiplyPolynomial():
    print "test is multiplyPolynomials...."
    assert(multiplyPolynomials([2,0,3],[4,5])==[8,10,12,15])
    assert(multiplyPolynomials([2,0,4],[4,5,6])==[8,10,28,20,24])
    assert(multiplyPolynomials([2,3,4],[4,5,6])==[8,22,43,38,24])
    print "Passed........................"

def testIsValidHand():
    print "test is ValidHand ........."
    assert(isValidHand("KD KD KD KD KD")==True)
    assert(isValidHand("JD JC KC KD KD")==True)
    assert(isValidHand("KD KD KD KD KD KD")==False)
    print "Passed............"

def testIsFlush():
    print"test is Flush .........."
    assert(isFlush("KD KD KD KD KD")==True)
    assert(isFlush("JD KD 1D 2C 3D")==False)
    assert(isFlush("1D 2D 3D 4D 5D")==False)
    print "Passed..........."

def testIsRoyalFlush():
    print "test is RoyalFlush ........."
    assert(isRoyalFlush("KD KS 7H 8C KC")==True)
    assert(isRoyalFlush("KD KD KD KD KD")==True)
    assert(isRoyalFlush("1D 2D 3D 4D 5D")==False)
    print "Passed.............."

def testHasPair():
    print"test has pair..............."
    assert(hasPair("KD KS 7H 8C KC")==True)
    assert(hasPair("KD 1D 2D 3D 4C")==False)
    assert(hasPair("1D 2D 3D 3C 4D")==False)
    print "Passed............."

def testGrid():
    print "test grid........."
    from Tkinter import *
    import math
    root=Tk()
    canvas = Canvas(root, width=750, height=500)
    canvas.pack()
    drawGrid(canvas,0,0,150,150)
    drawGrid(canvas,150,150,600,600)
    root.mainloop()
    print "Passed........."

def testAll():
    testIsValidHand()
    testIsFlush()
    testIsRoyalFlush()
    testHasPair()
    testMultiplyPolynomial()
    testAverageColor()
    testIsMagic()
    testNumberOfUniqueValue()
    testGrid()

def main():
    testAll()
   

if __name__ == "__main__":
    main()
