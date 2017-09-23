from particle import Particle
import math

#This class, tester.py, has helper
#functions for the particles array. 
# Rm, add, printParticles, resolveCollision
#

def rm(p,particles):    
    particles.remove(p)

def add(p, particles):
    particles.append(p)

def printParticles(particles):
    print "print was called"
    if (len(particles) == 0):
        print "No particles"
    for p in particles:
        p.printMe()
        print

def resolveInECollision(p1, p2, particles):#,particles):
    m = p1.m + p2.m  # New mass
    q = p1.q + p2.q
    mom_x = p1.m*p1.v_x + p2.m*p2.v_x
    mom_y = p1.m*p1.v_y + p2.m*p2.v_y
    v_x = mom_x/m
    v_y = mom_y/m
    x = (p1.m * p1.x + p2.m * p2.x)/(p1.m+p2.m) # Should really mass-weight...
    y = (p1.m * p1.y + p2.m * p2.y)/(p1.m+p2.m)  #
    pNew = Particle(m, x, y, v_x, v_y)
    print pNew.m, pNew.x, pNew.y, pNew.v_x, pNew.v_y, pNew.q
    rm(p1, particles) #remove p1 & p2 T_T
    rm(p2, particles)
    add(pNew, particles)
