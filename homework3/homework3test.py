#homework3 test

'''
def f(s):
    for x in xrange(1,4):
        spec = "%%0.%df" % x
        print (x,spec)
        print spec % float(s)
f("12.45645")

## 
def g(s):
    result = ""
    for i in xrange(len(s)):
        for j in xrange(i):
            if (s[j] > s[i]):
                result += s[j] + s[i]
    return result
print g("aebdc")

def h(s, t):
    assert((len(t) == 2) and ("0" not in t) and (t[1] > t[0]))
    count = 0
    for r in s.split(","):
        assert(r == t)
        count += 1
    return (count == int(t[0]) + int(t[1]))


print h("12,12,12","12")


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

print largestNumber("I saw 3 dogs, 17 cats, and 14 cows!")
print largestNumber("One person ate two hot dogs!")
print largestNumber("")

def f4(s,t):
	print t[2]
	print str(len(t))
	return (t[2] == str(len(t))) and (s[1:len(s)] == t[4:0:-1])
s='14352'
t='12534'
print f4(s,t)


def f5(s):
    assert("-" not in s)
    t = ""
    ok = False
    try:
        try:
            for i in xrange(len(s)):

                t += str(int(s[i]))
                t += "-"
                print t3
        except:
            for i in xrange(2,-2,-1):
                t += str(2/i)
    except:
        ok = (t == "3-4-12")
    return ok'''




def isKaprekar(n):
    if n==0 or n==1 :return True

    squareNumber  =  n**2
    stringNumber  =  str(squareNumber)
    stringLength  =  len(stringNumber)
    if stringLength <2 : return False
    leftPart      =   stringNumber[0:stringLength/2]
    rightPart     =   stringNumber[stringLength/2:]
    print squareNumber
    print leftPart
    print rightPart

    if(n == int(leftPart) + int(rightPart)):
        return True
    return False

print isKaprekar(45)
       # print 'x'+str(x)+' ',

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
                                      s!GoS
""")

    print "Passed!"





