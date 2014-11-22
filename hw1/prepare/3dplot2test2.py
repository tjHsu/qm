import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

x,y=np.mgrid[0:50:50j,0:50:50j]
#z=x*np.exp(-x**2-y**2)
z=np.sin(2*x*np.pi/50)*np.sin(2*y*np.pi/50)
ax=plt.subplot(111,projection='3d')
ax.plot_surface(x,y,z,rstride=2,cstride=2,cmap=plt.cm.coolwarm,alpha=0.8)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
 
plt.show()
