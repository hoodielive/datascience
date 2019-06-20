from sklearn import datasets as ds 

iris = ds.load_iris()

# sklearn.datasets.base.Bunch
print(type(iris))

# feature names for variables and target_names for target/label
print(iris.keys())

# display actual dataset
print(iris.data)

# display targets
print(iris.target)

# we display names
print(iris.target_names)

# data shape
print(iris.data.shape)

# iris.DESCR
print(iris.DESCR)
