import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,1,0.01)
f=5
d=np.sin(2*np.pi*f*t)
np.savetxt('sin-oct.txt',d,fmt='ro.18f')
with open('sin-txt','r')as f:
    A=np.load.txt(f)
plt.plot(t,d,label='sine wave')
plt.plot(t,A,'ro',label='Read Data')
plt.legend()
plt.xlabel('Time')
plt.ylabel('amplitude')
plt.title('sine wave-file handling')
plt.grid()
plt.show()