# hw1.py
# name + andrewId + section

######################################################################
# Place your non-autograded solutions below here!
######################################################################
#
# Be sure to start each line with a "#" so it is a Python comment!
# Also be sure to show your work.  Provide some simple explanation
# as to how you derived your solution.  Don't be too detailed, just
# enough so we can follow your logic.
#
#

# my solution to the manually grated portion:
# quiz 13
# Quick Answer:
 # a: not(P and Q) <=>(not P) or (not Q)
 ##      P  Q   P and Q    P and (not Q) 
 ##      T  T      T         F
 ##      T  F      F         T
 ##      F  T      F         F
 ##      F  F      F         F

# b: x is not 0 and x is not False and  x is not ""
## c: integer
## d: such as +, when we use two int val we will add them such as 1+1, when we use + between two strings, we do concatenation of strings


#2: Code Tracing:
##  10
#############################################
##  f g f False
##  h h h 2 
##  
##  

#3:


#4:


#5:

#rasoning over code:

# f1(x,y)  the answer is  (15,1)




######################################################################
# Place your autograde solutions below here
######################################################################
import math
def kthDigit(x, k):
    #  for different situation we found the different situation to get the number
    if x < 0:
        temp = -x
    else :
        temp=x
    temp = (temp/10**k)%10;

    return temp

def numberOfPoolBalls(rows):
    # find the number of PoolBalls
    

    return rows*(rows+1)/2

def numberOfPoolBallRows(balls):
    #print ((-1+math.sqrt(1+8*balls))/2)
    return math.ceil((-1+math.sqrt(1+8*balls))/2)

def isEvenPositiveInt(x):
    return 42

def isPerfectCube(x):
    return 42

def isTriangular(x):
    return 42

def fabricYards(inches):
    return 42
 
def fabricExcess(inches):
    return 42

def nearestBusStop(street):
    return 42

def areCollinear(x1, y1, x2, y2, x3, y3):
    return 42

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

def testKthDigit():
    print "Testing kthDigit()...",
    assert(kthDigit(789, 0) == 9)
    assert(kthDigit(789, 1) == 8)
    assert(kthDigit(789, 2) == 7)
    assert(kthDigit(789, 3) == 0)
    assert(kthDigit(-789, 0) == 9)
    print "Passed!"

def testNumberOfPoolBalls():
    print "Testing numberOfPoolBalls()...",
    assert(numberOfPoolBalls(0) == 0)
    assert(numberOfPoolBalls(1) == 1)
    assert(numberOfPoolBalls(2) == 1+2)
    assert(numberOfPoolBalls(3) == 1+2+3)
    assert(numberOfPoolBalls(10) == 55)
    print "Passed!"

def testNumberOfPoolBallRows():
    print "Testing numberOfPoolBallRows()...",
    assert(numberOfPoolBallRows(0) == 0)
    assert(numberOfPoolBallRows(1) == 1)
    assert(numberOfPoolBallRows(2) == 2)
    assert(numberOfPoolBallRows(3) == 2)
    assert(numberOfPoolBallRows(4) == 3)
    assert(numberOfPoolBallRows(6) == 3)
    assert(numberOfPoolBallRows(7) == 4)
    assert(numberOfPoolBallRows(10) == 4)
    assert(numberOfPoolBallRows(11) == 5)
    assert(numberOfPoolBallRows(54) == 10)
    assert(numberOfPoolBallRows(55) == 10)
    assert(numberOfPoolBallRows(56) == 11)
    print "Passed!"
 
def testIsEvenPositiveInt():
    print "Testing isEvenPositiveInt()...",
    assert(isEvenPositiveInt(2) == True)
    assert(isEvenPositiveInt(2040608) == True)
    assert(isEvenPositiveInt(21) == False)
    assert(isEvenPositiveInt(20406081) == False)
    assert(isEvenPositiveInt(0) == False)
    assert(isEvenPositiveInt(-2) == False)
    assert(isEvenPositiveInt(-2040608) == False)
    assert(isEvenPositiveInt("Go Steelers!") == False)
    assert(isEvenPositiveInt(1.23456) == False)
    assert(isEvenPositiveInt(True) == False)
    print "Passed!"
 
def testIsPerfectCube():
    print "Testing isPerfectCube()...",
    assert(isPerfectCube(0) == True)
    assert(isPerfectCube(1) == True)
    assert(isPerfectCube(-1) == True)
    assert(isPerfectCube(8) == True)
    assert(isPerfectCube(-8) == True)
    assert(isPerfectCube(27) == True)
    assert(isPerfectCube(-27) == True)
    assert(isPerfectCube(16) == False)
    assert(isPerfectCube(-16) == False)
    print "Passed!"
 
def testIsTriangular():
    print "Testing isTriangular()...",
    assert(isTriangular(0) == True)
    assert(isTriangular(1) == True)
    assert(isTriangular(2) == False)
    assert(isTriangular(3) == True)
    assert(isTriangular(4) == False)
    assert(isTriangular(5) == False)
    assert(isTriangular(6) == True)
    assert(isTriangular(54) == False)
    assert(isTriangular(55) == True)
    assert(isTriangular(56) == False)
    assert(isTriangular(-1) == False)
    print "Passed!"
 
def testFabricYards():
    print "Testing fabricYards... ",
    assert(fabricYards(0) == 0)
    assert(fabricYards(1) == 1)
    assert(fabricYards(35) == 1)
    assert(fabricYards(36) == 1)
    assert(fabricYards(37) == 2)
    assert(fabricYards(72) == 2)
    assert(fabricYards(73) == 3)
    assert(fabricYards(108) == 3)
    assert(fabricYards(109) == 4)
    print "Passed all tests!"
 
def testFabricExcess():
    print "Testing fabricExcess... ",
    assert(fabricExcess(0) == 0)
    assert(fabricExcess(1) == 35)
    assert(fabricExcess(35) == 1)
    assert(fabricExcess(36) == 0)
    assert(fabricExcess(37) == 35)
    assert(fabricExcess(72) == 0)
    assert(fabricExcess(73) == 35)
    assert(fabricExcess(108) == 0)
    assert(fabricExcess(109) == 35)
    print "Passed all tests!"

def testNearestBusStop():
    print "Testing nearestBusStop()...",
    assert(nearestBusStop(0) == 0)
    assert(nearestBusStop(4) == 0)
    assert(nearestBusStop(5) == 8)
    assert(nearestBusStop(12) == 8)
    assert(nearestBusStop(13) == 16)
    assert(nearestBusStop(20) == 16)
    assert(nearestBusStop(21) == 24)
    print "Passed all tests!"
 
def testAreCollinear():
    print "Testing areCollinear()...",
    assert(areCollinear(0, 0, 1, 1, 2, 2) == True)
    assert(areCollinear(0, 0, 1, 1, 2, 3) == False)
    assert(areCollinear(1, 1, 0, 0, 2, 2) == True)
    assert(areCollinear(1, 1, 0, -1, 2, 2) == False)
    assert(areCollinear(2, 0, 2, 1, 2, 2) == True)
    assert(areCollinear(2, 0, 2, 1, 3, 2) == False)
    assert(areCollinear(3, 0, 2, 1, 3, 2) == False)
    print "Passed all tests!"

def testAll():
    testKthDigit()
    testNumberOfPoolBalls()
    testNumberOfPoolBallRows()
    testIsEvenPositiveInt()
    testIsPerfectCube()
    testIsTriangular()
    testFabricYards()
    testFabricExcess()
    testNearestBusStop()
    testAreCollinear()

if __name__ == "__main__":
    testAll()