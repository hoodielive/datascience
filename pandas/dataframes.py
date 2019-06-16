from pandas import DataFrame as df
from pandas import Series as series

details = {'name': ['osa', 'ire', 'ifa'], 'age':[22,33,55], 'location': ['Africa', 'Cuba', 'Brazil']} 

frame = df(details)
print(frame)

frame = df(details, columns=['name','location','age', 'salary'])
print(frame)

print(frame['location'])
print(frame.location)
print(frame.loc[1])

frame.salary = 5000
print(frame)

s = series([300,400], index=[0,1]) 
print(s)

frame.salary = s 
print(frame)
