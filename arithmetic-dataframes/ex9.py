from pandas import DataFrame as df 
import numpy as np 

df1 = df(np.arange(6).reshape((2,3)), columns=[1,2,3])
df2 = df(np.arange(12).reshape((3,4)), columns=[1,2,3,4])
print(df1.add(df2,fill_value=0))
