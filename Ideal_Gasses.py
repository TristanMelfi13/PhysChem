import math
import random
import turtle
from random import *

ScreenSize = (600, 400)


class Particle:
    def __init__(self, Xcor, Ycor, XVel, YVel, CollisionFlag):
        self.Xcor = Xcor
        self.Ycor = Ycor
        self.XVelocity = XVel
        self.YVelocity = YVel
        self.CollisionFlag = CollisionFlag
        self.Visual = turtle.Turtle()
        self.Visual.shape("circle")
        self.Visual.shapesize(0.5)
    def InitializeTurtle(self):
        self.Visual.speed("fastest")
        self.Visual.penup()
        self.Visual.goto(self.Xcor, self.Ycor)

    def MoveVisual(self):
        self.Visual.penup()
        self.Visual.speed("fastest")
        self.Visual.setx(self.Visual.xcor() + self.XVelocity)
        self.Visual.sety(self.Visual.ycor() + self.YVelocity)

    def DetectWallCollision(self):
        if self.Visual.xcor() < ((ScreenSize[0] / 2) * -1) + 6 or self.Visual.xcor() > ((ScreenSize[0] / 2) - 15.5):
            self.XVelocity *= -1
        if self.Visual.ycor() < ((ScreenSize[1] / 2) * -1) + 14.5 or self.Visual.ycor() > ((ScreenSize[1] / 2) - 6):
            self.YVelocity *= -1
    def CheckForParticleCollision(self, Iter, PList):
        for j in range(len(PList)):
            if j != Iter:
                Distance = math.sqrt(math.pow(PList[j].Visual.xcor() - self.Visual.xcor(), 2) +
                                     math.pow(PList[j].Visual.ycor() - self.Visual.ycor(), 2))
                if self.CollisionFlag != 0:
                    self.CollisionFlag -= 1
                if Distance < 8 and self.CollisionFlag == 0:
                    XVelSave = self.XVelocity
                    YVelSave = self.YVelocity
                    self.XVelocity = PList[j].XVelocity
                    self.YVelocity = PList[j].YVelocity
                    PList[j].XVelocity = XVelSave
                    PList[j].YVelocity = YVelSave
                    self.CollisionFlag = 15




def CreateNewParticle():
    NewParticle = Particle(randrange(-1 * int(ScreenSize[0] / 2), int(ScreenSize[0] / 2)),
                           randrange(-1 * int(ScreenSize[1] / 2), int(ScreenSize[1] / 2)),
                           random() * (5 + 5) - 5, random() * (5 + 5) - 5, 0)
    if NewParticle.Xcor > 0:
        NewParticle.Xcor -= 100
    else:
        NewParticle.Xcor += 100

    if NewParticle.Ycor > 0:
        NewParticle.Ycor -= 100
    else:
        NewParticle.Ycor += 100

    NewParticle.InitializeTurtle()
    print("New Particle Created:")
    print("Xcor: {} || Ycor: {} || XVel: {} || YVel: {} ||".format(NewParticle.Xcor, NewParticle.Ycor,
                                                                   NewParticle.XVelocity, NewParticle.YVelocity))
    NewParticle.Visual.penup()
    return NewParticle


ParticleList = []

for i in range(18):
    ParticleList.append(CreateNewParticle())

wn = turtle.Screen()
wn.setup(width=ScreenSize[0], height=ScreenSize[1])

while True:
    XVelSum = 0
    YVelSum = 0
    for i in range(len(ParticleList)):
        turtle.tracer(0, 0)
        XVelSum += abs(ParticleList[i].XVelocity)
        YVelSum += abs(ParticleList[i].YVelocity)
        ParticleList[i].MoveVisual()
        ParticleList[i].DetectWallCollision()
        ParticleList[i].CheckForParticleCollision(i, ParticleList)
        turtle.update()