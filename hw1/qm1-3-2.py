import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

x,y=np.mgrid[0:1*10**-9:50j,0:2*10**-9:50j]
#z=x*np.exp(-x**2-y**2)
nx=1
ny=1
lx=1*10**-9
ly=2*10**-9
z=((4./lx*ly)**0.5)*np.sin(nx*x*np.pi/lx)*np.sin(ny*y*np.pi/ly)
ax=plt.subplot(111,projection='3d')
ax.plot_surface(x,y,z,rstride=2,cstride=2,cmap=plt.cm.coolwarm,alpha=0.8)

plt.xlim(-0.1*10**-9,1.1*10**-9)
plt.ylim(-0.2*10**-9,2.2*10**-9)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
 
#plt.show()
plt.savefig("hw31.png",dpi=300,format="png") 
plt.show()
