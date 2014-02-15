# hw2.py
# Chen Siyu+ siyuchen+ SectionA

"""
   ** Place your manually-graded (Reasoning Over Code) solutions here!  **
   ** Note that so long as you place them inside the triple-quotes,     **
   ** you do not need to place a # sign for a comment before each line! **
  1: quick answer:

       a: canvas.create_oval(145,145,155,155,outline="black",width=2)
       b: SE means the south east,to show the text it is anchored to the south and to the east. 
       c: in DeMorgan's Law not(A or B )<=>(not A and not B) therefore, this formula equals:( not f(x) and g(y))
       d: def f(x):
            b=0;
            for x xrange(-x,x,3):
                b+=g(a);
            return b
   2: code tracing:
      we can do it in this way: put evey element in a box:
      x, y ,z, m, when every we go a loop, we will find the result should be print
      12 4  2  0  z=0;z<12;z+=4 should print A because  x%z==0 m=1 and 2 because 2%3 =2
                1  should print  C  because 2%3 !=2
            6   1  should print C because 6%3 !=2
            10  1  should print B and C because y+z=14>12 and 10%3!=2

        the final output result: A 2 C B C

    Similarly, we can do like this:
          y ranges from x to -x and bigger than -x, the step is -2
      x    y       result
      -1   none         -1 :
      1    1             1 : 1
      3    3,1,-12       3 : 3 1 -1

      so we get the output as listed:

       -1 :
        1 : 1
        3 : 3 1 -1

3 rasoning  over code:
   f(x,y)   we need not assert so both x and y are int and z should be 10 so we should jump from the condition x=y+40, so we could know that there is a pair (x,y)=(41,1)is the solution

   g(z)    total should be 10 and z should be 0, there are 5 loops, as y only count the loop time in range ( 0,z,2) so z should be 10, 

4 free response:
// because 1 is a strange case wherer 1 is inclusive however 1itself is exclusive  but I define 1 as isPerfect
      def isPerfect(n):
    if (n<1) or (type(n)!=int): 
        return False;
    elif n==1:
        return True;
    sum=0;
    for x in range(1,n):
        if n%x==0:
            sum+=x;
    return sum==n;
5 
  this will print 


  53
        because when tracing back, we find (y,f,g)=(f(g(3)),f(g(3))/7,f(g(3))%5),therefore, we need to compute g(3) which equales to f(1)*3/2, for f(1)=1+2*f(0) where f(0)=1, so f(1)=1, f(2)=2+2*f(1) f(3)=3+3*f(2) f(4)=4+4*f(3)=42, so (y,f,g)=(42,6,2), the return result equals to y+f+g+3= 42+6+2+3    =53 as the printed result

  44   because for 57*15>0, (x,y,z)=(15/(2+1),57/(2+0),72) =(5,28,72)
                   5*28>0 ,  (x,y,z)=(28/(2+5),5/(2+1),28+5-72)=(4,1,-39)
                   4*1>0,    (x,y,z)=(1/(2+4),4/(2+1),4+1+39)=(0,1,44)
                so return 44 and print this 44
















"""

######################################################################
# Place your non-graphics solutions here!
######################################################################

def makeBoard(moves):
    board=0
    for x in range(0,moves):
        board=10*board+8
    return board
# start a Board and make all the digits to 8 according to the moves number
    
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
'''
     n=abs(n)
     counter=1
     while(True):
        if(n/10**counter>0):
            counter+=1
    return counter
'''


def kthDigit(n, k):
    # devide it into different small questions 
    number = abs(n)
    # we move right k steps and then we find the kth digit by mod
    for x in range(0,k):
        number = number/10;
    return number%10

def replaceKthDigit(n, k, d):
    # step 1 set the Kthdigt to 0
    number = n
    kth_Digit = kthDigit(n,k);
    number = number-kth_Digit*10**k;
   
    # step 2 right shift the target digit to make an integer to set the kth digit to d
    replace_number = d*(10**(k));

    return number+replace_number

    # another solution :
    # result=0
    # for i in xrange(max(digitCount(n),k+1)):
    #      if(i==k):
    #          result+=lShift10(d,i)
    #      else:
    #          result+=lShift10(kthDigit(n,i),i)
    #  return result 
    #     
