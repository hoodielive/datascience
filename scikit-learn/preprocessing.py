from sklearn import preprocessing 
import pandas as pd

iris_scaled = pd.DataFrame(preprocessing.scale(iris_data))

print(iris_scaled)
