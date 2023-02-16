import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from turtle import *


class Disk(object):
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=40):
        self.name = name
        self.xpos = xpos
        self.ypos = ypos
        self.height = height
        self.width = width
    
    def showDisk(self):
        penup()
        pencolor("black")
        goto(self.xpos, self.ypos)
        pendown()
        setheading(0)
        forward(self.width / 2)
        left(90)
        forward(self.height)
        left(90)
        forward(self.width)
        left(90)
        forward(self.height)
        left(90)
        forward(self.width / 2)
        penup()
        goto(0, 0)
        pendown()

    def newPos(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def clearDisk(self):
        penup()
        pencolor("white")
        goto(self.xpos, self.ypos)
        pendown()
        setheading(0)
        forward(self.width / 2)
        left(90)
        forward(self.height)
        left(90)
        forward(self.width)
        left(90)
        forward(self.height)
        left(90)
        forward(self.width / 2)
        penup()
        goto(0, 0)
        pendown()

class Pole(object):
    def __init__(self, name="", xpos=0, ypos=0, thick=10, length=100):
        self.pname = name
        self.stacks = []
        self.toppos = 0
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length

    def showPole(self):
        penup()
        goto(self.pxpos, self.pypos)
        pendown()
        setheading(0)
        forward(self.pthick / 2)
        left(90)
        forward(self.plength)
        left(90)
        forward(self.pthick)
        left(90)
        forward(self.plength)
        left(90)
        forward(self.pthick / 2)
        penup()
        goto(0, 0)
        pendown()

    def pushDisk(self, disk):
        self.stacks.append(disk)
        disk.newPos(self.pxpos, self.pypos + self.toppos)
        self.toppos += disk.height

    def popDisk(self):
        disk = self.stacks.pop()
        self.toppos -= disk.height
        return disk


class Hanoi(object):
    def __init__(self, n=3, start="A", workspace="B", destination="C"):
        self.startp = Pole(start, 0, 0)
        self.workspacep = Pole(workspace, 150, 0)
        self.destinationp = Pole(destination, 300, 0)
        self.startp.showPole()
        self.workspacep.showPole()
        self.destinationp.showPole()
        for i in range(n):
            self.startp.pushDisk(Disk("d" + str(i), 0, i * 150, 20, (n - i) * 30))
        for disk in self.startp.stacks:
            disk.showDisk()

    def moveDisk(self, start, destination):
        disk = start.popDisk()
        disk.clearDisk()
        destination.pushDisk(disk)
        disk.showDisk()

    def move_tower(self, n, s, d, w):
        if n == 1:
            self.moveDisk(s, d)
        else:
            self.move_tower(n - 1, s, w, d)
            self.moveDisk(s, d)
            self.move_tower(n - 1, w, d, s)

    def solve(self):
        self.move_tower(3, self.startp, self.destinationp, self.workspacep)


h = Hanoi()
h.solve()
done()

