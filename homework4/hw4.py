# ChenSiyu + siyuchen --- Section N

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

"""
f12 hw4b:
      1: a) O(n^2)
         b) O(nlogn)
		     c) O(n)
		      d) O(logn)
		      e) O(n)
		      f)  O(n)
      2: in worst case, binary guess request log2(1000)= 9.965784 ceil to 10
           from 1 to 1 billion  log2(1000000)= 19.93 ceil to 20, from 1 to 1 trillion log2(1000000000) = 29.897 ceil to 30
      3: (1,4,6,8,2,3,5,7)
      4:    (2,3,4,1,5)
            (2,3,1,4,5)
            (2,1,3,4,5)
            (1,2,3,4,5)
      5: the big O runtime for foo(n) could be O(nlogn) because we need to denote that when every time we times 2 of the n, the running time increase near to 3 times of previous, which is larger than 2 but less than 3, we could guess the complexity could be nlogn

      6:  understand the work
      7:  in the worst case of selection sort, that all the elements are reversed listed, so we need to spend O(n^2) time on it. just like  5,4,3,2,1, we need to loop through the whole list which is O(n) and every time put the largest to the end which takes O(n)


          in the worst case of mergesort ,the time is O(nlogn), we have logn times to merge, and everytime we sort the sub elements that need to be merged we need to take O(n) times, so the total time is O(nlogn)
          just like 8,7,2,1,4,3,6,5. 
            for n lists of elements to sort 
               3n  2 2 2 2
               3n   4   4
               3n     8       
                n=2^k  so the total is 3n * (# of paths) = 3nLogn so it's O(nlogn)

             
         

      8: 





          Bublesort: O(n^2)
             test data :  size   time 
                          1000    0.006
                          10000   0.375
                          100000  38.555



          Selectionsort: O(n^2)
              test data: size time 
                        1000    0.004
                        10000   0.221 
                        1000000 22.156

          InsertionSort: O(n^2)
              test  data: size  time 
                          1000   0.009
                          10000  0.140
                          100000 13.614


          QuickSort    : O(nlogn)
              test  data: size  time 
                          1000  0.002
                          10000 0.005
                        100000  0.021
          Mergesort :   O(nlogn)
             test  data: size  time 
                        100000  0.032
                        10000   0.003
                        1000     0

      9:  A  O(N)   becase T = 2N +5 can escape the 5
      	  B  O(N)   because N grows quicker than logN, we ignore  logN 
      	  C  O(N^3) because N**3 grows the fastest in T we ignore rest N**2 and logN
      	  D  O(N^2) becase T=30 * N**2
      	  E  O(N)   T= 13N 
      	  F  O(logN) everytime mergesort grows to double  size one, so we need to take Log N time to get 

      10:
        	a:O(n^2)
        	b:O(nlogn)
        	c:O(n^2)
        	d:O(n)
        	e:O(logn)
        	f:O(nlogn)

          def f0(n):
              count = 0
              for x in xrange(n):               O(n)
                  for y in xrange(1, n):        O(n)
                      count += 1                O(1)
              return count                      total isO(n^2)

          def f1(n):
              count = 0
              for x in xrange(n):               O(n)
                  for y in xrange(1, x):        O(n) worst case 
                      count += 1                O(1)
              return count                      total  is  O(n^2)

          def f2(n):
              count = 0
              for x in xrange(1,n/2, 2):         O(n/2)
                  for y in xrange(1, x/2):       O(n/4)
                      count += 1                  O(1)
              return count                       toal is O(n^2)

          def f3(n):                             
              count = 0
              for x in xrange(1,n):                O(n)
                  for y in xrange(1, n, n/100):    O(1)
                      count += 1
              return count                         total  O(n)

          def f4(n):
              count = n**2 # note: not setting count = 0
              while (n > 0):                         O(log(n))
                  count += 1                         O(1)
                  n /= 2                             O(1)
              return count                           total O(logn)

          def f5(n):                             
              count = 0
              for x in xrange(1, n):                 O(n)
                  count += f4(n)                     O(logn)
              return count                           O(nlogn)

   A3: 


         def h1(x, y):
              # interesting note: this is basically the ancient Egyptian multiplication algorithm!
              # And it only uses addition to multiply!  Cool!
              assert((x>0) and (y>0))
              (hi, lo) = (max(x,y), min(x,y))               O(1)
              (product, addend) = (0, hi)                   O(1)
              while (lo > 0):                               O(logN)
                  if (lo&1): product += addend              O(1)
                  addend += addend                          O(1)
                  lo = lo >> 1                              O(1)
              return product                                total O(logN)

          def h2(x, y):
              assert((x>0) and (y>0))
              result = 0
              for m in xrange(x):                           O(N)
                  for n in xrange(y):                       O(N)
                      result += 1                           O(1)
              return result                                 total O(N^2)

          def h3(x, y):
              assert((x>0) and (y>0))
              (hi, lo) = (max(x,y), min(x,y))
              # hint: (x-m)(y-m) = xy - m(x+y) + m**2
              result = 0
              while (lo > 10):                          O(n/10)
                  result += 10*(lo+hi) - 100            O(1)
                  (lo, hi) = (lo-10, hi-10)             O(1)
              while (lo > 0):                           O(1)
                  (lo, result) = (lo-1, result+hi)      O(1)
              return result                             total O(n)

          def h4(x, y):
              assert((x>0) and (y>0))                    O(1)
              (hi, lo) = (max(x,y), min(x,y))            O(1)
              product = 0                                O(1)
              for i in xrange(lo.bit_length()):          O(logN)
                  if (lo & (1<<i)): product += hi<<i     O(1)
              return product                             total O(logN )

   Quiz 3:
         def r1(n):
              for x in xrange(0, 2**n, 2**n/n**2):
                  print "This may print a lot!"
           
          def r2(n):
              s = "Yippee!" * n                    O(n)
              for x in xrange(len(bin(n))):        O(logn)
                  c = chr(ord('a') + x%26)         O(1)
                  print s.count(c)                 O(n)
                                                   O(nlog n)
           
          def r3(n):
              x = y = 0   # hint: note that this is outside both loops!
              while (x < n):                        O(logn)
                  while (y < n):                    O(logN)
                      print "y",                     O(1)                  
                      y += 3                         O(1)
                  print "x",                         O(1)
                  x += 4                             O(1)
                                                     total O(logn *logn )
           
          def r4(n):
              for x in xrange(n):                    O(n)
                  for y in xrange(-n, n):            O(n)
                      for z in xrange(100):           O(1)
                          print (x,y,z),
              for x in xrange(n):                     O(n)
                  print "huzzah!",                    O(1)

                                                    total O(n^2)
           
          def r5(n):
              step = int(round(n**0.5))              O(1)
              for x in xrange(123, n**2, step):      O(n**1.5)
                  print "Go team!",                  O(1)
                                                    total O(n**1.5)


"""      


