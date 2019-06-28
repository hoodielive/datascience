from pandas import Series 
import numpy as np

s = Series(np.arange(10))
s.to_csv('./demoseries', sep='/')

print(s)
