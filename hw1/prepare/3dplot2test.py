from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
sample = 1000
X = np.linspace(0,1000,sample)
Y = np.linspace(0,2000,sample)
Z = np.sin(X*np.pi/1000)*np.sin(Y*np.pi/2000)
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

plt.show()
