# File and Web Input/Output in Python
# from Kozibe's lecture notes
import urllib
import os

def readFile(filename, mode="rt"):
    # rt stands for "read text"
    fin = contents = None
    try:
        fin = open(filename, mode)
        contents = fin.read()
    finally:
        if (fin != None): fin.close()
    return contents

def writeFile(filename, contents, mode="wt"):
    # wt stands for "write text"
    fout = None
    try:
        fout = open(filename, mode)
        fout.write(contents)
    finally:
        if (fout != None): fout.close()
    return True

print "*************************************"
# print "Trying to delete the old joke file...",
# if (os.path.exists("joke.txt")):
#     try:
       
#         print "Success!"
#     except:
#         print "Error, could not delete joke file!"
# else:
#     print "(No old joke file to delete!)"

# print "*************************************"
print "Trying to read the file when it's not yet there..."
try:
    s = readFile("Files/joke.txt")
    print s
except:
    print "The file does not exist yet (as we hoped!)"

print "*************************************"
print "Now we'll save the file (to create it)..."
contents = "[(89,'BOb'),(90,'Teddy'),(80,'Wenny')]"
writeFile("Files/joke.txt", repr(contents))
try:
    s = readFile("Files/joke.txt")
    print s
except:
    print "The file does not exist yet (which would be strange now!)"

print "*************************************"
print "Now we'll read the file again, now that it's there..."
try:
    s = readFile("Files/joke.txt")
    print s
    print eval(s),"differences"
except:
    print "The file does not exist yet (as we hoped!)"

