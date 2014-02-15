'''


def longestDigitRun(n):
	counter=0;
	maxcounter=0;
	prev=None;
	while(n>0):
		cur=n%10;
		if(prev == cur):
			counter+=1;
		else:
			maxcounter=math.max(maxcounter,counter)
			counter=0

		prev=cur
		n /=10
	return maxcounter
## first do something

## at the beginning of the loop you don
## update at last
print longestDigitRun(10)
print longestDigitRun(1231231555555555)

def isImpolite(x):


def nthImpolitenumber(x):
	found=0
	guess=0
	while(found<x):
		if(isImpolite(guess)):
			found++
		guess++
	return guess

'''

from Tkinter import *
root = Tk()
canvas = Canvas(root, width=300, height=200)
canvas.pack()
canvas.create_oval(50, 50, 250, 150, fill="yellow")；；
root.mainloop()