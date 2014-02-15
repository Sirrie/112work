# hw3.py
# siyuChen+ siyuchen+Section N

"""
Place your manually-graded materials here

1 Quick Answer:
    a:   advantage 1: form from an overview of the whole problem, all detailed problems are regarted as "black boxes", these make it easier to manipulate
          advantage 2: by defineing the applicaiton comes together at a high level, lower lever work can be self-contained, it's eaiser to test
    b:  it will confused you when you read your code again after sever weeks
    c:  decrease the opportunities for you to think about the edge cases which is very important especially in future engnieering work
    d:   for experssion 1, c is A~Z and a~z;
            expression 2, c is A~Z and a~z and \ ]^_`;
            expression 3, c is A~z and a~z;
            expression 4, c is A~Z
            so expression 1 is equivalent to expression 3
2: code tracing :
    x loop from 1 to 3; we can get the following char:
         x      spec      print 
         1      %0.1f     12.5
         2      %0.2f     12.46
         3      %0.3f     12.456
    
    the function of the code is to find the previous alpha that is larger than the present one as well as the present one, so the out put should be : ebedecdc

3: rasoning over code:
   the function of the code is to find t=AB with length 2, and there is no 0 in t and the t[0]<t[1], for every element in s, it equals t, and the counter loops maximum time =A+B 
   so input could be ("12,12,12","12")

4: to slove this problem :
 we can do in this way:
 def largestNumber(s):
    hasDigit=False
    maxNumber=0
    if not s or len(s)==0: return None
    for str in s.split():
        if str.isdigit():
            hasDigit=True
            if int(str)>maxNumber:
                maxNumber=int(str)
    if not hasDigit:
        return None
    return maxNumber

5: #1 string problem:
    a: s is ab_c\d len(s)=6, n=6 , k=2 where it is whitespace, s.find("b")=1, s.find("e")=-1, xshould be 2
    b:  as there is + and - the first part of fmt should be %+d, and as ther are abc the second part should be "abc" then the length of loat is 3 so it should be 3.1f so the fmt should be "%+d abc %3.1f"
    c:  s[0] should be "d" and s has 5 elements, i range from 1 to 4 with step 1, the ASCII ord of S[i] should only larger than the s[i-1] in ASCII oder so s[1]=e, s[2]=f,s[3]=g,s[4]=h. so the s should be "defgh"
    d:  t[4:0:-1] there are 4 elements, so len(s) is 5, so t[2] is '5'
        and s, should be part of t's reverse version, s[1:5] is t[4:0:-1] so we should do in this way: s can be '14352' and t can be '12534'
    e:  s has no "-" when s[i] is not digit,so this try crash, so we need to move to the outside try and except, so we need to go to t=t+ str(2/2), when i==0, the outside try crash we go to the result, so t=3-4-12,and we find the s[0]=3,s[1]=4,s[3]!=digit 
        so s could be '34a'

"""

######################################################################
# Place your solutions and test functions here!
######################################################################

def nthNearlyPalindromicPrime (n):
    found   =   -1
    guess   =   3
    while(found < n):
        guess += 2;
        if isNearPalindromic(guess) and isPrime(guess):
            found += 1;
    return guess

##use helperfunction to find if number N is NearPalindromic
##first transform intger into string using string method to find the same pair of elements, keep a counter to record it, if the counter is leq to 1 so we find this is NearPalidromic
def isNearPalindromic(n):
    samePair   =  0
    strNumber  =  str(n)
    counter    =  0
    numLength  =  len(strNumber)
    for i in xrange(numLength / 2):
        if strNumber[i] != strNumber[numLength-1-i]:
            counter += 1
    if counter  ==  1:
        return True
    else:
        return False

# isPrime from Kosibe's in class funciton
def isPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = int(round(n**0.5))
    for factor in xrange(3,maxFactor+1,2):
        if (n % factor == 0):
            return False
    return True



def testNthNearlyPalindromicPrime ():
    print "Testing nthNearlyPalindromicPrime()...",
    
    assert(nthNearlyPalindromicPrime(0) == 13)
    assert(nthNearlyPalindromicPrime(1) == 17) 
    assert(nthNearlyPalindromicPrime(2) == 19)
    assert(nthNearlyPalindromicPrime(3) == 23)# replace with your own tests!
    print "Passed!"

def nthCarolPrime(n): 
    found = -1
    guess = 2
    while(found < n):
        if(isPrime((2**guess-1)**2-2)):
            found += 1
        guess +=1
    return (2**(guess-1)-1)**2-2


    

def testNthCarolPrime():
    print "Testing nthCarolPrime()...",
    assert(nthCarolPrime(0) == 7)
    assert(nthCarolPrime(1) == 47)
    assert(nthCarolPrime(2) == 223)
    assert(nthCarolPrime(3) == 3967)
    assert(nthCarolPrime(4) == 16127)
    assert(nthCarolPrime(5) == 1046527) # replace with your own tests!
    print "Passed!"
