import pandas as pd

# only read the parts of a file that is important 
df1 = pd.read_csv("./sample.csv", nrows=2)

print(df1)

