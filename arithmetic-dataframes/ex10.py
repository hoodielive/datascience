from pandas import Series as series 
from pandas import DataFrame as df 
import numpy as np

s = series([1,2,3,4,5], index=['a','b','c','d','e'])
s = series(np.arange(5), index=[1,2,3,4,5])

d = df(np.arange(10).reshape(2,5), columns=[1,2,3,4,5])

print(d - s)
#print(d + s)

