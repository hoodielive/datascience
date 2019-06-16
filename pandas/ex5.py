# Create a series which contains prices of some consumer items where the index of the series is the name 
# of the item is the name of the item and the element at that index is the price of the item
# also access the price of one of the item(s) using indexing

from pandas import Series as series 


a = series(['400', '500', '600'], index=['grocery', 'trip', 'ebo'])
print(a)
print(a['trip'])
