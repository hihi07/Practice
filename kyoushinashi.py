import numpy as np
import math
import pandas as pd
import matplotlib .pyplot as plt
from sklearn import linear_model,datasets
from scipy import stats
import seaborn as sns
from sklearn.cluster import KMeans



df=pd.read_csv('/Users/hiraku/Desktop/Python/consumerPrices.csv')

#print(df.head(7))
#print(df['食料'].head(5))
print(df.keys())

df1=df[['都道府県','食料','水道光熱費','住居','家具家事用品', '衣類', '保険医療', '交通通信', '教育','教養娯楽', '諸雑費']]
#print(df1.head(5))
#plt.scatter(df1['食料'],df1['水道光熱費'])
#plt.show()

model=KMeans(n_clusters=4,random_state=0)

#df1_1=df[['食料','水道光熱費','住居', '家具家事用品', '衣類', '保険医療', '交通通信', '教育','教養娯楽', '諸雑費']]

df1_1=df.drop('都道府県',axis=1)#axis=0なら行の削除 axis=1なら列の削除

model.fit(df1_1)

res=model.labels_
#print(res)

#result=pd.Series(res)

#df2=pd.DataFrame(df1,res)
#df2=df1.append(res)

df1['res']=res
print(df1)

plt.scatter(df1['食料'],df1['水道光熱費'],c=df1['res'])

plt.show()


#
