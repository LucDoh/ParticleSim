#Simple plotting paricles
#
#-Luc d'Hauthuille

import sys as sys
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

from particle import Particle
import worker as worker
import creater as cr
import collisionDealer as cold
import FieldsAndForces as ffs


#This should be moved to FieldsAndForces
def updatePs(p, t, acc, eField, bField):
    a = [f1 + f2 for f1, f2 in zip(acc, eField)]
    p.x = p.x + p.v_x*t #0.5*(a[0])*t*t
    p.y = p.y + p.v_y*t # 0.5*(a[1])*t*t
    ffs.applyAcc(p, t, a, bField)#Questionable time to update velocities
    #Old, worked: p.x = p.x + p.v_x*t + 0.5*(acc[0])*t*t


#Set simulation parameters
t_tot = 8000
t = t_tot/4000 #/2000 #0.5
acc = [0, 0] # 10 is ~ g? lol
particles = [] #create empty particles array
#eField = [2000,0]
bField = [0,0,200000000]
numParticles = 10 #10
selfInteraction = True #Choose whether selfinteracting(Efields)


#Get argument and set it to numparticles
if (len(sys.argv) > 1):
    numParticles = int(sys.argv[1])

pSize = 100
v_max = 2
v_y2 = v_max
wholeSize = 250000 #~the whole screen x,y : [-1,1]
pauseTime = 0.02 #0.1 testedd and a bit slow
wSize = 3000

#Start a fig using matplotlib
fig = plt.figure() #plt.figure(figsize=(10,10)) #20,10
ax1 = fig.add_subplot(111, aspect='equal')
size = [wSize,wSize]#1000,1000] # Size of domain
ax1.set_xlim((-size[0],size[0]))
ax1.set_ylim((-size[1],size[1]))
plt.ion()
#End figure setup

#Propogate particles thru time
def init():
    global acc
    global particles
    global v_max
    global eField
    #adhocCreate()
    cr.createPs(numParticles, size, particles)

    #This plots particles @ pos given with radius
    '''for p in particles:
        ax1.add_artist(Circle(xy=(p.x, p.y), radius = p.r))
        print "Radius rn is ", p.r
    plt.show()
    '''
    
    #Move through time
    for i in range(0, t_tot, t):
        if (i%10 == 0):
            nPositive = 0
            ke=0
            v_max = max([p.v_y for p in particles]) #Find max velocity
            for p in particles:
                ke+= (p.v_x**2 + p.v_y**2)
                if (p.q > 0):
                    nPositive+=1
                print (ke)


        #print "There are", len(particles), "particles."
        ax1.set_xlim((-size[0],size[0]))
        ax1.set_ylim((-size[1],size[1]))
        l = str(len(particles))
        ax1.set_title(l+" particles" + "," + str(nPositive) + "are positive")
        #pos = [(p.x, p.y) for p inelasticCollision particles]
        #Move particles through space
        for p in particles:
            #ffs.applyEField(p)
            if (selfInteraction == True):
                eField = ffs.getEField(p, particles) #gets EField on p due to particles

            #updatePs(p, t, acc, eField)
            updatePs(p, t, acc, eField, bField) #trying to add BField
            ax1.add_artist(Circle(xy=(p.x, p.y), radius = p.r))
            #plt.scatter(p.x, p.y, s= (wholeSize/10000)*p.m)             
        plt.show()
        plt.pause(pauseTime)
        plt.cla()
        cold.checkAllCollisions(particles)
        cold.checkBoundary(particles, t, size) #Check if hits wall


#This is a dumb way to do this Luc
def adhocCreate():
    #Creating particles adhoc
    test = Particle(41.89e9, 0, 0, 50, 0, 10)
    worker.add(test, particles)
    ''' '''
    charge = Particle(41.89e9, -0.5*size[0], 0, 50, -50, 10)
    worker.add(charge, particles)
    b1 = Particle(41.89e9, -0.9*size[0], 0.05*size[1], 50, 0, 10)
    b2 = Particle(41.89e9, -0.9*size[0], 0, 50, 0, 10)
    worker.add(b1, particles)
    worker.add(b2, particles)
    worker.printParticles(particles)
    
    '''
    b3 = Particle(41.89e9, -0.9*size[0], -0.05*size[1], 50, 0, 10)
    b4 = Particle(41.89e9, -0.9*size[0], 0.09*size[1], 50, 0, -1)
    b5 = Particle(41.89e9, -0.9*size[0], -0.09*size[1], 50, 0, -1)
    worker.add(b3, particles)
    worker.add(b4, particles)
    worker.add(b5, particles)
    '''
    


init()


#For randoming
#y = np.random.random()ss
