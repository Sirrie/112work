#hw4 solution
def findZeroWithBisection(f,x0,x1,epsilon):
	if(f(x0)==0):return x0
	if(f(x1)==0):return x1
	if(f(x0)*f(x1)>=0):return 
	middle = (x0+x1)/2.0
	fMiddle= f(middle)
	while(abs(x0-x1)>epsilon):
		if (f(x0)*fMiddle<0):
			x1=middle
		else:# zero between middle and x1
			x0 = middle
		middle = float(x0+x1)/2
		fMiddle=f(middle)
	return middle


def unboundedNumberGuessing(n):
	s = "0"
	sign=0
	guess=1
	if(n == 0):return s
	if(n <0):
		sign=1
	number=abs(n)
	while(guess<number):
		s+=",%d" %guess
		guess*=2
	if guess/2 == number:
		s+="number"
		return s
	s+=BS(guess/2,guess,number,sign)
	return s

def BS(lB,UB,n,sign):
	s=""
	while (lB<UB):
		mid=(lB+UB)/2
		if mid == n:
			s+=",%d" %mid
			return s
		elif mid >n:
			s+=",%d" %mid
			UB=mid
		else:
			s+=",%d" %mid
			lB=mid +1
	return s
print unboundedNumberGuessing(0)
print unboundedNumberGuessing(42)


#you should think clearly what each step is doing before coding 



