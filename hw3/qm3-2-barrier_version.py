import matplotlib.pyplot as plt
import numpy as np
from scipy import constants as const

#set the given parameter
hbar     = const.hbar  #in J*s
L        = 5e-10#in meter
M        = const.m_e
V0       = 1* 1.602176565e-19 #ev into J
Emax     = 3* 1.602176565e-19 #ev into J


interval = 500
E1 = np.linspace(10e-39,V0, interval)
T1 = 1.0/(1.+((V0**2)/(4*E1*(V0-E1)))*((np.sinh(((2*L)/hbar)*((2*M*(V0-E1))**0.5)))**2))

E3 = np.linspace(V0,Emax, interval)
T3 = 1.0/(1.+((V0**2)/(4*E3*(E3-V0)))*((np.sin(((2*L)/hbar)*((2*M*(E3-V0))**0.5)))**2))

# calculate the wave-length
print const.h/((2*M*2.206e-19)**0.5)
print const.h/((2*M*4.010e-19)**0.5)

#plot setting
plt.plot(E1,T1)

plt.plot(E3,T3)
plt.ylabel("T")
plt.xlabel("E(in Joule)")
plt.xlim(0,Emax)
plt.show()
plt.savefig("hw3-2-barrier_test.png",dpi=300,format="png")

