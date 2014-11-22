# Source Code for Task 2.

from scipy import special as sp
import numpy as np
import matplotlib.pyplot as plt

print sp.ai_zeros(10)
print sp.airy(-2.33810741)

def xfrange(start, stop, step):
    while start < stop:
        yield start
        start += step

p=-0.1
z={}
x={}
for i in xfrange(0,20,0.00001):
    x[i]=sp.airy(((np.pi/(2.*1.149))**(2./3))*(-1.)*(1.149+i))
    z[i]=sp.airy(((np.pi/(2.*1.149))**(2./3))*(1.149-i))
    r = x[i][0]*z[i][2]-x[i][2]*z[i][0]
    if (abs(r)<0.5*0.0001 and i-p>0.15):
        print "e=",i
        print "ζ-L/2=",((np.pi/(2.*1.149))**(2./3))*(-1.)*(1.149+i)
        print "Ai(ζ-L/2)=",x[i][0]
        print "ζL/2=",((np.pi/(2.*1.149))**(2./3))*(1.149-i)
        print "Bi(ζ-L/2)=",x[i][2]
        print "-b/a=Ai/Bi=",x[i][0]/x[i][2]
        p=i


l=(6*(10**-10)/(5.29*(10**-11)))
s=500
x1 = np.linspace(-l,l,s)
y1 = sp.airy(0.1248*(x1-9.299))
plt.subplot(211)
plt.plot(x1,y1)
plt.xlabel("x-axis") 
plt.ylabel("y-axis") 
plt.title("HW1.3") 
plt.savefig("hw4.png",dpi=300,format="png") 
plt.show() 

print ((2*500.*10**-4)/51.422)**(1./3)
print (3.941*(10**-20)/(4.3587*(10**-18))/500*(10**4)*51.422)
print (1.678*(10**-19)/(4.3587*(10**-18))/500*(10**4)*51.422)
print (3.766*(10**-19)/(4.3587*(10**-18))/500*(10**4)*51.422)
print (6*(10**-10)/(5.29*(10**-11)))




