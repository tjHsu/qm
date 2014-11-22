import matplotlib.pyplot as plt
import numpy as np
from scipy import constants as const

#set the given parameter
hbar     = const.hbar  #in J*s
L        = 2.5e-10#in meter
M        = const.m_e
V0       = 4* 1.602176565e-19 #ev into J


interval = 5000
z0 = (L / hbar)*((2*M*V0)**0.5)
print "z0=",z0
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
p=0
q=0

z_even= []
z_odd = []
z_even_count =-1
z_odd_count =-1

for i in z2:

	if  abs((((z0/i)**2)-1)**0.5 - np.tan(i)) < 10**-1 and i-t>0.5*np.pi:
		t=i
		print "When z=", i,",E0+V0 = ",(hbar**2)*(i**2)/(2*M*L),"Joule."
		print (((z0/i)**2)-1)**0.5 - np.tan(i)
		z_even=z_even+[i]
		z_even_count = z_even_count+1
	if  abs((((z0/i)**2)-1)**0.5 + (1./np.tan(i))) < 10**-1 and i-u>0.5*np.pi:
		u=i
		print "When z=", i,",E0+V0 = ",(hbar**2)*(i**2)/(2*M*L),"Joule."
		print (((z0/i)**2)-1)**0.5 +(1./np.tan(i))
		z_odd=z_odd+[i]
		z_odd_count = z_odd_count+1
#print z_even,z_odd
#print z_even[z_even_count]


		
#plot setting
plt.subplot(211)
plt.plot(z1,x1)
plt.plot(z2,x2,"b")
plt.plot(z3,x3,"g")
plt.plot(z4,x4,"r")
plt.xlabel("z")
plt.ylabel("y")
#plt.title()
plt.ylim(0,20)

plt.subplot(212)
z1 = np.linspace(-L,L, interval)
x1 = z1*0.
plt.plot(z1,x1)
kappa=(((z0**2)-(z_even[0]**2))**0.5)/L		
z5= np.linspace(-L, L, interval)
x5= (1/((L+(1/kappa))**0.5)*np.cos((z_even[0])*z5/L))
plt.plot(z5,x5,"b")
'''
kappa=(((z0**2)-(z_even[1]**2))**0.5)/L		
z6= np.linspace(-L, L, interval)
x6= (1/((L+(1/kappa))**0.5)*np.cos((z_even[1])*z6/L))
plt.plot(z6,x6,"b")
'''
kappa=(((z0**2)-(z_odd[0]**2))**0.5)/L		
print kappa
kare= (z_odd[0]/L)*np.tan(z_odd[0])
print 1/((L+(1/kappa))**0.5)
z7= np.linspace(-L, L, interval)
x7= (1/((L+(1/kappa))**0.5)*np.sin((z_even[0])*z7/L))
plt.plot(z7,x7,"g")

plt.title("eigenfunctions")
'''
kappa=(((z0**2)-(z_odd[1]**2))**0.5)/L		
z8= np.linspace(-L, L, interval)
x8= (1/((L+(1/kappa))**0.5)*np.sin((z_even[1])*z8/L))
plt.plot(z8,x8,"g")
'''
'''
print z_even,z_even_count
print z_odd,z_odd_count
for i in range(z_even_count+1):
	print "i=",i
	kappa=(((z0**2)-(z_even[z_even_count]**2))**0.5)/L		
	z5= np.linspace(0, L, interval)
	x5= (1/((L+(1/kappa))**0.5)*np.cos((z_even[z_even_count])*z5/L))
	plt.plot(z5,x5,"b")
for i in range(z_odd_count+1):
	kappa=(((z0**2)-(z_odd[z_odd_count]**2))**0.5)/L		
	z6= np.linspace(0, L, interval)
	x6= (1/((L+(1/kappa))**0.5)*np.sin((z_even[z_even_count])*z5/L))
	plt.plot(z6,x6,"g")
'''

plt.xlim(-L,L)

for i in range(8):
	print ((i*np.pi*hbar/2/L)**2)/2/M

print 

plt.show()
#plt.savefig("hw3-1-5A.png",dpi=300,format="png")



