import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

from particle import Particle
import worker as worker
import FieldsAndForces as ffs
import math

vScale = 25
q = 10

# Create particles of some number, distributed across
# the domain (~size) and adds them to global list 
# particles
def createPs(numParticles, size, particles):
    if numParticles == 0: 
        return True
    evenSpaceX = size[0]/numParticles
    evenSpaceY = size[1]/numParticles
    for i in range(numParticles):
        #s = 15*np.random.random_sample()        
        x, y, v_x, v_y = assignRandV(size)
        prt =  Particle(42e9, x, y, v_x, v_y, q) #(42e9, size[0]/(i+1), size[1]/(i+1), v_x, v_y, q)
        particles.append(prt)

def assignRandV(size):
    global vScale
    global q
    randx = np.random.random()
    randy = np.random.random()
    x = randx*size[0]
    y = randy*size[1]
    if (randx < 0.5):
        v_x = vScale*np.random.random()
    else:
        v_x = -vScale*np.random.random()
        q = -q
    if (randy < 0.5):
        v_y = vScale*np.random.random()
    else:
        v_y= -vScale*np.random.random()
        q = -q
    return x, y, v_x, v_y
