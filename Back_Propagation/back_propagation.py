from random import random, randint
from dataset import *
from math import exp

HIDDEN_LAYER_LENGTH = 15
INPUT_LAYER_LENGTH = 45
OUTPUT_LAYER_LENGTH = 10
NUM_REPLICAS = 4
LEARNING_RATE = 0.1
NUM_EPOCHS = 100000


# Method to Initialize the Artificial Neural Network
def initialize(): 

    input_dataset, output_dataset = initialize_dataset(NUM_REPLICAS, INPUT_LAYER_LENGTH, OUTPUT_LAYER_LENGTH)

    print("\nGenerating Dataset....")
    print("INPUT DATASET")
    for i in input_dataset:
        print(i)

    print()
    print("OUTPUT DATASET")
    print(output_dataset)

    print("\nInitialize Weights.....")
    print("MATRIX BETWEEN INPUT AND HIDDEN LAYER")
    weights1 = []
    for i in range(INPUT_LAYER_LENGTH):
        weight_row = []
        for j in range(HIDDEN_LAYER_LENGTH):
            weight_row.append(random())
        weights1.append(weight_row)
    
    for i in weights1:
        print(i)

    print("\nMATRIX BETWEEN HIDDEN AND OUTPUT LAYER")
    weights2 = []
    for i in range(HIDDEN_LAYER_LENGTH):
        weight_row = []
        for j in range(OUTPUT_LAYER_LENGTH):
            weight_row.append(random())
        weights2.append(weight_row)

    for i in weights2:
        print(i)

    return input_dataset, output_dataset, weights1, weights2



def feed_forward(input, weights1, weights2):
    
    # print("Forward Propagation method called")
    hidden_layer = []
    output_layer = []

    # Forward feeding to the hidden layer: input * weights1
    for i in range(HIDDEN_LAYER_LENGTH): 
        weighted_sum = 0
        for j in range(INPUT_LAYER_LENGTH):
            weighted_sum += input[j] * weights1[j][i]
        weighted_sum = 1.0/(1.0 + exp(-weighted_sum))
        hidden_layer.append(weighted_sum)
    # print("Hidden Layer: ", hidden_layer)

    # Forward feeding to the output layer: hidden * weights2
    for i in range(OUTPUT_LAYER_LENGTH):
        weighted_sum = 0
        for j in range(HIDDEN_LAYER_LENGTH):
            weighted_sum += hidden_layer[j] * weights2[j][i]
        weighted_sum = 1.0/(1.0 + exp(-weighted_sum))
        output_layer.append(weighted_sum)
    # print("Output Layer: ", output_layer)

    return hidden_layer, output_layer



def back_propagation(input, hidden, output, weights1, weights2, expected_output):
    
    # print("Backward Propagation method called with input: ", input)

    # Copy the weight matrices for updates
    weights_hidden_output = weights2.copy()
    weights_input_hidden = weights1.copy()
    
    # Calculate Error gradients for the output layer and add them to a list
    delta_output = []
    for k in range(OUTPUT_LAYER_LENGTH):
        # Calculate error between expected and desired values
        error = expected_output[k] - output[k]
        # Calculate Error Gradient for the output layer
        delta_output.append(output[k] * (1 - output[k]) * error)
    # print("Error Gradients for the output layer: ", delta_output)

    # Calculate Error gradients for the hidden layer and add them to a list
    delta_hidden = []
    for j in range(HIDDEN_LAYER_LENGTH):             
        summation_gradient_weights_output = 0
        for k in range(OUTPUT_LAYER_LENGTH):
            summation_gradient_weights_output += delta_output[k] * weights2[j][k]
        delta_hidden.append(hidden[j] * (1 - hidden[j]) * summation_gradient_weights_output)
    # print("Error Gradients for the hidden layer: ", delta_hidden)

    # Propagate the error backwards and make weight corrections
    for k in range(OUTPUT_LAYER_LENGTH):
        for j in range(HIDDEN_LAYER_LENGTH):
            
            # Calculate weight correction for the weights between hidden and output layers and update the weight matrix
            weight_correction_hidden_output = LEARNING_RATE * hidden[j] * delta_output[k]
            weights_hidden_output[j][k] += weight_correction_hidden_output

            for i in range(INPUT_LAYER_LENGTH):
                weight_correction_input_hidden = LEARNING_RATE * input[i] * delta_hidden[j]
                weights_input_hidden[i][j] += weight_correction_input_hidden

   
    # return the updated weight values
    return weights_input_hidden, weights_hidden_output



def main():

    # Initialize the Neural network
    input_dataset, output_dataset, weights1, weights2 = initialize()
    print("\nSize of Input Dataset: ", len(input_dataset))
    print("Size of Output Dataset: ", len(output_dataset))
    print("Input Layer: ", INPUT_LAYER_LENGTH, " Hidden Layer: ", HIDDEN_LAYER_LENGTH, " Output Layer: ", OUTPUT_LAYER_LENGTH)
    print("Dimensions of First Weight Matrix: ", len(weights1), "X", len(weights1[0]))
    print("Dimensions of Second Weight Matrix: ", len(weights2), "X", len(weights2[0]))

    print("Weights between Input and Hidden Layer before training: ", weights1[3])
    print("\nWeights between Hidden and Output Layer before training: ", weights2[3])
    
    for epoch in range(NUM_EPOCHS):
        for i in range(len(input_dataset)):
            hidden_layer, output_layer = feed_forward(input_dataset[i], weights1, weights2) # Forward Propagation    
            w1, w2 = back_propagation(input_dataset[i], hidden_layer, output_layer, weights1, weights2, output_dataset[i]) # Backward Propagation
            weights1 = w1
            weights2 = w2

    print("Weights between Input and Hidden Layer after training: ", weights1[3])
    print("\nWeights between Hidden and Output Layer after training: ", weights2[3])
    
    # Test the neural network
    # Test for Bitmap 0
    test_input0 = [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0]
    hidden_layer, ff_output = feed_forward(test_input0, weights1, weights2)
    print("Output Layer upon forward feeding test input for Bitmap 0: ", ff_output)
    max = ff_output[0]
    max_index = 0
    for i in range(len(ff_output)):
        if ff_output[i] > max:
            max = ff_output[i]
            max_index = i
    print("Actual Output: ", max_index, " Desired Output: ", 0)
    
    # Test for Bitmap 2
    test_input3 = [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0]
    hidden_layer, ff_output = feed_forward(test_input3, weights1, weights2)
    print("Output Layer upon forward feeding test input for Bitmap 0: ", ff_output)
    max = ff_output[0]
    max_index = 0
    for i in range(len(ff_output)):
        if ff_output[i] > max:
            max = ff_output[i]
            max_index = i
    print("Actual Output: ", max_index, " Desired Output: ", 3)
    
    # Test for Bitmap 7
    test_input7 = [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0]
    hidden_layer, ff_output = feed_forward(test_input7, weights1, weights2)
    print("Output Layer upon forward feeding test input for Bitmap 0: ", ff_output)
    max = ff_output[0]
    max_index = 0
    for i in range(len(ff_output)):
        if ff_output[i] > max:
            max = ff_output[i]
            max_index = i
    print("Actual Output: ", max_index, " Desired Output: ", 7)
    

if __name__ == '__main__':
    main()
