from pandas import Series as series 
from pandas import DataFrame as df 
import numpy as np

series1 = series([1,2,3,4,5], index=['a','b','c','d','e'])
series2 = series([1,2,3,4,5,6,7], index=['a','b','c','d','e','f','g'])

print(series1)

print(series2)

print(series1 + series2)

df1 = df(np.arange(12).reshape((3,4)), columns=['a','b','c','d'])
df2 = df(np.arange(16).reshape((4,4)), columns=['a','b','c','d'])

print(df1)
print(df2)

print(series1.add(series2, fill_value=0)) 
print(df1.add(df2, fill_value=0)) 
