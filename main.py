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
    
    def __init__(self, app, batonAmount):
        self.width = app.width-40
        self.left = 20
        self.right = self.left+(self.width)
        batonSpacing = self.width/batonAmount
        
        for i in range(batonAmount):
            x = self.left + batonSpacing*i + batonSpacing/2
            y = 20
            self.batons.append(Baton(x,y))
    
    def dropBaton(self):
        dropIndex = randrange(len(self.batons))
        self.batons[dropIndex].drop()
    
class Baton:
    x,y = 0,0
    dropped = False
    
    def __init__(self, x, y):
        self.x, self.y = x,y
    
    def drop(self):
        self.dropped = True
    
    def checkMiss(self, app):
        if self.y > app.height:
            self.dropped = False
            self.x, y = -100, -100
    
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
    app.step += 1
    if app.step % 90 == 0:
        app.dropper.dropBaton()
    for baton in app.dropper.batons:
        if baton.dropped == True:
            baton.y += 2
            baton.checkMiss(app)

def resetApp(app):
    app.step = 0
    app.dropper = Dropper(app, 6)
    app.grabber = Grabber(app.width/2, app.height-50)

def onAppStart(app):
    resetApp(app)

def main():
    runApp()
    
main()
