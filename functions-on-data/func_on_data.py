from pandas import DataFrame as df 
import numpy as np

d = df(np.arange(16).reshape((4,4))) 
print(d)
print('----------------------------')

f = lambda x: x + 10 
print(d.apply(f))

print('----------------------------')
f2 = lambda x: x * x 
print(d.apply(f2))
