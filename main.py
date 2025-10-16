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
        pass
    
class Baton:
    x,y = 0,0
    dropped = False
    
    def drop():
        pass
    
    def checkMiss():
        pass
    
class Grabber:
    points = 0
    x = 0
    
    def move(direction):
        # either "left" or "right"

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
    pass
    
def onStep(app):
    for baton in app.dropper.batons:
        if baton.dropped == True:
            baton.y -= 2
            baton.checkMiss()

def resetApp(app):
    app.dropper = Dropper(6)

def onAppStart(app):
    resetApp(app)

def main():
    runApp()
    
main()
