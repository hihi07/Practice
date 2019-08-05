import numpy as np
import math


#print('test')

#=================格納=================
data=[1,2,3]
arr=np.array(data)
arr1=np.zeros(5)
data2=np.zeros((3,6))
data2=np.ones(5)
arange=np.arange(8)

#print(data)
#print(arr)
#print(arr.dtype)
#print(arr1)
#print(data2)
#print(arange)

#=================型の修正=================

test_str=np.array(['1.2','-3.4','5.6'],dtype=np.string_)
#print(test_str.astype(float))

sample=[3,4,5,5,7,8]
#print(len(sample))
#print(sample)
n=len(sample)
#print(sample+[1,1,1,1,1,1])

def ave_data(x):
    y=0
    y=sum(x)
    return y/n

def s2(x):
    s2n=0
    i=0
    for i in range(n):
        s2n += (x[i]-ave_data(x))**2
    return s2n/n

print("自作関数での分散=",s2(sample))
print("numpyでの分散関数の計算結果",np.var(sample))
result_s2=s2(sample)

print(math.sqrt(result_s2))
