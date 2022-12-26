import math
import random
import turtle
from random import *

ScreenSize = (600, 400)


def Distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))


def MostProbableVelocity(Temp, MolarMass):
    MolarMass /= 1000
    return math.sqrt((Temp * 8.3145 * 2) / MolarMass)


def LJTest(Distance):
    pass


class Particle:
    def __init__(self, Xcor, Ycor, XVel, YVel, MolarMass):
        self.Xcor = Xcor
        self.Ycor = Ycor
        self.XVelocity = XVel
        self.YVelocity = YVel
        self.MolarMass = MolarMass
        self.Visual = turtle.Turtle()
        self.Visual.shape("circle")
        self.Visual.shapesize(0.5)

    def InitializeTurtle(self):
        self.Visual.speed("fastest")
        self.Visual.penup()
        self.Visual.goto(self.Xcor, self.Ycor)
        DistanceFromOrigin = Distance(self.Visual.xcor(), 0, self.Visual.ycor(), 0)
        Accel = MostProbableVelocity(298, self.MolarMass) + random() * (5 + 15) - 15
        print("Most Probable Speed of Helium atom at 300 Kelvin: {}".format(Accel))
        self.XVelocity += (Accel * (self.Visual.xcor() / DistanceFromOrigin)) / 1000
        self.YVelocity += (Accel * (self.Visual.ycor() / DistanceFromOrigin)) / 1000

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
                if Distance < 8:
                    XVelSave = self.XVelocity
                    YVelSave = self.YVelocity
                    self.XVelocity = PList[j].XVelocity
                    self.YVelocity = PList[j].YVelocity
                    PList[j].XVelocity = XVelSave
                    PList[j].YVelocity = YVelSave


def CreateNewParticle():
    NewParticle = Particle(randrange(-1 * int(ScreenSize[0] / 2), int(ScreenSize[0] / 2)),
                           randrange(-1 * int(ScreenSize[1] / 2), int(ScreenSize[1] / 2)),
                           random() * (1 + 1) - 1, random() * (1 + 1) - 1, 4)
    if NewParticle.Xcor > 0:
        NewParticle.Xcor -= 50
    else:
        NewParticle.Xcor += 50

    if NewParticle.Ycor > 0:
        NewParticle.Ycor -= 50
    else:
        NewParticle.Ycor += 50

    NewParticle.InitializeTurtle()
    print("New Particle Created:")
    print("Xcor: {} || Ycor: {} || XVel: {} || YVel: {} || Magnitude of Vector {} m/s".format(NewParticle.Xcor,
                                                                                              NewParticle.Ycor,
                                                                                              NewParticle.XVelocity,
                                                                                              NewParticle.YVelocity,
                                                                                              1000 * (math.sqrt(
                                                                                                  math.pow(
                                                                                                      NewParticle.XVelocity,
                                                                                                      2) + math.pow(
                                                                                                      NewParticle.YVelocity,
                                                                                                      2)))))
    NewParticle.Visual.penup()
    return NewParticle


ParticleList = []

for i in range(18):
    ParticleList.append(CreateNewParticle())

wn = turtle.Screen()
wn.setup(width=ScreenSize[0], height=ScreenSize[1])

sum = 0

for i in range(len(ParticleList)):
    sum = 1000 * ((math.pow(ParticleList[i].XVelocity, 1) + math.pow(ParticleList[i].YVelocity, 1)))

print("SUM OF PARTICLE VELOCITIES {}".format(sum / len(ParticleList)))

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
