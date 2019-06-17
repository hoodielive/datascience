import cntk 

import numpy as np 

x_input = np.array([[1,2,3,4,5]], np.float32)
y_input = np.array([[10]], np.float32)

X = cntk.input_variables(5, np.float32)
y = cntk.input_variables(1, np.float32)

from cntk.layers import Dense, Sequential 
model = Sequential([ Dense(32), Dense(1)])(X)

loss = cntk.squared_error(model, y)

learning_rate = 0.001 
trainer = cntk.Trainer(model, (loss), cntk.adagrad(model.parameters, learning_rate))

for epoch in range(10):
    trainer.train_minibatch({X: x_input, y: y_input})
