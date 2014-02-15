# Enter these expressions and statements into the interpreter.
# Predict the results of each line before advancing to the next line.
# Be precise.

print 3*3/4, 3/4*3, 3**3/4

x = 1000*1000*1000*1000 # one trillion
x
print x
type(x)
x /= 1000*1000*1000 # divide by one billion 
x
x/1000
x

x = 123
x.bit_length()

import sys
x = sys.maxint  # 2^31-1, or 2147483647
x.bit_length()
x
x+1
-x
-(x+1)
-x-1
-x-2

not 43
not 43/99
43/99 or 99/43 or 99

print 0xff
print hex(255)
print 255 == 0xff
print 255 == hex(255)

print "-----------------"
x = 5
print 42 if (x == 5) else 99
print ((x == 5) and 42) or 99
print ((x == 5) * 42) + ((x != 5) * 99)
print 42 + (x/6)*(99-42)
print 42 + ((x-5)*(99-42))

print "-----------------"
x = 6
print 42 if (x == 5) else 99
print ((x == 5) and 42) or 99
print ((x == 5) * 42) + ((x != 5) * 99)
print 42 + (x/6)*(99-42)
print 42 + ((x-5)*(99-42))