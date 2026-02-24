import numpy as np

# Batch of 4 samples, each with 3 input features
inputs = [
    [1.0,  2.0,  3.0],
    [2.0,  5.0, -1.0],
    [-1.5, 2.7,  3.3],
    [0.0,  1.0,  0.5]
]

# 3 neurons, each with 3 weights (one per input feature)
weights = [
    [ 0.2,  0.8, -0.5],
    [ 0.5, -0.91, 0.26],
    [-0.26, -0.27, 0.17]
]

# One bias per neuron
biases = [2.0, 3.0, 0.5]

output = np.dot(inputs, np.array(weights).T) + biases
print(output)