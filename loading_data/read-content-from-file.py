import pandas as pd

#df1 = pd.read_table("./sample.csv", sep=',')
df1 = pd.read_csv("./sample.csv", names=['a','b','c','d'])
df2 = pd.read_csv("./colon.sep", sep=":")
df2 = pd.read_csv("./colon.sep", sep=":", skiprows=[2])
print(df1)
print(df2)

