

# load what we need

import matplotlib.pyplot as plt
import numpy as np

# sin from 0-180

x = np.arange(0,180)
y = np.sin(x * np.pi / 180.0)


# begin

    #set x y list

plt.plot(x,y) 

    # set the domain otherwise is automatic
#plt.xlim(-30,390)
#plt.ylim(-1.5,1.5)
   

plt.xlabel("x-axis") 
plt.ylabel("y-axis") 
plt.title("The Title") 


    # end  
    # then is show
plt.show() 


    # save
    # replace pyplot.show() into the below:

plt.savefig("filename.png",dpi=300,format="png") 

