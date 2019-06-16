from pandas import Series as series 
from pandas import DataFrame as df 
import numpy as np

s = series([1,2,3,4])
print(s)

d = df(np.arange(8).reshape(2,4)) 
print(d)

print(d - s)
print(d + s)