##  from two direction to find the nearest Kaprekar Number, compare the difference of the two kaaprekar return the one with smaller value
def nearestKaprekarNumber(n):
    if isKaprekar(n): return n
    smallerKaprekar = n-1
    largerKaprekar  = n+1
    while(smallerKaprekar > 0 and not isKaprekar(smallerKaprekar) or not isKaprekar(largerKaprekar)):
        print  "in loop"
        if not isKaprekar(smallerKaprekar): 
            smallerKaprekar += 1
        if not isKaprekar(largerKaprekar):
            largerKaprekar +=  1
    leftDifference = n - smallerKaprekar
    rightDifference= largerKaprekar - n
    if leftDifference > rightDifference:
        return smallerKaprekar
    else:
        return largerKaprekar



def isKaprekar(n):
    squareNumber  =  n**2
    stringNumber  =  str(squareNumber)
    stringLength  =  len(stringNumber)
    leftPart      =   stringNumber[0:stringLength/2]
    rightPart     =   stringNumber[stringLength/2:]
    if(squareNumber == int(leftPart) + int(rightPart)):
        return True
    return False

def testNearestKaprekarNumber():
    print "Testing nearestKaprekarNumber()...",
    print  "hererere"
    print nearestKaprekarNumber(49)
    print  "lkjskdjfksdf"
    assert(nearestKaprekarNumber(49) == 45)
    assert(nearestKaprekarNumber(51) == 55) 
    assert(nearestKaprekarNumber(222)== 297)

    # replace with your own tests!
    print "Passed!"
    # keep a temp to define the message to compy to pattern
    # according to 3 2 cases: if there is * compy from message otherwise compy from pattern
def patternedMessage(message, pattern):

    copyTemp  = 0
    returnStr = ""
    message   = message.replace(" ","")
    mLen      = len(message)
    for m in pattern.splitlines():
        for temp in range(len(m)):
            
            if m[temp] == "*":
                returnStr += message[copyTemp%mLen]
                copyTemp  +=1
            else:
                returnStr += m[temp]    
        returnStr +="\n"
    return returnStr

def testPatternedMessage():
    print "Testing patternedMessage()...",

    assert(patternedMessage("Go Pirates!!!", """
***************
******   ******
***************
""")=="""GoPirates!!!GoP
irates   !!!GoP
irates!!!GoPira""") 

    assert(patternedMessage("Go Steelers!", """

                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ '$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
'$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  '$$$
   '$$$'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$o
   o$$'   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$' '$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$'$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$'
 ''''       $$$$    '$$$$$$$$$$$$$$$$$$$$$$$$$$$$'      o$$$
            '$$$o     '$$$$$$$$$$$$$$$$$$'$$'         $$$
              $$$o          '$$'$$$$$$'           o$$$
               $$$$o                                o$$$'
                '$$$$o      o$$$$$$o'$$$$o        o$$$$
                  '$$$$$oo     '$$$$o$$$$$o   o$$$$'
                     '$$$$$oooo  '$$$o$$$$$$$$$'
                        '$$$$$$$oo $$$$$$$$$$
                                '$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$'
                                      '$$$'
""")=="""
                          GoSteelers!GoSteeler
                      s!GoSteelers!GoSteelers!GoS
                   teelers!GoSteelers!GoSteelers!GoS         te   el er
   s ! Go        Steelers!GoSteelers!GoSteelers!GoSteel       er s! GoSt
ee l e rs      !GoSteeler    s!GoSteelers!    GoSteelers       !GoSteel
ers!GoSte     elers!GoSt      eelers!GoSt      eelers!GoSt    eelers!G
  oSteele    rs!GoSteele      rs!GoSteele      rs!GoSteelers!GoSteeler
  s!GoSteelers!GoSteelers    !GoSteelers!G    oSteelers!GoSt  eele
   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSteel     ers!
    GoS   teelers!GoSteelers!GoSteelers!GoSteelers!GoSteelers     !GoSt
   eele   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSt       eele
   rs!    GoSteelers!GoSteelers!GoSteelers!GoSteelers!Go Steelers!GoSteele
  rs!GoSteelers  !GoSteelers!GoSteelers!GoSteelers!GoS   teelers!GoSteelers
  !GoSteelers!G   oSteelers!GoSteelers!GoSteelers!Go     Steel
 ers!       GoSt    eelers!GoSteelers!GoSteelers!G      oSte
            elers     !GoSteelers!GoSteelers!         GoS
              teel          ers!GoSteel           ers!
               GoSte                                elers
                !GoSte      elers!GoSteele        rs!Go
                  Steelers     !GoSteelers!   GoStee
                     lers!GoSte  elers!GoSteeler
                        s!GoSteele rs!GoSteel
                                ers!GoSteele
                                    rs!GoSteeler
                                     s!GoSteeler
                                      s!GoS""")
    print "Passed!"


def encrypt(plaintext, password):
    return 42

def testEncrypt():
    print "Testing encrypt()...",
    assert(False) # replace with your own tests!
    print "Passed!"

def decrypt(ciphertext, password):
    return 42

def testDecrypt():
    print "Testing decrypt()...",
    assert(False) # replace with your own tests!
    print "Passed!"

######################################################################
##### ignore_rest: The autograder will ignore all code below here ####
######################################################################

def testAll():
    testNthNearlyPalindromicPrime()
    testNthCarolPrime()
    testNearestKaprekarNumber()
    testPatternedMessage()
    testEncrypt()
    testDecrypt()

def main():
    testAll()

if __name__ == "__main__":
    main()