######################################################################
# Place your autograde solutions below here
######################################################################

def findZeroWithBisection(f,x0,x1,epsilon):
  result = None
  # loop when we havn't find the result of the function 
  while(f(x0)*f(x1)<0 and abs(x0-x1)>epsilon):
		mid=x0+(x1-x0)/2.0 # incase there is overfloat
		if f(mid) == 0: 
			result = mid
		elif f(mid) > 0:
			x1 = mid
		else:
			x0 = mid
  if abs(x0-x1)<epsilon :
    result = (x0+x1)/2.0
  return result


def almostEqual(d1, d2):
    epsilon = 0.000001
    return (abs(d2 - d1) < epsilon)

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
    
    # edge case 1 where guess == number directly return
    if guess == number :
      resultStr +=str((-1)**sign*guess)
      return resultStr
    # edge case 2 where we ned to binary search 
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

def justifyText(text,number):
    textProcessed=replaceWS(text)

  

import string
# set a flag to sign that which digit shoul be replaced by 
def replaceWS(text):
  stringCount=text[0]
  for x in range(1,len(text)):
    if (text[x] in string.whitespace or text[x]=="\n") and (text[x-1].isalpha()):
      stringCount+=str(1)
    elif (text[x] in string.whitespace or text[x]=="\n" )and (text[x-1] in string.whitespace or text[x]=="\n"):
      stringCount+=str(2)
    else:
      stringCount+=text[x]
  stringReshape=""
  for x in range(len(stringCount)):
    if stringCount[x]== "1":
      stringReshape+=" "
    elif stringCount[x]=="2":
      pass
    else:
      stringReshape +=stringCount[x]
  return stringReshape

######################################################################
##### ignore_rest: The autograder will ignore all code below here ####
######################################################################

def testfindZeroWithBisection():
  print "Testing findZeroWithBisection ......"
  print "use bisection to approximate x where x**5 == 2**x"
  def f3(x): return x**5 - 2**x # f(1)<0, f(2)>0
  x = findZeroWithBisection(f3, 1, 2, 0.000000001)
  print " x =", x                              # prints x = 1.17727855081
  print " check: x**5 - 2**x =", (x**5 - 2**x)

  print "use bisection to approximate sqrt(2):"
  def f1(x): return x*x - 2 # root at x=sqrt(2)
  x = findZeroWithBisection(f1, 0, 2, 0.000000001)
  print " x =", x                # prints  x = 1.41421356192
  print " check: x**2 =", (x*x)  # prints  check: x**2 = 1.99999999871 (really close!)

  print "use bisection to approximate phi (the golden ratio):"
  def f2(x): return x**2 - (x + 1) # root at x=phi
  x = findZeroWithBisection(f2, 0, 2, 0.000000001)
  print " x =", x                  # prints x = 1.61803398887
  phi = (1 + 5**0.5)/2             # the actual value (to within Python's floating point accuracy)
  print " check: x/phi =", (x/phi) # prints check: check: x/phi = 1.00000000007 (nice!)
  assert(almostEqual(findZeroWithBisection(f1,0,2,0.000000001),1.41421356))

  assert(almostEqual(findZeroWithBisection(f1,0,4,0.000000001)**2,2))
 

def testUnboundedNumber():
  print "testing unboundedNumberGuessing ...."
  assert(unboundedNumberGuessing(0)=="0")
  assert(unboundedNumberGuessing(1)=="0,1")
  assert(unboundedNumberGuessing(-1)=="0,-1")
  assert(unboundedNumberGuessing(42)=="0,1,2,4,8,16,32,64,48,40,44,42")
  print unboundedNumberGuessing(-13)
  assert(unboundedNumberGuessing(-13)=="0,-1,-2,-4,-8,-16,-12,-14,-13")
  print "Passed!"


def testAll():
  testfindZeroWithBisection()
  testUnboundedNumber()
def main():
  testAll()
  

if __name__ == "__main__":
  main()




