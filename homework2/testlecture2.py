#testlecture2
def isPerfect(n):
	if(n<1) or (type(n)!=int):
		return False;
	elif n==1 :
		return True
	sum=0;
	for x in range(1,n):
		if n%x==0:
			sum+=x;
	return sum==n;


assert(isPerfect(0)==False)
assert(isPerfect(1)==True)
assert(isPerfect(1.0)==False)
assert(isPerfect(28)==True)
assert(isPerfect(28.0)==False)