def lShift10(n,k):
    return n*(10**k)
def rShift10(n,k):
    return n/(10**k)


def getLeftmostDigit(n):
    # we assumen the digit number start with 
    digit_number = digitCount(n);
    # as the kthDigit count digit from right to left we need to count the digit from left to right
    left_most_digit = kthDigit(n,digit_number-1);

    return left_most_digit

def clearLeftmostDigit(n):
    # to make the left_most_digit to 0
    digit_number = digitCount(n);
    present_number = replaceKthDigit(n,digit_number-1,0);
    return present_number

##  step by step finish the work
##   we should break the steps into different steps
##   make a k =digitCount(board)-position
##   return  replaceKthDigit(board,k,move)



def makeMove(board, position, move):
    # first get the number of the digit in the board

    digit_number=digitCount(board)
    ### pay attention to the defination of and and or!!!!!! you should remember the difference and the type difference 

    ### especially pay attention to that not(1 or 2)== (not 1 and not 2)
    if move != 1 and move != 2: 
        return "move must be 1 or 2!"
    # this situation we need to duge the whether we go voer teh board
    ##!!!!! we should take the position in to consideration where position is less than 1 such as 0 or negative
    elif position > digit_number or position<1: 
        return "offboard!"

    kth_Digit = kthDigit(board,digit_number-position)
    if kth_Digit!=8: 
        return "occupied!"
    # replace the 8 with other digits thus we can decide the status of the board
    board=replaceKthDigit(board,digit_number-position,move)
    return board


def isWin(board):
    ## ones there is 112 we can define there is somebody who will win

    ## if there is a series of numbers is 112
    ##  mode by 1000 and check 112, and keep going

    ''' cannot use magic number   
        target   =  112
        digitsToKeep  = digitCount(target)
        while(board>0 && board>100):
            if board%(10**digitsToKeep)==112: return True
            else board = board/10
        return  False
    '''
    digit_number=digitCount(board)
    for x in range(0,digit_number-2):
        if kthDigit(board,x)==2 and kthDigit(board,x+1)==1 \
        and kthDigit(board,x+2)==1:
            return True
    return False


def isFull(board):
    # once there is some digit not equals to 8 return False
    # else we should return True
    # if the input is str which means there is error infomation that means there is error but in other edge cases 
    if type(board) == str: return False
    digit_number=digitCount(board)
    for x in range(0,digit_number):
        if kthDigit(board,x) == 8: return False
    return True
'''
important tips: to be careful with space and colons 



the whole logic should go in this way:

  

   first : keep track of who the player is 
   second: change the input "GAME", get the size and then build the board acoording to the size
   third : loop through game, (the judgement is the board is valid and the length of the input game is still larger than 0)
   fourth:  loop may stop at situations because of the error, win ,tie 
    after jumping out of the loop ,the only situation should be :
         Tie  the board is full 
         Unfinished !!!!!
 

'''
def play112(game):
    
    player_turn=0;# start from the first person, 1 stands for player 1,0 stands for player 2
    board_size=getLeftmostDigit(game);
    board=makeBoard(board_size);
    game=clearLeftmostDigit(game);
    #if game == 0: return str(board) + ": Unfinished!" delete this situation because it is included in the whole situation
    
    # use this temp to record the board in order for other use
    board_record=board
    
   
    
    while(game > 0 and not isFull(board)):
        # get postion and move 
    
        position =getLeftmostDigit(game)
        game = clearLeftmostDigit(game)
        move = getLeftmostDigit(game)
        game = clearLeftmostDigit(game)
        
        #change player turn 
        player_turn=(player_turn+1)%2
        # keep a temp of board inorder the return of the board could be string
        board_record=board
        board=makeMove(board,position,move)
        # if the board is not string it means there is error 
        if type(board) != int:
            return str(board_record)+": Player "+str(2-player_turn)+": "+str(board)
            break
        # onece we find the result we should jump out of the function to make 
        elif isWin(board):
            return str(board)+": Player "+str(2-player_turn)+ " wins!" 
            break
    # when we end the game, the only situation is uninished or Tie~

    if isFull(board):
        return str(board)+": Tie!" 
    # set the default return situation as Unfinished!
    return str(board)+": Unfinished!"

