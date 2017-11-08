import numpy as np
import math
from particle import Particle
import worker as worker


#Here we'll use a simple Euler equation [ x_t+1 = x_t + x'_t*(delt_t) ] 


'''
#This Was used once
def updatePs(p, t, acc):
    p.x = p.x + p.v_x*t #+ 0.5*acc[0]*t*t
    p.y = p.y + p.v_y*t #+ 0.5*acc[1]*t*t    
    applyAcc(p, t, acc)#Questionable time to update velocities
'''

#This has been moved from pUpdateSimple2
def updatePs(p, t, acc, eField, bField):
    a = [f1 + f2 for f1, f2 in zip(acc, eField)]
    p.x = p.x + p.v_x*t #0.5*(a[0])*t*t
    p.y = p.y + p.v_y*t # 0.5*(a[1])*t*t
    #ffs.applyAcc(p, t, a, bField)#Questionable time to update velocities
    applyAcc(p, t, a, bField)#Questionable time to update velocities
    #Old, worked: p.x = p.x + p.v_x*t + 0.5*(acc[0])*t*t



#Updates the velocities of a particle with acc
def applyAcc(p, t, acc, bField = [0,0,0]):
    #eField = getEfield(p, particles)
    if (bField[2] != 0): # Calculate force from Bfield assuming B_z only 
        acc[0] += (p.q*(p.v_y*bField[2]))/p.m 
        acc[1] += (p.q*(-p.v_x*bField[2]))/p.m
    p.v_x = p.v_x + acc[0]*t #+ eField[0]*t
    p.v_y = p.v_y + acc[1]*t #+ eField[1]*t

def applyGivenAcc(p, t, a):
    p.v_x = p.v_x + a[0]*t
    p.v_y = p.v_y + a[1]*t
    
#Calculates the E-field on particle p
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
            cosTheta = deltX/(dist+0.1) #dist +1 avoids div by zero
            sinTheta = deltY/(dist+0.1) #dist +1 avoids div by zero
            eField[0] += eMag*cosTheta
            eField[1] += eMag*sinTheta
    return eField


def applyEField(p):
    if p.q != 0:
        applyGivenAcc(p, t, eField)
