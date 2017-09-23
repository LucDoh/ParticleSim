import numpy as np
from particle import Particle
import tester as worker
import math


def updatePs(p, t, acc):
    p.x = p.x + p.v_x*t + 0.5*acc[0]*t*t
    p.y = p.y + p.v_y*t + 0.5*acc[1]*t*t
    applyAcc(p, t, acc)#Questionable time to update velocities

def applyAcc(p, t, acc):
    #eField = getEfield(p, particles)
    p.v_x = p.v_x + acc[0]*t #+ eField[0]*t
    p.v_y = p.v_y + acc[1]*t #+ eField[1]*t
    

def getEField(p, particles):
    k = 8.99 * 10**2 #8.99 * 10**9 
    eField = [0,0]
    eMag = 0
    for i in particles:
        if i is not p:
            deltX = (p.x - i.x)
            deltY = (p.y - i.y)
            dist = math.sqrt(deltX**2 + deltY**2)
            eMag = (k*(i.q*p.q))/((dist+1)**2) #dist +1 avoids div by zero
            cosTheta = deltX/(dist+1) #dist +1 avoids div by zero
            sinTheta = deltY/(dist+1) #dist +1 avoids div by zero
            eField[0] += eMag*cosTheta
            eField[1] += eMag*sinTheta
    return eField
def applyGivenAcc(p, t, a):
    p.v_x = p.v_x + a[0]*t
    p.v_y = p.v_y + a[1]*t

def applyEField(p):
    if p.q != 0:
        applyGivenAcc(p, t, eField)
