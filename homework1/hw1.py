# hw1.py
# Siyu Chen + siyuchen + Section A

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
 ##      P  Q   P and Q    P and (not Q)   not (P and Q)   (Not P) or (Not Q)
 ##      T  T      T         F                  F                   F
 ##      T  F      F         T                  T                   T
 ##      F  T      F         F                  T                   T
 ##      F  F      F         F                  T                   T

# b: x is not 0 and x is not False and  x is not ""

" !!!!!!!!!!   use  bool(x)   !!!!!!!!   "
## c: Integer
## d: such as +, when we use two int val we will add them such as 1+1, when we use + between two strings, we do concatenation of strings


#2: Code Tracing:
##  10      
''' first we get g(9 )=8 and f(13)=28 and then we need to compute f(8)=64 and g(28)=27 ; the final step we need to do is to do 64%27 and return 10
'''
#############################################
##  f g f False
##  h h h 2 
''' f(1,0) will print "f" return true and g(-1,-2) will print "g" and retrun true and f(3,4) will print "f" return False ,in "and" circomstances, once there is false python don't go to g(5,6), then print "False", so finally we will see f g f  and the returned result is False

     for the second line, we will find  h(-1,0) will print "h" and return 0 h(0,1) will print "h" and return 0 , h(1,2) will print "h" return 2 which is not 0 and in python once the or sentence is true the result will return 2 and don't go to h(2,3)
       so we will see "h h h 2" as printed 
'''  

#3: x=30, y=10
##   I just try some number and found when x=30 and y=10 satisfy the requirment, good luck ^-^ 
##  in order to reason it, first line asks the x and y should be both int, and x should be greater than y, and all digits in x and y will sum up less than 5, so all the digits in x, y are bounded to 0,1,2,3,4. As x, y have the same remainder mod by 10, the end digit should be 0, and we find x should be A0 and y should be B0. To satisfy the last equation, we find x should be 30 and y should be 10.
'''
def f(x,y):
    return ((type(x) == type(y) == int) and
            (100 > x > y > 0) and
            (x/10 + x%10 + y/10 + y%10 < 5) and
            (x % 10 == y % 10) and
            (x == y * 3))
'''
##   x=38,y=11
##    (x,y)=(38,11) as we find x is bounded to 30 to 40 so, y only can be 11 or 12, when y=11, 3*y=33 so, when x=38 satisfy the g(x,y)==5, it is imposibble for y to be 12, as 3y=36 36+5=41>40 

#4: import math

# def findRoot(a,b,c):
#     delta=b**2-4*a*c;
#     if delta <0:
#         return False;
#     else:
#         return (-b+math.sqrt(delta))/2;  

#  def findRoot(a,b,c):
#      delta=b**2-4*a*c;
#      return (a!=0) and (delta>=0) and( -b+delta**(0.5))/2/a  

#5: a: x=-y; neither of x or y could be 0, and they can't be both even, one must be negative one must be possitive; the abstract of x and y should be the same to guruantee ((x%y==y%x)) so we find x=-y should be the result.

#   b: the print shoulb be 7,
''' (5*3 ==0)=0,
     the right part should be 5+r(r(1,0),1)
     so we can get that the equations should be 5+r(1,1)
     so it is 5+2=7 
     this will print 7
'''
#rasoning over code:

# f1(x,y) (x,y)=(5,3) we find x>y and x-y<10 then 5=sqrt(z) z=10+x*y, assume x=y+k; then we can calculate the x by these constrains as: z should be 25 thus we find x=5,y=3, 


#f2(x) x=9.0  we find that x should not be int as type(x) is not int; then ((x%1)**2==int(x%1)) so x%1 should be 0, as x**2 is larger than 8*x, x should be larger than 8, x could be 9.0


# f3(x,y) (6,4) we find x+y should be 10, x>y so there are only, (9,1) (8,2)(7,3)( 6,4) to satisfy the result, so we can find that when x=6,y= 4 is the result.

#f4(x,y) (50,1) we find that y can only be 3 or 2 or 1 and we found we could only find the x should be at least something bigger than 1, when y=1, x could be 50, so we get the result.

#f5(x,y) (x,y) =(10,6) is the resutl,  as x+y=16 ,x>y we only have 7 kind of possilbe results, then as round(float(x/y))!=round(float(x)/y), therefore, x/y %1 should be greater than 0.5 to make it satisfy the statement.

#f6(x)  we find that x=int , 1000>x>0, if x=123, y flip x so y=321, so as x==y so x should be something like  ABA, when we come to (int(x**0.5) == 11) x can be numbers freom 121 to 143, as fore the constrain: (x / 125) > (x / 135), x should larger than 125 and smaller than 135, so x should be 131, therefore, we find the result



######################################################################
# Place your autograde solutions below here
######################################################################
#import math
def kthDigit(x, k):
    #  for different situation we found the different situation to get the number of kth digit
    '''if x < 0:
        temp = -x
    else :
        temp=x

    temp = (temp/10**k)%10;'''

    return (abs(x)/10**k)%10

def numberOfPoolBalls(rows):
    # find the number of PoolBalls and get the result by adding all the balls for different rows
    

    return rows*(rows+1)/2

def numberOfPoolBallRows(balls):
    # it's like the inverse of the previous method, we find when ball equals to 0, we will return 0, when balls number doesn't equal to the total sum of the balls of the rows n we have to do ceilling to get the row number
    result=(-1+(1+8*balls)**(0.5))/2.0
    
    return int(result)+(result%1 >0)
    # this is how we do ceiling to get the result



def isEvenPositiveInt(x):
    # first we need to judge whether x is int or not and if it is int we come to see whether x is greater than 0  and whether it is enven
    '''if (type(x)==int and x>0 and x%2==0):
        result= True;
    else:

        result= False;'''
    #print (x,result)
    return type(x)==int and x>0 and x%2==0

def isPerfectCube(x):
    # we can divide x into tow groups positive integers and negative integers, each group treat them differently and finaly use ceilling to see whether the cube root is an int or not


    result=(abs(x)**(1.0/3))
    print(result)
   
    return x ==0 or (result%1==0)


def isTriangular(x):
    # it is very similar with row of ball problem, first we need to find whether x is positive, then we need to judge whether the square root is integer 
    

    
    return x>=0 and (1-(((-1+(1+8*x)**(0.5))/2.0)%1>0))

    

def fabricYards(inches):
    # if the inches is 0 return 0
    # if the inches is not 0 , return ((inches-1)/36+1)
    return inches !=0 and ((inches-1)/36+1)
 
def fabricExcess(inches):
   # if the inches is 0 return 0
   # if the inches i positive return the excess inches when we dill with 36, we need to treat it as 0 it is the approach 1

   ## as for approach 2:
   #  return fabricYards(inches)*36-inches
    return inches !=0 and (36-inches%36)%36
    

def nearestBusStop(street):
  # find the nearer street to stop the bus, we use round to get the nearest integer we find especially we need to deal with the situation where 
  #print  round(float(street-1)/8)*8
    return round(float(street-1)/8)*8


def slope(x1,y1,x2,y2):
    return 1.0*(y2-y1)/(x2-x1)

def almostEqual(x,y)
    


def areCollinear(x1, y1, x2, y2, x3, y3):
    return (y1-y2)*(x3-x1)-(y3-y1)*(x1-x2)==0
#
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