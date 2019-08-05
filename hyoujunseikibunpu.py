import math
import numpy as np
import matplotlib.pyplot as plt


def N_0_1(x):
    y = math.exp(-0.5*(x**2))/math.sqrt(2.0*math.pi)
    return y

#print(N_0_1(5))

k=np.linspace(-5.0,5.0,10)

p=[]
for i in range(len(k)):
    p.append(N_0_1(k[i]))#appendはリストのメソッドで追加の意味

print(k)

plt.scatter(k,p)
plt.show()
