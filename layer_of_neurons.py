inputs = [1, 2, 3]

weights=[
   [0.2, 0.8, -0.5], [0.5, -0.91, 0.26], [-0.26, -0.27, 0.17]
]

biases=[2,3,0.5]

output=[]

for i in range(3):
    sum = 0
    weightArr = weights[i]
    bias = biases[i]

    for j in range(3):
        input = inputs[j]
        weight = weightArr[j]
        sum = sum + input*weight
    sum += bias
    output.append(sum)

print(output)
