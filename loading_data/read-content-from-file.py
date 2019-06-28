import pandas as pd

#df1 = pd.read_table("./sample.csv", sep=',')
df1 = pd.read_csv("./sample.csv", names=['a','b','c','d'])

print(df1)

