#Simple plotting paricles
#
#-Luc d'Hauthuille

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

from particle import Particle
import tester as worker
import creater as cr
import FieldsAndForces as ffs
import math

#from collisionCheck import checker

'''def createPs(numParticles, size, particles):
    evenSpaceX = size[0]/numParticles
    evenSpaceY = size[1]/numParticles
    for i in range(numParticles):
        s = 15*np.random.random_sample()
        prt =  Particle(30, size[0]/(i+1), size[1]/(i+1), s, s)
        #if i % 2 == 0: # prt = Particle(1 , i*evenSpaceX, i*evenSpaceY, s, 0)
        #else: # prt = Particle(1,-i*evenSpaceX, -i*evenSpaceY, s, v_y2)
        particles.append(prt)'''

def updatePs(p, t):
    p.x = p.x + p.v_x*t + 0.5*(acc[0])*t*t
    p.y = p.y + p.v_y*t + 0.5*(acc[1])*t*t
    ffs.applyAcc(p,t, acc)#Questionable time to update velocities


# Check if any p hits boundary, treat fully elastically
# by flipping normal component of v. Should appreciate
# the passsage of time.
def checkBoundary(particles, t):
    for p in particles:
        if p.x + p.r < -0.9*size[0]: #or (p.x + 1.5*p.v_x*t) < -1.1*size[0]:
            p.v_x = -p.v_x
        if p.x + p.r > 0.9*size[0]: #or (p.x + 1.5*p.v_x*t) > 1.1*size[0]:
            p.v_x = -p.v_x
        if p.y + p.r< -0.9*size[1]: #or (p.y + 1.5*p.v_y*t) < -1.1*size[1]:
            p.v_y = -p.v_y
        if p.y + p.r > 0.9*size[1]: #or (p.y + 1.5*p.v_y*t) > 1.1*size[1]:
            p.v_y = -p.v_y


def checkAllCollisions(particles):
    for p in particles:
        checkCollision(p, particles)

def checkCollision(p, particles):
        for i in particles:
            if i is p:
                continue
            dist = math.sqrt((p.x-i.x)**2 + (p.y-i.y)**2)
            print "Dist is", dist
            if ((dist < 2*(i.r + p.r))):
                print "Mayday, we have a COLLISION b/w:"
                print p.m, p.x, p.y, p.v_x, p.v_y
                print i.m, i.x, i.y, i.v_x, i.v_y
                worker.resolveInECollision(p, i, particles)
                return

#Start a fig
fig = plt.figure()
#plt.figure(figsize=(10,10)) #20,10
ax1 = fig.add_subplot(111, aspect='equal')
size = [500,500] #[1,1] # Size of domain
ax1.set_xlim((-size[0],size[0]))
ax1.set_ylim((-size[1],size[1]))



#Set general parameters
acc = [0, -10] # 10 is ~ g? lol
particles = []
t_tot = 200
t = 0.5
eField = [1,0]

numParticles = 10
pSize = 100
v_max = 20
v_y2 = v_max
wholeSize = 250000 #~the whole screen x,y : [-1,1]


#Propogate particles thru time
plt.ion()
def init():
    global acc
    global particles
    global v_max
    #Creating particles
    test = Particle(41.89e9, 0.5*size[0], 0, -50, -50)
    charge = Particle(41.89e9, -0.5*size[0], 0, 50, -50)
    worker.add(test, particles)
    worker.printParticles(particles)
    worker.add(charge, particles)
    worker.printParticles(particles)

    #Move through time
    i = 0
    ax1.set_xlim((-size[0],size[0]))
    ax1.set_ylim((-size[1],size[1]))
    #This plots a particle @ pos given with radius
    #r=200
    #ax1.add_artist(Circle(xy=(0, 0),radius =r))
    for p in particles:
        ax1.add_artist(Circle(xy=(p.x, p.y), radius = p.r))
        print "Radius rn is ", p.r
    #plt.scatter(find1.x, find1.y, s= r_in_points[1]**2) 
    plt.show()

    cr.createPs(numParticles, size, particles)
    for i in range(t_tot):
        #print "There are", len(particles), "particles."
        ax1.set_xlim((-size[0],size[0]))
        ax1.set_ylim((-size[1],size[1]))
        #pos = [(p.x, p.y) for p inelasticCollision particles]
        #Move particles through space
        for p in particles:
            #ffs.applyEField(p)
            updatePs(p, t)
            ax1.add_artist(Circle(xy=(p.x, p.y), radius = p.r))
            #plt.scatter(p.x, p.y, s= (wholeSize/10000)*p.m) 
            #s = point size, s=1000 usess half the radius of s=4000
        plt.show()
        plt.pause(0.01)
        plt.cla()
        checkAllCollisions(particles)
        checkBoundary(particles, t) #Check if hits wall
        if i % 5 == 0:
            v_max = max([p.v_y for p in particles]) #Find max velocity

init()


#For randoming
#y = np.random.random()ss
