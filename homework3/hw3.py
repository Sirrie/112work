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

you cannot use split to do that !!!!!!!!!!!


import math
def largestNumber(s):
  maxNumber=None
  temp=""
  if len(s) ==0 or s is "": 
    return None
  for i in range(len(s)):

    if s[i].isdigit():
      temp +=s[i]
    elif temp is not "":
      maxNumber=max(int(temp),maxNumber)
      temp=""
  return maxNumber




  

5: #1 string problem:
    a: s is ab_c\d len(s)=6, n=6 , k=2 where it is whitespace, s.find("b")=1, s.find("e")=-1, xshould be 2
    b:  as there is + and - the first part of fmt should be %+d, and as ther are abc the second part should be "abc" then the length of loat is 3 so it should be 3.1f so the fmt should be "%+dabc%3.1f"
    c:  s[0] should be "d" and s has 5 elements, i range from 1 to 4 with step 1, the ASCII ord of S[i] should only larger than the s[i-1] in ASCII oder so s[1]=e, s[2]=f,s[3]=g,s[4]=h. so the s should be "defgh"

      every time it plus i so the total length should be 

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
def testNearPalindromic():
    print "Testing NearPalidromic()...",
    assert(isNearPalindromic(11)==False)
    assert(isNearPalindromic(13)==True)
    assert(isNearPalindromic(17)==True)
    print "Passed!"

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

def testisPrime():
    print "Testing isPrime()...",
    assert(isPrime(11)==True)
    assert(isPrime(13)==True)
    assert(isPrime(17)==True)
    assert(isPrime(19)==True)
    print "Passed!"


def testNthNearlyPalindromicPrime ():
    print "Testing nthNearlyPalindromicPrime()...",
    
    assert(nthNearlyPalindromicPrime(0) == 13)
    assert(nthNearlyPalindromicPrime(1) == 17) 
    assert(nthNearlyPalindromicPrime(2) == 19)
    assert(nthNearlyPalindromicPrime(3) == 23)# replace with your own tests!
    print "Passed!"
# compute the Carol number using the function given in wikipedia
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
  # edge case where input is non-positive we return 1 we need to change float into int
   # n = int(round(n))
    if n <= 1: 
      return 1 
    if isKaprekar(n): 
      return n
    # take into consideration we only chose the int number but input could be float

    delta=0.00000000001
    number   = int(round(n-delta))
    smallerKaprekar = number 
    largerKaprekar  = number 
    # from the number we need to find we need to go to two directions and find the one that is nearer to the target number 

    while(smallerKaprekar > 0 and (not isKaprekar(smallerKaprekar) and not isKaprekar(largerKaprekar))):
    # find one and return 

        smallerKaprekar = smallerKaprekar - 1
        largerKaprekar  = largerKaprekar  + 1   
    if (isKaprekar(smallerKaprekar) and isKaprekar(largerKaprekar)):
      leftDifference = n - smallerKaprekar
      rightDifference = largerKaprekar - n
       # ties to the smaller one  
      if leftDifference <= rightDifference :
        return smallerKaprekar
      else:
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
    if(n == int(leftPart) + int(rightPart) and int(rightPart)>0):
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
    assert(isKaprekar(55)==True)
    print  "Passed!"


def testNearestKaprekarNumber():
    print "Testing nearestKaprekarNumber()...", 
    assert(nearestKaprekarNumber(5.000000099999)==9)
    assert(nearestKaprekarNumber(4.999999999999)==1)
    assert(nearestKaprekarNumber(0.000000000001)==1)
    assert(nearestKaprekarNumber(13641234)==13641364)
    assert(nearestKaprekarNumber(28)==45)
    assert(nearestKaprekarNumber(27)==9)
    assert(nearestKaprekarNumber(2475.5)==2223)

    assert(nearestKaprekarNumber(2475.400000001)==2223)
    assert (nearestKaprekarNumber(-1) ==1)
    assert(nearestKaprekarNumber(0) == 1)
    assert(nearestKaprekarNumber(0.2)==1)
    assert(nearestKaprekarNumber(49.5)==45)
    assert(nearestKaprekarNumber(49) == 45)
    assert(nearestKaprekarNumber(51) == 55) 
    assert(nearestKaprekarNumber(222)== 297)

    # replace with your own tests!
    print "Passed!"
    # keep a temp to define the message to compy to pattern
    # according to 3 2 cases: if there is * compy from message otherwise compy from pattern
import string

#  match the message with pattern and use it to replace the none white space place in the pattern with message 

#  keep a temp to loop from and try to check whether this char is 
def patternedMessage(message, pattern):
    copyTemp  = 0
    returnStr = ""
    message   = message.replace(" ","")
    mLen      = len(message)
    # loop from the beginning and then encrypt every element one by one
    for m in pattern.splitlines():
        for temp in range(len(m)):
            if m[temp] is not " ":
                returnStr += message[copyTemp%mLen]# round through the pattern
                copyTemp  += 1
            else:
                returnStr += m[temp]    
        returnStr += "\n"
    return returnStr.strip('\n')

