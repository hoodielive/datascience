from pandas import DataFrame as df
from pandas import Series as seri 
import numpy as np 

products = seri([100,200,300,400], index=['cellphone', 'computer', 'monitor', 'iPhone'])
print(products)

print()

print(products.sort_index())

print()

print(products.sort_values(ascending=False))
