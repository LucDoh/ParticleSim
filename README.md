# ParticleSim_L
This is a basic particle interaction simulator built in python.

To run the simulation, type run pUpdateSimple.py or pUpdateSimple2.py.
- pUpdateSimple uses only gravity 
- pUpdateSimple2 uses a basic implementation 
of the Coulomb force.

Helper functions are defined in a few classes:
i) collisionDealer.py: has functions to check for collisons and if found,
resolve collisions [O(n^2)... I know]
ii) worker.py: used to remove/add a particle to the list,print lisst of
particles and resolve collisions inelastically if they are found by cDealer.
iii) particle.py: defines the Particle object.
iv) FieldsAndForces.py: functions here are routinely called to apply forces due
to fields to the particles in the list, and advance them in position. Currently
uses the Euler Method and deals with self-interaction by brute force O(n^2).
v) creater.py: creates particles (eventually uniformly distributed) of somewhat
random velocities/positions. with some integer amount of charge. 