'''
    player =1
    boardSize = getLeftmostDigit(spec)
    board=makeBoard(boardSize)
    spec =
    while( spec >0):
        position= getLeftmostDigit(spec)
        spec    = clearLeftmostDigit(spec)
        move    = getLeftmostDigit(spec)
        spec    = clearLeftmostDigit(spec)


        newboard   = makeMove(board, posiont,move)
        if type(newboard) == str:
            return str(board) + ": Player" +str(player) + ": "+ board
        board= newboard
        #如果没有错误的话，那么继续检查，这样的结果可能有不同，可能有人赢，可能是平局，可能是未结束。。。。ufinished不用return 任何事情
'''




######################################################################
##### ignore_rest: The autograder will ignore all code below here ####
######################################################################

######################################################################
# Place your graphics solutions here (BELOW the ignore_rest line!)
######################################################################

from Tkinter import *
import math
# given the center and the range as well as the step of the radius we can get the poslition of the rectangle that contains the circle
def getCirclePosition(range_temp,x_center,y_center,dr):
    x_left = x_center-range_temp*dr;
    x_right= x_center+range_temp*dr;
    y_left = y_center-range_temp*dr;
    y_right= y_center+range_temp*dr;
    return(x_left,y_left,x_right,y_right)

def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

def drawCircle(canvas, x0, y0, x1, y1):
    width = x1 - x0
    if (width > 200):
        fill = "blue"
    else:
        fill = rgbString(147, 197, 114) # pistachio!
    canvas.create_oval(x0, y0, x1, y1, fill=fill, width=4)

def drawCircleGradient(canvas, x0, y0, x1, y1):
    # set the width and the height
    width=x1-x0;
    height=y1-y0;
    # find the r of the largest circle 
    r=min(width/2.0,height/2.0)
    # find the cneter of the cercle
    xc=(x0+x1)/2.0;
    yc=(y0+y1)/2.0;
    # judge the condition where we will see that 
    if(width>200):
    # in the first situation we should draw 50 circles
        dr=r/50.0;
        for x in range(50,0,-1):
            dr=r/50.0;
            green=255/49.0*x-255/49.0
            color=rgbString(255-green,green,0);
            # build a helper function to calculate the circleposition
            (x_left,y_left,x_right,y_right)=getCirclePosition(x,xc,yc,dr)
            
            canvas.create_oval(x_left,y_left,x_right,y_right,fill=color,width=0)
    else:
    # in the second situation we should draw 5 circles
        for x in range(5,0,-1):
            dr=r/5.0;
            green=green=255/4.0*x-255/4.0
            color=rgbString(255-green,green,0);
            
            (x_left,y_left,x_right,y_right)=getCirclePosition(x,xc,yc,dr)
            canvas.create_oval(x_left,y_left,x_right,y_right,fill=color,width=0)

# helper function to draw line in like V
def drawlineinV(canvas,x0,y0,x1,y1,x2,y2,color):
    range_bound=20
    width1=x1-x0
    width2=x2-x1
    height1=y1-y0
    height2=y2-y1
    dx1=width1/19.0
    dx2=width2/19.0
    dy1=height1/19.0
    dy2=height2/19.0
    # loop from 0 to 19 and draw a line between the two different line in the V shape
    for x in range(0,range_bound):
        x_left=x0+dx1*x
        x_right=x1+dx2*x
        y_left=y0+dy1*x
        y_right=y1+dy2*x
        canvas.create_line(x_left, y_left, x_right, y_right, fill=color, width=1)

def drawLinePattern(canvas, left, top, right, bottom):
    # use helper fucntion to get the line to draw
    # first draw the different part of the lines
    drawlineinV(canvas,left,bottom,(right+left)/2.0,top,right,bottom,"purple")
    drawlineinV(canvas,left,top,left,bottom,(right+left)/2.0,top,"blue")
    # draw the purple V line and the red V line
    canvas.create_line(left,bottom,(right+left)/2.0,top,fill="purple",width=3)
    canvas.create_line((right+left)/2.0,top,right,bottom,fill="red",width=3)
    canvas.create_line(left,top,left,bottom,fill="blue",width=3)

