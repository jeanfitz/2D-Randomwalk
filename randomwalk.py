## 2D random walk plot
##
## Basic Example using numpy, matplotlib
## Usage: Developing simulations, could be used for student learning,
## checking theoretical values

## Author: Jean Fitzmaurice 
## August 2019

import numpy as np
import matplotlib.pyplot as plt
import random

## unit step 2D random walk

## Ask user how many steps?
nsteps = input("How many steps? ")
nsteps=int(nsteps)

## Start from origin (0,0) in plane

lastpoint=[0.0,0.0]

random.seed(None)

for i in range(0,nsteps):
  print(i)
  # Draw random phase from [0,2pi] re^(i *theta), where r=1 
  theta = np.random.uniform(0,2*np.math.pi)
  # Compute dx, dy
  dx = np.math.cos(theta)
  dy = np.math.sin(theta)

  # Plot line segment from lastpoint to new point

  plt.plot([lastpoint[0],lastpoint[0]+dx],[lastpoint[1],lastpoint[1]+dy],'r.-')
## Set lastpoint for next step
  lastpoint=[lastpoint[0]+dx, lastpoint[1]+ dy]

## Plot attributes

plt.gca().set_aspect('equal',adjustable='box')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.title("2D random walk")
plt.show()


  
