# Implementation of matplotlib function
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
from matplotlib import cm
import matplotlib	
from numpy import *
#from numpy import real, imag, exp, log, e
funcinp=str(input("Input complex function  :  "))
  
feature_x = np.linspace(-5.0, 5.0, 1000)
feature_y = np.linspace(-5.0, 5.0, 1000)
  
# Creating 2-D grid of features
[X, Y] = np.meshgrid(feature_x, feature_y)
z=(X+Y*1j)
fz = eval(funcinp)
#fzabs=np.abs(fz)
fzarg=np.angle(fz)

  
fig, ax = plt.subplots(1, 1)
#Z = np.sqrt(X ** 2 + Y ** 2)
ax.set_aspect('equal', adjustable='box')

# plots filled contour plot
ax.pcolormesh(X, Y, fzarg, cmap="hsv", vmin=-(np.pi), vmax=(np.pi))
#ax.pcolormesh(X, Y, fzabs, cmap="viridis", norm=matplotlib.colors.LogNorm())
  
plt.show()
'''norm=matplotlib.colors.LogNorm(),'''