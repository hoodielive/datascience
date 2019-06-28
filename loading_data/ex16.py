# Reading data from multiple file formats 
# create a csv file and save some random data into it
# read the csv file in form of a dataframe 
# create a csv file with some other separator like a '/'
# read the above file with different separator 
# read only 2 rows from the file

import pandas as pd 

df1 = pd.read_csv('./sample.csv', sep=',', nrows=2)


df2 = pd.read_csv('./2colnums.csv')

print(df1)
print('-' * 35)
print(df2)
