from pandas import Series, DataFrame
import numpy as np

s = Series([1,2,3,4], index=['d','c','a','b']) 
print(s)
print()
print(s.sort_index())
print()
d = DataFrame(np.arange(16).reshape((4,4)), index=['three', 'one', 'four', 'two'], columns=['d','c','b','a'])
print(d)
print()
print(d.sort_index(axis=1, ascending=False))

s2 = Series([2,5,4,1])
print()
print(s2.sort_values())

print()
s = Series([1,3,np.nan,4,5,np.nan,8])
print(s)
print()
print(s.sort_values())
