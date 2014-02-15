#quiz4_practice
import string
def capitalizeFirstLetters(s):
	if s is None or len(s)==0:
		return ""
	result=s[0].upper()
	beforeIsSpace=False
	for i in range(1,len(s)):
		if beforeIsSpace and s[i].isalpha():
			result+=s[i].upper()
			beforeIsSpace=False
			continue
		if s[i] ==" ":
			beforeIsSpace=True
		if s[i] in string.punctuation:
			beforeIsSpace=False
		result+=s[i]
	return result

print capitalizeFirstLetters("don't do that (pleae)")

# attention: puncutation jdugement and case devide


def interleave(s1,s2):
    result=s1[0]+s2[0]
    if len(s1)<=len(s2):
    	result+=s1[1:]+s2[1:]
    else:
    	result+=s2[1:]+s1[1:]
    return result

print interleave('pto','yhn')
print interleave('a#','cD!f2

def mostFrequentLetter(s):
	count=0
	
