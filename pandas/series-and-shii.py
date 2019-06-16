from pandas import Series

# create a series
a = Series([10,20,30,40,50])
print(a)

# just values
print(a.values)

# just index
print(a.index)

# create series with predefined index
b = Series([100,200,300], index=['b', 'c', 'a'])
print(b)

# get values from predefined index
print(b[['b', 'a']])

# create series from python-dictionary 
d = {'a': 1000, 'b': 2000, 'c': 3000} 
s = Series(d)
print(s)
