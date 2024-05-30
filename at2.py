import numpy as np
import matplotlib.pyplot as plt
print("Enter length of araay x")
x_length=int(input())
x=np.zeros(x_length)
for i in range(x_length):
    print(f"Enter x[{i}]")
    x[i]=float(input())
print("Ente leengtyh of array")
y_length=int(input())
y=np.zeros(y_length)
for i in range(y_length):
    print(f"Enter y[{i}]")
    y[i]=float(input())
k_values=np.arange(0,1.41,0.01)
result=np.zeors_like(k_values)
for i in range(x_length):
    result+=x[i]*np.cos(2*np.pi*i*k_values)
plt.plot(k_values,result)
plt.show