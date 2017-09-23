import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

from particle import Particle
import tester as worker
import FieldsAndForces as ffs
import math

vScale = 1

def createPs(numParticles, size, particles):
    if numParticles == 0: 
        return True
    evenSpaceX = size[0]/numParticles
    evenSpaceY = size[1]/numParticles
    for i in range(numParticles):
        #s = 15*np.random.random_sample()        
        randx = np.random.random()
        randy = np.random.random()
        if (randx < 0.5):
            v_x = vScale*np.random.random()
            q = 10
        else:
            v_x = -vScale*np.random.random()
            q = -10
        if (randy < 0.5):
            v_y = vScale*np.random.random()
            q = 10
        else:
            v_y= -vScale*np.random.random()
            q = -10
        
        prt =  Particle(42e9, size[0]/(i+1), size[1]/(i+1), v_x, v_y, q)
        particles.append(prt)
