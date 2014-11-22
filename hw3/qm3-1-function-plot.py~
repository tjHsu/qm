import matplotlib.pyplot as plt
import numpy as np
from scipy import constants as const

#set the given parameter
hbar     = const.hbar  #in J*s
L        = 5e-10#in meter
M        = const.m_e
V0       = 4* 1.602176565e-19 #ev into J


interval = 5000
z0 = (L / hbar)*((2*M*V0)**0.5)

#set the plot 
z1 = np.linspace(0,z0, interval)
x1 = z1*0.
z2 = np.linspace(0.1,z0, interval)
x2 = (((z0/z2)**2)-1)**0.5
z3 = np.linspace(0.1,z0, interval)
x3 = np.tan(z3)
z4 = np.linspace(0.1,z0, interval)
x4 = -(1./np.tan(z4))

#finding eigenvalue
t=-1
u=-1
for i in z2:

	if  abs((((z0/i)**2)-1)**0.5 - np.tan(i)) < 10**-1 and i-t>0.5*np.pi:
		t=i
		print "When z=", i,",E0+V0 = ",(hbar**2)*(i**2)/(2*M*L),"Joule."
		print (((z0/i)**2)-1)**0.5 - np.tan(i)

	if  abs((((z0/i)**2)-1)**0.5 + (1./np.tan(i))) < 10**-1 and i-u>0.5*np.pi:
		u=i
		print "When z=", i,",E0+V0 = ",(hbar**2)*(i**2)/(2*M*L),"Joule."
		print (((z0/i)**2)-1)**0.5 +(1./np.tan(i))
		
#plot setting
plt.plot(z1,x1)
plt.plot(z2,x2,"b")
plt.plot(z3,x3,"g")
plt.plot(z4,x4,"r")
plt.xlabel("z")
plt.ylabel("y")
plt.title("Even")
plt.ylim(0,20)
#plt.show()
plt.savefig("hw3-1-funtion-plot.png",dpi=300,format="png")

