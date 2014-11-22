import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

L =1
m= 9.11*10**-31
hbar = 1.05*10**-34
t = m*L*L/2/np.pi/hbar
x,y=np.mgrid[0:L:50j,0:t:50j]
#z=x*np.exp(-x**2-y**2)

z=0.9*np.sin(x*np.pi/L)+0.1*np.sin(3*x*np.pi/L)+6*np.sin(x*np.pi/L)*np.sin(3*x*np.pi/L)*np.cos(4*np.pi*np.pi*hbar*y/m/L/L)
ax=plt.subplot(111,projection='3d')
ax.plot_surface(x,y,z,rstride=2,cstride=2,cmap=plt.cm.coolwarm,alpha=0.8)

#plt.xlim(-0.1*10**-9,1.1*10**-9)
#plt.ylim(-0.2*10**-9,2.2*10**-9)

ax.set_xlabel('z(0 - L)')
ax.set_ylabel('t(0 - mL^2/2*pi*hbar)')
ax.set_zlabel('|psi|^2')
 
#plt.show()
plt.savefig("hw31.png",dpi=300,format="png") 
plt.show()
