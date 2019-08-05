import numpy as np
import math
import pandas as pd



#------data_set--------------------

data2=[32,16,18,19,17,25,11,16,30,16]
E=20

data1=[i for i in range(1,len(data2)+1)]

#data2=[10,25,20,27,29,9]
#print(sum(data2))#sum()はpythonの組み込み関数
df=pd.DataFrame(data=data2,index=data1,columns=['test'])
#print(data1)
#print(df)
#----------------------------------

ziyudo=len(data2)

def chi_2(x):
    y=0
    for i in range(0,ziyudo):
        #print(x[i])
        y += ((x[i]-E)**2)/E

    return y

print(chi_2(data2))
