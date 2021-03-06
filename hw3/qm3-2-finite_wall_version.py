import matplotlib.pyplot as plt
import numpy as np
from scipy import constants as const

#set the given parameter
hbar     = const.hbar  #in J*s
L        = 5e-10#in meter
M        = const.m_e
V0       = 1* 1.602176565e-19 #ev into J
Emax     = 3* 1.602176565e-19 #ev into J

#Tinv= 1+((V0**2)/(4*E*(E+V0)))*((sin(((2*L)/hbar)*((2*M*(E+V0))**0.5)))**2)
interval = 500
E = np.linspace(10e-39,Emax, interval)
T = 1.0/(1.+((V0**2)/(4*E*(E+V0)))*((np.sin(((2*L)/hbar)*((2*M*(E+V0))**0.5)))**2))
print E
print ((V0**2.)/(4.*E*(E+V0)))

plt.plot(E,T)
plt.ylabel("T")
plt.xlabel("E(in Joule)")
#plt.show()
plt.savefig("hw3-2-i.png",dpi=300,format="png")