def testPatternedMessage():
    print "Testing patternedMessage()...",
    assert(patternedMessage("Go Pirates!!!", """
***************
******   ******
***************
""")==
"""GoPirates!!!GoP
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
""")=="""                          GoSteelers!GoSteeler
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
    assert(patternedMessage('A','\n*\n') == 'A')
    print "Passed!" 


def encrypt(plaintext, password):
    plaintext   =  plainTextPreProcess(plaintext)
    pwdLength   =  len(password)
    textLength  =  len(plaintext)
     # delete all the white space
    temp        =0     # temp to loop inorder to encrypt one char by one char
    offsetEncrpy=  ord("a")
    upperCaseOffset= ord("A")
    alphaLength  =   26
    resultText  =""
    while (temp<textLength):
      charToEncrypt   = plaintext[temp]
      charOffset      = ord(password[temp%pwdLength]) - offsetEncrpy
      if ord(password[temp%pwdLength])< offsetEncrpy:
        return "password must be all lowercase"
      charToEncrypt   = computeOffset(charToEncrypt,charOffset)
      resultText     += charToEncrypt
      temp            =temp+1
    return resultText


# we need to remove none letter elements first  
# secondely we need to change ever letter into uppercase
def plainTextPreProcess(plaintext):
    processedText = ""
    for c in plaintext:
      if c in string.ascii_letters :
        processedText += c.upper()
    return processedText
#  compute the encrypt offset
def computeOffset(charToEncrypt,charOffset):
    start= ord("A")
    alphaLength=26
    afterEncrypt = (ord(charToEncrypt)-start+charOffset)%alphaLength+start
    return chr(afterEncrypt)


def testplainTextPreProcess():
    print "Testing plainTextPreProcess()...",
    assert(plainTextPreProcess("AA df!")=="AADF")
    assert(plainTextPreProcess("as d ") =="ASD")
    assert(plainTextPreProcess("") == "")
    print  "Passed!"





def testcomputeOffset():
    print " Testing computeOffset...",
    assert(computeOffset("G",0) == "G")
    assert(computeOffset("O",25)== "N")
    assert(computeOffset("T",1) == "U")
    assert(computeOffset("E",24)== "C")
    print   "Passed!"

def testEncrypt():
    print "Testing encrypt()...",
    assert(encrypt("Go Team!","azby")=="GNUCAL")
    assert(encrypt("TT  I love!!","ccdeeeee")=="VVLPSZI")
    assert(encrypt("CMU  Time Zone ~","sdkjffU")=="password must be all lowercase")
    assert(encrypt("Hello world! My life","abbbbbcde")=="HFMMPXQUPDNZMJGG")


     # replace with your own tests!
    print "Passed!"

def decrypt(ciphertext, password):
    pwdLength   =  len(password)
    textLength  =  len(ciphertext)
    # delete all the white space
    temp        =  0     # temp to loop inorder to encrypt one char by one char
    offsetEncrpy=  ord("a")
    resultText  =""
    # loop through the whole ciphertext one char by one char and find the one that we need to crypt to
    while (temp<textLength):
      charToDecrypt   = ciphertext[temp]
      charOffset      = ord(password[temp%pwdLength]) - offsetEncrpy
      # print error messeage once we find the password has uppercase letter
      if ord(password[temp%pwdLength])< offsetEncrpy:
        return "password must be all lowercase"
      charToDecrypt   = computeOffsetDecrypt(charToDecrypt,charOffset)
      resultText     += charToDecrypt
      temp            = temp+1
    return resultText

def computeOffsetDecrypt(charToDecrypt,charOffset):
    # start means the char where we need to round back and begin with
    start        =  ord("A")
    alphaLength  =  26
    # using mod to do decrypt process and minus the charOffset then plus start to get the Decrypt number
    afterDecrypt =  (ord(charToDecrypt)-start-charOffset)%alphaLength+start
    return chr(afterDecrypt)

def testcomputeOffsetDecrypt():
    print " Testing computeOffsetDecrypt() ...",
    assert(computeOffsetDecrypt("G",0) =="G")
    assert(computeOffsetDecrypt("N",25)=="O")
    assert(computeOffsetDecrypt("U",1) =="T")
    assert(computeOffsetDecrypt("C",24)=="E")
    print  "Passed!"



def testDecrypt():
    print "Testing decrypt()...",
    assert(decrypt("GNUCAL","azby")=="GOTEAM")
    assert(decrypt("VVLPSZI","ccdeeeee")=="TTILOVE")
    assert(decrypt("HFMMPXQUPDNZMJGG","abbbbbcde")=="HELLOWORLDMYLIFE")
    #assert() # replace with your own tests!
    print "Passed!"

######################################################################
##### ignore_rest: The autograder will ignore all code below here ####
######################################################################

def testAll():
    testNthNearlyPalindromicPrime()
    testNearPalindromic()
    testisPrime()
    testNthCarolPrime()
    testisKaprekar()
    testNearestKaprekarNumber()
    testPatternedMessage()
    testplainTextPreProcess()
    testEncrypt()
    testcomputeOffset()
    testDecrypt()
    testcomputeOffsetDecrypt()

def main():
    testAll()

if __name__ == "__main__":
    main()