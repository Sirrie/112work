def h3(x, y):
    assert((x>0) and (y>0))
    (hi, lo) = (max(x,y), min(x,y))
    # hint: (x-m)(y-m) = xy - m(x+y) + m**2
    result = 0
    while (lo > 10):
        result += 10*(lo+hi) - 100
        print (lo,hi,result)
        (lo, hi) = (lo-10, hi-10)
    while (lo > 0):
        print (lo, result)
        (lo, result) = (lo-1, result+hi)
    return result

print h3(41,65)

def unboundedNumberGuessing(n):
    sign = 0
    resultStr="0,"
    if n<0:
      sign = 1
    if n == 0:
      resultStr="0"
      return resultStr
    number = abs(n)
    guess = 1
    while (guess <number):
      resultStr +=str((-1)**sign*guess)+","
      guess *=2
    
    
    if guess == number :
      resultStr +=str((-1)**sign*guess)
      return resultStr
    resultStr +=str((-1)**sign*guess)+","
    resultStr+=findBinary(guess/2,guess,number,sign)
    return resultStr

def findBinary(lowerBound,uperBound,number,sign):
    resultStr=""
   
    while(lowerBound +1< uperBound):
      mid=(lowerBound+uperBound)/2
     
      if mid == number:
        resultStr+=str((-1)**sign*mid)
        return resultStr
      elif mid < number:
        
        resultStr+=str((-1)**sign*mid)+","
        
        lowerBound = mid 
        
      else:
        
        resultStr+=str((-1)**sign*mid)+","
        print resultStr
        uperBound = mid 
        
    if lowerBound == number:
      resultStr += str((-1)**sign*lowerBound)
      return resultStr
    if uperBound == number:
      resultStr += str((-1)**sign*uperBound)
      return resultStr
   

print unboundedNumberGuessing(0)

print unboundedNumberGuessing(1)
print unboundedNumberGuessing(2)
print unboundedNumberGuessing(3)
print unboundedNumberGuessing(4)
print unboundedNumberGuessing(42)
print unboundedNumberGuessing(61)
print unboundedNumberGuessing(13835058055282163712L)
print unboundedNumberGuessing(-13)
print unboundedNumberGuessing(13)


'''def unboundedNumberGuessing(n):
  sign =0
  if n<0: sign =1
  number=abs(n)
  previous=0
  guess =1
  returnString="0,"
  while (number>guess or guess !=number):
    mid = (previous + guess)/2.0
    if mid == number:
      returnString+=str(mid*(-1)**sign)
      return returnString
    returnString+=str(guess*(-1)**sign)
    returnString+=","
    print (previous,guess,returnString)
    previous=guess
    guess*=2
  return returnString
print unboundedNumberGuessing(0)
print unboundedNumberGuessing(-1)
print unboundedNumberGuessing(1)
'''