# load what we need

import matplotlib.pyplot as plt
import numpy as np


# sin from 0-180
# y= (2/(10**-9))**0.5*np.sin(np.pi*x/(10**-9))

l=1#*10**-9
s=50
x1 = np.linspace(0,l,s)
y1 = ((2./l)**0.5)*np.sin(x1 * np.pi / l)
x2 = np.linspace(0,l,s)
y2 = ((2./l)**0.5)*np.sin(2*x2 * np.pi / l)
x0 = np.linspace(0,l,s)
y0 = x0*0

#((2/l)**0.5)*

#x1 = np.arange(0,1000)
#y1 = np.sin(x1 * np.pi / 1000)
#x2 = np.arange(0,1000)
#y2 = np.sin(2*x2 * np.pi / 1000)

#x0 = np.arange(-300,1300)
#y0 = x0*0

# begin

    #set x y list
plt.subplot(211)
plt.plot(x1,y1)
plt.plot(x0,y0,"r") 
plt.xlim(-0.1*l,1.1*l)


plt.subplot(212)
plt.plot(x2,y2)
plt.plot(x0,y0,"r") 
plt.xlim(-0.1*l,1.1*l)


plt.xlabel("x-axis") 
plt.ylabel("y-axis") 
plt.title("HW1.3") 


    # end  
    # then is show
plt.savefig("hw1.png",dpi=300,format="png") 
plt.show() 


    # save
    # replace pyplot.show() into the below:



