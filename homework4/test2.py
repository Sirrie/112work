






texttext = """\
We hold these truths to be self-evident:  that all men are created equal;
that they are endowed by their Creator with certain unalienable rights;
that among these are life, liberty, and the pursuit of happiness."""
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


print replaceWS(texttext)