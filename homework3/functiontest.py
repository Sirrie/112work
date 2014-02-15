#python test2
'''import string
def plainTextPreProcess(plaintext):
    processedText = ""
    for c in plaintext:
      if c in string.ascii_letters :
        processedText += c.upper()

    return processedText



print plainTextPreProcess("Go  ME!")
'''
import string
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


# we need to remove none letter onese 
# we need to change ever letter into uppercase
def plainTextPreProcess(plaintext):
    processedText = ""
    for c in plaintext:
      if c in string.ascii_letters :
        processedText += c.upper()
    return processedText
#  compute the encrypt offset
def computeOffset(charToEncrypt,charOffset):
    start= ord("A")
    afterEncrypt = (ord(charToEncrypt)-start+charOffset)%26+start
    return chr(afterEncrypt)



print  encrypt("TT I love!!","ccdeeeee")
print  encrypt("CMU Time Zone ~","sdkjffU")

print  encrypt("Hello world! My life","abbbbbcde")