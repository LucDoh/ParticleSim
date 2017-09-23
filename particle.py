import numpy as np
class Particle:
    #This should define a particle absolutely
    isParticle = True
    dens = (10**7) #~=kg/m^3 Steel
    def __init__(self, m, x, y, v_x, v_y, q = 0):
        self.x = x
        self.y = y
        self.m = m
        self.v_x = v_x
        self.v_y = v_y
        self.q = q
        #self.r = ((3*m)/(4*np.pi*(10**7)))**(1./3.)
        self.r = (self.m**(1.0/3.0)) * 0.002794 #Approxx
        #For dens = 10^7, r = (m^(1/3))*(0.00288)

    def printMe(self):
        print " M= ", self.m," q= ", self.q,
        print " v_y= ", self.v_y, " v_x= ", self.v_x, " r= ", self.r
        print "(", self.x, ",", self.y, ")"
    
    def getSize(self):
        pSize = (4/3)*pi*(r)^3
