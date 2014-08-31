
# classDemo.py

# Based on modulesDemo2.py and structsDemo.py
# Only here with a Struct rather than a canvas.data dictionary.
# Also uses a Face class from faceDemoWithClass.py.

# Uses the faceDemoWithClass.py module, which
# Creates a face and displays it
# The face can either smile or frown

from Tkinter import *
import faceDemoWithClass

################################
# declare the Struct class first (for use in place of dictionary)
################################

class Struct:
    pass

#######################
# redrawAll and init
#######################

def redrawAll(canvas):
    canvas.delete(ALL)
    # Draw the demo info
    font = ("Arial", 16, "bold")
    msg = "Class Demo: With Module"
    canvas.create_text(canvas.width/2, 25, text=msg, font=font)
    # Draw the face
    canvas.face1.drawFace() # was: faceDemoWithStruct.drawFace(canvas.face1)
    canvas.face2.drawFace() # was: faceDemoWithStruct.drawFace(canvas.face2)

def init(canvas):
    canvas.width = canvas.winfo_reqwidth() - 4
    canvas.height = canvas.winfo_reqheight() - 4
    canvas.face1 = faceDemoWithClass.Face(canvas,
                                    0, 50,
                                    canvas.width/2, canvas.height,
                                    True) # True = smiley
    canvas.face2 = faceDemoWithClass.Face(canvas,
                                    canvas.width/2, 50,
                                    canvas.width, canvas.height,
                                    False) # False = frowny
    redrawAll(canvas)

########### copy-paste below here ###########

def run():
    # create the root and the canvas
    root = Tk()
    root.resizable(width=FALSE, height=FALSE)
    canvas = Canvas(root, width=300, height=200)
    canvas.pack(fill=BOTH, expand=YES)
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    canvas.data = Struct()
    init(canvas)
    # set up events
    # root.bind("<Button-1>", leftMousePressed)
    # root.bind("<KeyPress>", keyPressed)
    # timerFired(canvas)
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()