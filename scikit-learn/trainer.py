from sklearn.model_selection import train_test_split 

x = 4
y = 2
test_size = 10

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)

print(x_train)
