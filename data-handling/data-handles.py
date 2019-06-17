from pandas import Series 
from pandas import DataFrame as df
import numpy as np 

s = Series([1,2,np.nan,3,4,np.nan,5])

print(s)

print(s.dropna())

data = df([[1,2,3], [np.nan,np.nan,np.nan], [2,np.nan,4],[np.nan,3,np.nan]])

print(data)

print()

print(data.dropna())

print(data.dropna(how='all'))

print() 

data[3]=np.nan
print(data)

print(data.dropna(how='all',axis=1))
