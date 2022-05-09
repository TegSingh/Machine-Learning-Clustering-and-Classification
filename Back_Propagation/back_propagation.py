from random import random, randint
from dataset import *

HIDDEN_LAYER_LENGTH = 15
INPUT_LAYER_LENGTH = 45
OUTPUT_LAYER_LENGTH = 10
NUM_REPLICAS = 4

# Method to Initialize the Artificial Neural Network
def initialize(): 

    input_dataset, output_dataset = initialize_dataset(NUM_REPLICAS)

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
    for i in range(HIDDEN_LAYER_LENGTH):
        weight_row = []
        for j in range(INPUT_LAYER_LENGTH):
            weight_row.append(random())
        weights1.append(weight_row)
    
    for i in weights1:
        print(i)

    print("\nMATRIX BETWEEN HIDDEN AND OUTPUT LAYER")
    weights2 = []
    for i in range(OUTPUT_LAYER_LENGTH):
        weight_row = []
        for j in range(HIDDEN_LAYER_LENGTH):
            weight_row.append(random())
        weights2.append(weight_row)

    for i in weights2:
        print(i)

    return input_dataset, output_dataset, weights1, weights2

def feed_forward(input, output, weights1, weights2):
    print("Forward Propagation method called")

def back_propagation():
    print("Backward Propagation method called")

def main():

    # Initialize the Neural network
    input_dataset, output_dataset, weights1, weights2 = initialize()
    for i in range(len(input_dataset)):
        feed_forward(input_dataset[i], output_dataset[i], weights1, weights2)
        

if __name__ == '__main__':
    main()
