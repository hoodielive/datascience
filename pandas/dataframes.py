from pandas import DataFrame as df

details = {'name': ['osa', 'ire', 'ifa'], 'age':[22,33,55], 'location': ['Africa', 'Cuba', 'Brazil']} 

frame = df(details)
print(frame)

frame = df(details, columns=['name','location','age'])
print(frame)
