import pandas as pd 

df1 = pd.read_csv('./sample.csv', nrows=2)
df1.to_csv('./newdata')

print(df1)
