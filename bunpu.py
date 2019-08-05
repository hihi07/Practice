import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.special import comb
from scipy.stats import norm

#二項分布
p=0.5
n=10

y_bio=pd.Series([comb(float(n),x)*(p**x)*(1-p)**(float(n)-x) for x in range(0,n+1)])

#print(y_bio)
#plt.bar(y_bio.index,y_bio)
#plt.show()
#ポアソン分布
lam=2

def kaijou(m):
    if(m==0 or m==1):
        return 1
    else:
        return m*kaijou(m-1)

def f_poisson(x):
    y=((lam**x)*math.exp(-lam))/kaijou(x)
    return y

#print(f_poisson(3))

y_poi=pd.Series([f_poisson(x) for x in range(0,n+1)])

#plt.bar(y_poi.index,y_poi)
#plt.show()



#標準正規分布（自作関数）
n_ori:int=100#型の宣言
x_ori=np.linspace(-5.0,5.0,n_ori)

def N(x):
    y=math.exp(-0.5*x**2)/math.sqrt(2.0*math.pi)
    return y

y_N=pd.Series([N(s) for s in x_ori])#for inのあとはリストも可

#print(y_N)
#plt.bar(y_N.index,y_N)
plt.plot(x_ori,y_N)
plt.show()

#標準正規分布
y_N_lib=norm.pdf(x_ori,0,2)

#plt.plot(x_ori,y_N_lib)
#plt.show()

x = np.arange(-4,4,0.1)
y = [norm.pdf(x=m,loc=0,scale=1) for m in x]

#plt.plot(x,y)
#plt.show()
