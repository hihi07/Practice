import numpy as np
import math
import pandas as pd
import matplotlib .pyplot as plt
from sklearn import linear_model,datasets


#------original_data--------------------

data1=[0,1,2,3,4,5]
data2=[3,2,5,7,6,10]

df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)

#print(df2)

model=linear_model.LinearRegression()
model.fit(df1,df2)

#print(model.coef_)
#print(model.intercept_)
#---------------------------------------

#------sklearn_dataset------------------

boston=datasets.load_boston()
#print(type(boston))
#print(boston.keys())

b_data=pd.DataFrame(data=boston.data,columns=boston.feature_names)#<class 'sklearn.utils.Bunch'>の型は扱いが特別
#print(b_data)

#print(boston.DESCR)#データの概要
#print(b_data.head(5))

#rooms=pd.DataFrame(b_data.RM)
num_rooms=pd.DataFrame(b_data['RM'])
#print(num_rooms.head(10))

price_rooms=pd.DataFrame(boston.target)

model=linear_model.LinearRegression()
model.fit(num_rooms,price_rooms)

#print(model.coef_)
#print(model.intercept_)

x_test=np.linspace(num_rooms.min(),num_rooms.max(),100)[:,np.newaxis]
resal_liner=model.predict(x_test)

#plt.scatter(num_rooms,price_rooms,color='blue')
#plt.plot(x_test,resal_liner,color='red')
#plt.show()


#-------------------住宅価格の単回帰予想------------------------

df=pd.read_csv('/Users/hiraku/Desktop/Python/monthlyRent.csv')
#print(df.head())

plt.scatter(df['人口密度'],df['家賃'])
#plt.show()

df_explain=df.drop(['都道府県','家賃'],axis=1)
df_purpose=df['家賃']

model=linear_model.LinearRegression()
model.fit(df_explain,df_purpose)

x_lin=np.linspace(df['人口密度'].min(),df['人口密度'].max(),100)#[:,np.newaxis]
x=pd.DataFrame(x_lin)

#resal_liner=model.predict(x)

#print(model.coef_)
res_coef=pd.DataFrame({'係数値':model.coef_ ,'係数名':df_explain.columns})
print(res_coef)
print(model.intercept_)

#plt.scatter(num_rooms,price_rooms,color='blue')
#plt.plot(x,resal_liner,color='red')
#plt.show()



#
