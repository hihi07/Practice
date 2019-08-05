import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#---------1次元配列の相関係数------
x=list(i for i in range(10))#[]と同義
print(x)

np.random.seed(0)
y=list(np.random.randint(0,10,10))#[]と同義ではないnpなのでlist指定しないと出力はarrayになる
print(y)

xs=pd.Series(x)
ys=pd.Series(y)
#print(xs)

res=xs.corr(ys)
print(res)

df=pd.DataFrame(x,y)
#print(df)
#-----------------------------

#-------2次元配列の相関係数-------

df=pd.DataFrame(index=['idx'+str(i) for i in range(10)])
for i in range(3):
    df['col'+str(i)]=np.random.rand(10)

print(df ,'\n\n')

res_df=df.corr()
print(res_df)
