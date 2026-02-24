import numpy as np

# Single Neuron
################
# inputs = [1,2,3]
# weights = [0.2,0.8,-0.5]
# bias = 0.8

# output = np.dot(inputs, weights) + bias

# print(output)

inputs = [1, 2, 3]

weights=[
   [0.2, 0.8, -0.5], [0.5, -0.91, 0.26], [-0.26, -0.27, 0.17]
]

biases=[2,3,0.5]

layers_output = np.dot(weights, inputs) + biases
print(layers_output)

# layers_output = np.dot(inputs, weights) + biases  Wrong one

# When you write np.dot(inputs, weights), numpy treats inputs as a row vector (1×3) and multiplies it by weights (3×3), 
# producing a (3,1) result. However, this computes the wrong thing — it's treating each column of weights as a neuron's weights rather than each row.

# The correct version on line 21, np.dot(weights, inputs), multiplies weights (3×3) by inputs (3,1),
# which is equivalent to computing the dot product of each neuron's weight row against the inputs — giving one output value per neuron. That's the intended behavior.

layers_output1 = np.dot(inputs, np.transpose(weights)) + biases
print(layers_output1)