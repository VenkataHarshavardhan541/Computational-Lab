import numpy as np
from matplotlib import pyplot as plt

t=np.arange(0,1,0.01,)
F=4
F1=2
x=np.sin(2*np.pi*F*t)+np.sin(2*np.pi*F1*t)
y=np.sin(2*np.pi*F*t)-np.sin(2*np.pi*F1*t)
plt.plot(t,x)
plt.plot(t,y)
plt.xlabel("time")
#it just label the x-axis()
plt.ylabel("amplitude")
plt.title("sine wave")
plt.show()