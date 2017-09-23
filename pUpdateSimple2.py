#Simple plotting paricles
#
#-Luc d'Hauthuille

import sys as sys
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

from particle import Particle
import tester as worker
import creater as cr
import collisionDealer as cold
import FieldsAndForces as ffs

def updatePs(p, t, acc, eField):
    a = [f1 + f2 for f1, f2 in zip(acc, eField)]
    p.x = p.x + p.v_x*t + 0.5*(a[0])*t*t
    p.y = p.y + p.v_y*t + 0.5*(a[1])*t*t
    ffs.applyAcc(p, t, a)#Questionable time to update velocities
    #Old, worked: p.x = p.x + p.v_x*t + 0.5*(acc[0])*t*t


#Set simulation parameters
t_tot = 8000
t = t_tot/2000 #0.5
acc = [0, 0] # 10 is ~ g? lol
particles = []
eField = [0,0]

if (len(sys.argv) > 1):
    numParticles = int(sys.argv[1])
else:
    numParticles = 10
pSize = 100
v_max = 2
v_y2 = v_max
wholeSize = 250000 #~the whole screen x,y : [-1,1]
pauseTime = 0.01 #0.1 testedd and a bit slow


#Start a fig
fig = plt.figure()
#plt.figure(figsize=(10,10)) #20,10
ax1 = fig.add_subplot(111, aspect='equal')
size = [1000,1000] #[1,1] # Size of domain
ax1.set_xlim((-size[0],size[0]))
ax1.set_ylim((-size[1],size[1]))

#Propogate particles thru time
plt.ion()
def init():
    global acc
    global particles
    global v_max
    #Creating particles
    test = Particle(41.89e9, 0.5*size[0], 0, -50, -50, 1)
    charge = Particle(41.89e9, -0.5*size[0], 0, 50, -50, -2)
    worker.add(test, particles)
    worker.printParticles(particles)
    worker.add(charge, particles)
    worker.printParticles(particles)
    cr.createPs(numParticles, size, particles)

    #This plots particles @ pos given with radius
    for p in particles:
        ax1.add_artist(Circle(xy=(p.x, p.y), radius = p.r))
        print "Radius rn is ", p.r
    plt.show()
    #Move through time
    for i in range(0, t_tot, t):
        if (i%10 == 0):
            nPositive = 0
            for p in particles:
                if (p.q > 0):
                    nPositive+=1
        #print "There are", len(particles), "particles."
        ax1.set_xlim((-size[0],size[0]))
        ax1.set_ylim((-size[1],size[1]))
        l = str(len(particles))
        ax1.set_title(l+" particles" + "," + str(nPositive) + "are positive")
        #pos = [(p.x, p.y) for p inelasticCollision particles]
        #Move particles through space
        for p in particles:
            #ffs.applyEField(p)
            eField = ffs.getEField(p, particles)
            #print eField
            updatePs(p, t, acc, eField)
            ax1.add_artist(Circle(xy=(p.x, p.y), radius = p.r))
            #plt.scatter(p.x, p.y, s= (wholeSize/10000)*p.m)             
        plt.show()
        plt.pause(pauseTime)
        plt.cla()
        cold.checkAllCollisions(particles)
        cold.checkBoundary(particles, t, size) #Check if hits wall
        if i % 5 == 0:
            v_max = max([p.v_y for p in particles]) #Find max velocity

init()


#For randoming
#y = np.random.random()ss
