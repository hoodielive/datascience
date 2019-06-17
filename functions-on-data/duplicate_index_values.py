from pandas import Series, DataFrame 
import numpy as np

s = Series([1,2,3,4,5], index=['a', 'b', 'a', 'c', 'd']) 

print(s)

print(s['a'])

print(s.index.is_unique)
print()
# create dataFrame 
d = DataFrame(np.arange(6).reshape((2,3)), columns=[1,2,3], index=['a','a'])
print(d)
print() 

# check for unqiueness
print(d.index.is_unique)
print()
d = DataFrame(np.arange(16).reshape((4,4)))

print(d) 
print()

# calculate the sums
print(d.sum())

# the sum of each row 
print(d.sum(axis=1))

# the sum of the columns / #rows
print(d.mean())

# the rows only
print(d.mean(axis=1))

# how many elements are present in a column
print(d.count())

# max and min
print(d.min())
print(d.max())

# get it all / data 
print(d.describe())
