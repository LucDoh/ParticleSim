#Simple plotting paricles
#
#-Luc d'Hauthuille

import numpy as np
import matplotlib.pyplot as plt

from particle import Particle
import tester as worker
import FieldsAndForces as ffs
import math


#Set general parameters
acc = [0, -10] # 10 is ~ g? lol
particles = []
t_tot = 150
t = 1
eField = [1,0]

numParticles = 5
pSize = 10
size = [1000,500]
v_max = 20
v_y2 = v_max
#Propogate particles thru time
#createPs(numParticles, size)

def init():
    global acc
    global particles
    global v_max
    worker.printParticles(particles)
    test = Particle(10, -size[0], 0, v_max*2, 0 )
    charge = Particle(10, -0.5*size[0], 0, 0, 0, 10)
    worker.add(test, particles)
    worker.add(charge, particles)
    worker.printParticles(particles)
    worker.resolveCollision(particles[0], particles[1], particles)
    worker.printParticles(particles)

    #Move through time
    i = 0
    for i in range(t_tot):
        #pos = [(p.x, p.y) for p inelasticCollision particles]
        #Move particles through space

        #for p in particles:

        if i % 5 == 0:
            v_max = max([p.v_y for p in particles]) #Find max velocity

init()


#For randoming
#y = np.random.random()ss
