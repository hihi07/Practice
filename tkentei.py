import numpy as np
import math
import pandas as pd
import matplotlib .pyplot as plt
from sklearn import linear_model,datasets
from scipy import stats
import seaborn as sns


#------original_data--------------------

US=[180.7,167.3,167.8,164.6,176.2,157.2,181.5,166.4,172.9,169.5]
JP=[193.0,175.1,175.8,171.4,186.9,161.6,194.0,173.9,182.6,178.0]

#plt.plot(JP)
#plt.show()

print(stats.ttest_ind(JP,US,equal_var=False))

#---------------------------------------

SIZE=1000

data1=np.random.normal(loc=50,scale=20,size=SIZE)
#print(data1)

sns.distplot(data1,bins=range(-20,120))

data2=np.linspace(-5.0,5.0,SIZE)

#plt.plot(data1)
plt.show()









#
