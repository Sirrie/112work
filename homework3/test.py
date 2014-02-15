
def nearestKaprekarNumber(n):
  # edge case where input is non-positive we return 1 we need to change float into int
   # n = int(round(n))
    if n <= 1: 
      return 1 
    if isKaprekar(n): 
      return n
    # take into consideration we only chose the int number but input could be float
    delta=0.00000000001
    print n-delta
    number   = int(round(n-delta))
    print ('number',number)
    smallerKaprekar = number 
    largerKaprekar  = number 
    # from the number we need to find we need to go to two directions and find the one that is nearer to the target number 

    while(smallerKaprekar > 0 and (not isKaprekar(smallerKaprekar) and not isKaprekar(largerKaprekar))):
    # find one and return 

        smallerKaprekar = smallerKaprekar - 1
        largerKaprekar  = largerKaprekar  + 1
        print "here "+str(smallerKaprekar)+" "+str(largerKaprekar)
    
    if (isKaprekar(smallerKaprekar) and isKaprekar(largerKaprekar)):
      leftDifference = n - smallerKaprekar
      rightDifference = largerKaprekar - n
       # ties to the smaller one  
      if leftDifference <= rightDifference :
        print "here1 "
        return smallerKaprekar
      else:
        print "here2"
        return largerKaprekar
    elif isKaprekar(smallerKaprekar):
      return smallerKaprekar
    else:
      return largerKaprekar
    
# check if the number is Kaprekar number 
# change the number into two parts of a number , and mimic the process of the whole process of computing kaprekar number 
def isKaprekar(n):
    if type(n) is not int:
      return False# we need to round input into int 
    if n <= 0 :
      return False
    if n==1 :
      return True
    squareNumber  =  n**2
    stringNumber  =  str(squareNumber)
    stringLength  =  len(stringNumber)
    if stringLength <2 : return False
    x = stringLength/2 
    leftPart      =   stringNumber[0:x]
    rightPart     =   stringNumber[x:]
    
    if(n == int(leftPart) + int(rightPart) and int(rightPart) > 0):
        return True
    if(stringLength %2 != 0 and stringLength >1):
      leftPartodd   =    stringNumber[0:x+1]
      rightPartodd  =    stringNumber[x+1:]
      
      if (n == int(leftPartodd) + int(rightPartodd) and int(rightPartodd)>0):
        return True
    return False

def testisKaprekar():
    print "Testing isKaprekar()...",
    assert(isKaprekar(0)==False)
    assert(isKaprekar("")==False)
    assert(isKaprekar(1.1)==False)
    assert(isKaprekar(45)==True)
    print  "Passed!"


def testNearestKaprekarNumber():
    print "Testing nearestKaprekarNumber()...", 
    assert(nearestKaprekarNumber(5.000000099999)==9)
    assert(nearestKaprekarNumber(4.999999999999)==1)
    assert(nearestKaprekarNumber(0.000000000001)==1)
    print nearestKaprekarNumber(13641234)
    assert (nearestKaprekarNumber(-1) ==1)
    assert(nearestKaprekarNumber(0) == 1)
    assert(nearestKaprekarNumber(0.2)==1)
    assert(nearestKaprekarNumber(49.5)==45)
    assert(nearestKaprekarNumber(49) == 45)
    assert(nearestKaprekarNumber(51) == 55) 
 
    assert(nearestKaprekarNumber(222)== 297)
testisKaprekar()
print "A "
print isKaprekar(10)
print nearestKaprekarNumber(27)
print nearestKaprekarNumber(2475.5)
