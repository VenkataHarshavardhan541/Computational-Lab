import numpy as np
from matplotlib import pyplot as plt
t=np.arange(0,1,0.01)
dict={'s1':[2,5],'s2':[5,10],'s3':[3,7],'s4':[10,12],'s5':[1,3]}
k=int(input('enter sinusoidal key to generate'))
if dict[k]:
    x=dict[k][0]*np.sin(2*np.pi*dict[k][1]*t)
    plt.plot(t,x)
    plt.show()