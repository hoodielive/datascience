import pandas as pd

df1 = pd.read_csv("./sample.csv")
df1 = pd.read_table("./sample.csv", sep=',')

print(df1)

