def kthDigit(n, k):
    # devide it into different small questions 
    number = abs(n)
    # we move right k steps and then we find the kth digit by mod
    for x in range(0,k):
        number = number/10;
    return number%10

def digitCount(n):
    # count the digit number of an int
    # if it is 0, we just return 1
    number=abs(n)
    if (n==0): return 1
    # otherwise we use counter to count the number of the digits in it using loop once we find the digit is not zero we end the loop
    counter=0
    while(number != 0):
        counter += 1;
        number = number/10;
    return counter

def isFull(board):
    # once there is some digit not equals to 8 return False
    # else we should return True
    # if the input is str which means there is error infomation that means there is error but in other edge cases 
    if type(board) == str: return False
    digit_number=digitCount(board)
    for x in range(0,digit_number):
        if kthDigit(board,x) == 8: return False
    return True

print "Testing isFull()...",
assert(isFull(888888) == False)
assert(isFull(121888) == False)
assert(isFull(812188) == False)
assert(isFull(888121) == False)
assert(isFull(212122) == True)
assert(isFull(212212) == True)
for x in xrange(-8,88888,8):
    if not isFull(x) and x/100<20 :print x, "  sdfs",isFull(x)
print "Passed!"