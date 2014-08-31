# selectionSortSim.py

########################################
## The original selectionSort algorithm
########################################

def selectionSort(a):
    for startIndex in xrange(len(a)):
        minIndex = startIndex
        for compareIndex in xrange(startIndex+1, len(a)):
            if (a[compareIndex] < a[minIndex]):
                # we just found a new min on this pass
                minIndex = compareIndex
        # at this point we found the smallest element
        # from startIndex to the end of the list
        # so swap them using Python tuple cleverness
        (a[startIndex],a[minIndex]) = (a[minIndex], a[startIndex])

########################################
## Make steps explicit
########################################

def doStep(a, step):
    if (step["action"] == "compare"):
        pass
    elif (step["action"] == "newMin"):
        pass
    elif (step["action"] == "swap"):
        swapIndex = step["swapIndex"]
        minIndex = step["minIndex"]
        (a[swapIndex],a[minIndex]) = (a[minIndex], a[swapIndex])
        
def sort1(a):
    steps = []
    for startIndex in xrange(len(a)):
        minIndex = startIndex
        for compareIndex in xrange(startIndex+1, len(a)):
            step = { "action":"compare" ,
                     "compareIndex":compareIndex,
                     "minIndex":minIndex }
            steps.append(step)
            doStep(a, step)
            if (a[compareIndex] < a[minIndex]):
                minIndex = compareIndex
                # we just found a new min on this pass
                step = { "action":"newMin" ,
                         "minIndex":minIndex }
                steps.append(step)
                doStep(a, step)
        # at this point we found the smallest element
        # from startIndex to the end of the list
        # so swap them using Python tuple cleverness
        step = { "action":"swap" ,
                 "swapIndex":startIndex,
                 "minIndex":minIndex }
        steps.append(step)
        doStep(a, step)
    return steps

########################################
## Our first non-graphical simulation
## (so exciting!)
########################################

import copy

def sim1(a):
    print a
    steps = sort1(copy.deepcopy(a))    
    for step in steps:
        doStep(a, step)
        print step
    print a

########################################
## Now, graphically visualize this
########################################

from Tkinter import *

def mousePressed(event):
    canvas = event.widget.canvas
    redrawAll(canvas)

def keyPressed(event):
    canvas = event.widget.canvas
    if (event.char == "s"):
        animateStep(canvas)
    redrawAll(canvas)

def timerFired(canvas):
    redrawAll(canvas)
    delay = 250 # milliseconds
    canvas.after(delay, timerFired, canvas) # pause, then call timerFired again

def getNextStep(canvas):
    a = canvas.data["a"] 
    steps = canvas.data["steps"]
    nextStep = canvas.data["nextStep"]
    if (nextStep >= len(steps)):
        return { }
    step = steps[nextStep]
    return step
    
def animateStep(canvas):
    a = canvas.data["a"]
    step = getNextStep(canvas)
    doStep(a, step)
    nextStep = canvas.data["nextStep"]
    canvas.data["nextStep"] = nextStep + 1
    
def redrawAll(canvas):
    canvas.delete(ALL)
    step = getNextStep(canvas)
    compareIndex = step.get("compareIndex", None)
    minIndex = step.get("minIndex", None)
    swapIndex = step.get("swapIndex", None)
    action = step.get("action", None)
    a = canvas.data["a"]
    for i in xrange(len(a)):
        bottom = 400
        height = 300*a[i]/16
        top = bottom - height
        left = 20 + 30 * i
        right = left + 20
        color = "gray"
        if (i == compareIndex):
            color = "cyan"
        elif (i == minIndex):
            color = "orange"
        elif (i == swapIndex):
            color = "magenta"
        canvas.create_rectangle(left, top, right, bottom, fill=color)

import random

def init(canvas):
    a = range(1,16+1)
    random.shuffle(a)
    steps = sort1(copy.deepcopy(a))
    nextStep = 0
    canvas.data["a"] = a
    canvas.data["steps"] = steps
    canvas.data["nextStep"] = nextStep
    redrawAll(canvas)

########### copy-paste below here ###########

def run():
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=500, height=500)
    canvas.pack()
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    canvas.data = { }
    init(canvas)
    # set up events
    root.bind("<Button-1>", mousePressed)
    root.bind("<Key>", keyPressed)
    timerFired(canvas)
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()