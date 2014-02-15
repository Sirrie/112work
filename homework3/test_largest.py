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

print largestNumber("adb4444f2222")
print largestNumber("as 13 sdf 45 a ")