# This class will deal with interparticle collisions
# as well as collisions with boundaries
#-Luc d'Hauthuille                                                                                      

import numpy as np
import math
from particle import Particle
import worker as worker

#import matplotlib.pyplot as plt
#from matplotlib.patches import Circle
#import creater as cr
#import FieldsAndForces as ffs



#### Make all this its own function #######
# Check if any p hits boundary, treat fully elastically
# by flipping normal component of v. Should appreciate (idk what I mean appreciate?)
# the passsage of time.
def checkBoundary(particles, t, size):
    for p in particles:
        if p.x - p.r < -1.0*size[0]: #or (p.x + 1.5*p.v_x*t) < -1.1*size[0]:
            p.v_x = -p.v_x
        if p.x + p.r > 1.0*size[0]: #or (p.x + 1.5*p.v_x*t) > 1.1*size[0]:
            p.v_x = -p.v_x #if p.v_x > 0 else p.v_x
        if p.y - p.r < -1.0*size[1]: #or (p.y + 1.5*p.v_y*t) < -1.1*size[1]:
            p.v_y = -p.v_y
        if p.y + p.r > 1.0*size[1]: #or (p.y + 1.5*p.v_y*t) > 1.1*size[1]:
            p.v_y = -p.v_y


def checkAllCollisions(particles):
    for p in particles:
        checkCollision(p, particles)

#checks if there is a collision, if so then resolve using worker class
def checkCollision(p, particles):
        for i in particles:
            if i is p:
                continue
            dist = math.sqrt((p.x-i.x)**2 + (p.y-i.y)**2)
            #print "Dist is", dist
            if ((dist < (i.r + p.r))):
                print "Mayday, we have a COLLISION b/w:"
                print p.m, p.x, p.y, p.v_x, p.v_y
                print i.m, i.x, i.y, i.v_x, i.v_y
                worker.resolveInECollision(p, i, particles)
                return
#### END of make all this its own function #######
