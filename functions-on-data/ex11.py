from pandas import DataFrame, Series
import numpy as np 

d = DataFrame(np.arange(9).reshape((3,3)), columns=['1','2','3'])

print(d)

fn = lambda x: x - 15 * 0.15

print(d.apply(fn))