#helper function which will draw a hexgon and a red polygon and a green polygon in it
def drawSmallCube(canvas,x0,y0,d):
    # given the left-top cornner coordinates, return the whole shape
    x0=x0;
    y0=y0;
    x1=x0-d/2.0;
    y1=y0+math.sqrt(3)*d/2.0;
    x2=x0;
    y2=y0+math.sqrt(3)*d;
    x3=x0+d;
    y3=y0+math.sqrt(3)*d;
    x4=x0+d*1.5;
    y4=y1;
    x5=x0+d;
    y5=y0;
    x6=x0+0.5*d;
    y6=y4;
    canvas.create_polygon(x0,y0,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,fill="green")
    canvas.create_polygon(x0,y0,x6,y6,x4,y4,x5,y5,fill="red")
    canvas.create_polygon(x6,y6,x2,y2,x3,y3,x4,y4,fill="blue")

def drawCrazyCubes(canvas, x0, y0, x1, y1):
    canvas.create_rectangle(x0,y0,x1,y1,fill="yellow")
    dx=(x1-x0)/20.0;

    xstart=x0+dx/2.0;
    ystart=y0;
    #draw cubes one by one using nested loop
    for x in range(0,10):
        for y in range(0,10):
            drawSmallCube(canvas,xstart+x*2*dx,ystart+y*math.sqrt(3)*dx,dx)


            
def drawHexagonsBonus(canvas, x0, y0, x1, y1):
    # try start and end method to draw the cubes
    dx=(x1-x0)/15.5;
    xstart=x0+dx/2.0;
    ystart=y0;
    xstart2=xstart+1.5*dx;
    ystart2=ystart+math.sqrt(3)/2*dx;
    for x in range(0,5):
        for y in range(0,8):
            drawSmallCube(canvas,xstart+x*3*dx,ystart+y*math.sqrt(3)*dx,dx)
    for x in range(0,5):
        for y in range(0,8):
            drawSmallCube(canvas,xstart2+x*3*dx,ystart2+y*math.sqrt(3)*dx,dx)

######################################################################
# Drivers: do not modify this code
######################################################################

def onButton(canvas, drawFn):
    canvas.data.drawFn = drawFn
    redrawAll(canvas)
    
def redrawAll(canvas):
    canvas.delete(ALL)
    canvas.create_rectangle(0,0,canvas.data.width,canvas.data.height,fill="cyan")
    drawFn = canvas.data.drawFn
    if (drawFn):
        canvas.create_rectangle(50, 50, 450, 450, width=4)
        drawFn(canvas, 50, 50, 450, 450)
        canvas.create_rectangle(500, 150, 700, 350, width=4)
        drawFn(canvas, 500, 150, 700, 350)
        canvas.create_text(canvas.data.width/2,20, text=drawFn.__name__, fill="black", font="Arial 24 bold")

def graphicsMain():
    root = Tk()
    canvas = Canvas(root, width=750, height=500)
    class Struct: pass
    canvas.data = Struct()
    canvas.data.width = 750
    canvas.data.height = 500
    buttonFrame = Frame(root)
    canvas.data.drawFns = [drawCircle, drawCircleGradient, drawLinePattern, drawCrazyCubes, drawHexagonsBonus]
    canvas.data.drawFn = canvas.data.drawFns[0]
    for i in xrange(len(canvas.data.drawFns)):
        drawFn = canvas.data.drawFns[i]
        b = Button(buttonFrame, text=drawFn.__name__, command=lambda drawFn=drawFn:onButton(canvas, drawFn))
        b.grid(row=0,column=i)
    canvas.pack()
    buttonFrame.pack()
    redrawAll(canvas)
    root.mainloop()

######################################################################
# Tests
######################################################################

def testMakeBoard():
    print "Testing makeBoard()...",
    assert(makeBoard(1) == 8)
    assert(makeBoard(2) == 88)
    assert(makeBoard(3) == 888)
    print "Passed!"

def testDigitCount():
    print "Testing digitCount()...",
    assert(digitCount(0) == 1)
    assert(digitCount(5) == digitCount(-5) == 1)
    assert(digitCount(42) == digitCount(-42) == 2)
    assert(digitCount(121) == digitCount(-121) == 3)
    print "Passed!"

