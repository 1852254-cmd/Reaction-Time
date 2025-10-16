# reaction time test thingymajig

# ---------------------------------
# Instructions
# ---------------------------------

# try to catch the batons!

# ---------------------------------
# TODO
# ---------------------------------

# everything gang

# ---------------------------------
# Source Code
# ---------------------------------
from cmu_graphics import *
from random import randrange
import math

# ---------------------------------
# classes
# ---------------------------------

class Dropper:
    batons = []
    
    def __init__(self, batonAmount):
        self.width = app.width-40
        self.left = 20
        self.right = left+width
        
    
class Baton:
    x,y = 0,0
    dropped = False
    
    def __init__(self, x, y):
        pass
    
    def drop():
        pass
    
    def checkMiss():
        pass
    
class Grabber:
    points = 0
    x = 0
    
    def __init__(self, x, y):
        pass
    
    def move(self, direction):
        # either "left" or "right"
        if direction == "left":
            self.x -= 2
        elif direction == "right":
            self.x += 2
        
    def checkCatch(self, baton):
        pass

# ---------------------------------
# app functions
# ---------------------------------

def onKeyHold(app, keys):
    if "left" in keys or "a" in keys:
        app.grabber.move("left")
    if "right" in keys or "d" in keys:
        app.grabber.move("right")


def onMousePress(app, mouseX, mouseY):
    pass
    
def onMouseRelease(app, mouseX, mouseY):
    pass

def onMouseDrag(app, mouseX, mouseY):
    pass

def onMouseMove(app, mouseX, mouseY):
    if mouseX < app.grabber.x:
        app.grabber.move("left")
    elif mouseX > app.grabber.x:
        app.grabber.move("right")

def redrawAll(app):
    grabber = app.grabber
    dropper = app.dropper
    
    # draw batons first
    for baton in dropper.batons:
        x1 = baton.x-5
        y1 = baton.y-20
        drawRect(x1, y1, 10, 40, fill='red', border='black')
        
    # then dropper
    drawRect(20, 0, app.width-40, 30, fill='yellow', border='black')
    
    # then grabber
    drawCircle(grabber.x, app.height-20, 10, fill='blue')

def onStep(app):
    for baton in app.dropper.batons:
        if baton.dropped == True:
            baton.y -= 2
            baton.checkMiss()

def resetApp(app):
    app.dropper = Dropper(6)
    app.grabber = Grabber(app.width/2, app.height-50)

def onAppStart(app):
    resetApp(app)

def main():
    runApp()
    
main()
