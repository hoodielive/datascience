from pandas import DataFrame as df 
from pandas import Series as series
import numpy as np


#d = df(['Cruise', 'Chevy', 16000, 23, 2014], \
#        index=['0','1','2','3','4'], \
#        columns=['name','model','price', 'mileage', 'year'])

car = {'brand': ['BMW', 'Ford', 'Audi'], 'model': ['X5', 'Focus', 'A8'], 'price': [100000,20000, 12000], 
        'year': [2015,2018,2019]}

frame = df(car)
print(frame)
print(frame.brand)
print(frame.price[1])

print(frame.reindex(columns=['brand', 'price','model', 'mileage', 'year']))