def testKthDigit():
    print "Testing kthDigit()...",
    assert(kthDigit(789, 0) == kthDigit(-789, 0) == 9)
    assert(kthDigit(789, 1) == kthDigit(-789, 1) == 8)
    assert(kthDigit(789, 2) == kthDigit(-789, 2) == 7)
    assert(kthDigit(789, 3) == kthDigit(-789, 3) == 0)
    assert(kthDigit(789, 4) == kthDigit(-789, 4) == 0)
    print "Passed!"

def testReplaceKthDigit():
    print "Testing replaceKthDigit()...",
    assert(replaceKthDigit(789, 0, 6) == 786)
    assert(replaceKthDigit(789, 1, 6) == 769)
    assert(replaceKthDigit(789, 2, 6) == 689)
    assert(replaceKthDigit(789, 3, 6) == 6789)
    assert(replaceKthDigit(789, 4, 6) == 60789)
    print "Passed!"

def testGetLeftmostDigit():
    print "Testing getLeftmostDigit()...",
    assert(getLeftmostDigit(7089) == 7)
    assert(getLeftmostDigit(89) == 8)
    assert(getLeftmostDigit(9) == 9)
    assert(getLeftmostDigit(0) == 0)
    print "Passed!"

def testClearLeftmostDigit():
    print "Testing clearLeftmostDigit()...",
    assert(clearLeftmostDigit(60789) == 789)
    assert(clearLeftmostDigit(789) == 89)
    assert(clearLeftmostDigit(89) == 9)
    assert(clearLeftmostDigit(9) == 0)
    assert(clearLeftmostDigit(0) == 0)
    print "Passed!"

def testMakeMove():
    print "Testing makeMove()...",
    
    assert(makeMove(8, 1, 1) == 1)
    assert(makeMove(888888, 1, 1) == 188888)
    assert(makeMove(888888, 2, 1) == 818888)
    assert(makeMove(888888, 5, 2) == 888828)
    assert(makeMove(888888, 6, 2) == 888882)
    assert(makeMove(888888, 6, 3) == "move must be 1 or 2!")
    assert(makeMove(888888, 7, 1) == "offboard!")
    assert(makeMove(888881, 6, 1) == "occupied!")
    print "Passed!"

def testIsWin():
    print "Testing isWin()...",

    assert(isWin(888888) == False)
    assert(isWin(112888) == True)
    assert(isWin(811288) == True)
    assert(isWin(888112) == True)
    assert(isWin(211222) == True)
    assert(isWin(212212) == False)
    print "Passed!"

def testIsFull():
    print "Testing isFull()...",
    assert(isFull(8)==False)
    assert(isFull(888888) == False)
    assert(isFull(121888) == False)
    assert(isFull(812188) == False)
    assert(isFull(888121) == False)
    assert(isFull(212122) == True)
    assert(isFull(212212) == True)
    print "Passed!"

def testPlay112():
    print "Testing play112()...",
    
    assert(play112( 5 ) == "88888: Unfinished!")
    assert(play112( 521 ) == "81888: Unfinished!")
    assert(play112( 52112 ) == "21888: Unfinished!")
    assert(play112( 5211231 ) == "21188: Unfinished!")
    assert(play112( 521123142 ) == "21128: Player 2 wins!")
    assert(play112( 521123151 ) == "21181: Unfinished!")
    assert(play112( 52112315142 ) == "21121: Player 1 wins!")
    assert(play112( 523 ) == "88888: Player 1: move must be 1 or 2!")
    assert(play112( 51223 ) == "28888: Player 2: move must be 1 or 2!")
    assert(play112( 51211 ) == "28888: Player 2: occupied!")
    assert(play112( 5122221 ) == "22888: Player 1: occupied!")
    assert(play112( 51261 ) == "28888: Player 2: offboard!")
    assert(play112( 51122324152 ) == "12212: Tie!")
    print "Passed!"

def testAll():
    testMakeBoard()
    testDigitCount()
    testKthDigit()
    testReplaceKthDigit()
    testGetLeftmostDigit()
    testClearLeftmostDigit()
    testMakeMove()
    testIsWin()
    testIsFull()
    testPlay112()

######################################################################
# Main: you may modify this to run just the parts you want to test
######################################################################

def main():
    graphicsMain()
    testAll()

if __name__ == "__main__":
    main()