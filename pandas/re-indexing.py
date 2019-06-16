from pandas import Series as series 
from pandas import DataFrame as df
import numpy as np

s = series([10,20,30,40,50], index=['c','b','d','e','a']) 
print(s)

print(s.reindex(['a','b','c','d','e']))

d = df(np.arange(9).reshape((3,3)), index=['c','a','b'], columns=['apple', 'mango', 'banana'])

print(d.reindex(['a','b','c']))
