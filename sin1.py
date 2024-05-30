import numpy as np
from matplotlib import pyplot as plt

t=np.arange(0,1,0.01,)
F=5
x=2*np.sin(2*np.pi*F*t)
plt.plot(t,x)
plt.xlabel("time")
#it just label the x-axis()
plt.ylabel("amplitude")
plt.title("sine wave")
plt.show()