from random import randint

value0 = [[0, 1, 1, 1, 0],
[1, 0, 0, 0, 1], 
[1, 0, 0, 0, 1], 
[1, 0, 0, 0, 1], 
[1, 0, 0, 0, 1], 
[1, 0, 0, 0, 1], 
[1, 0, 0, 0, 1], 
[1, 0, 0, 0, 1], 
[0, 1, 1, 1, 0]]

value1 = [[0, 0, 1, 0, 0],
[0, 1, 1, 0, 0], 
[1, 0, 1, 0, 0], 
[0, 0, 1, 0, 0], 
[0, 0, 1, 0, 0], 
[0, 0, 1, 0, 0], 
[0, 0, 1, 0, 0], 
[0, 0, 1, 0, 0], 
[0, 0, 1, 0, 0]]

value2 = [[0, 1, 1, 1, 0],
[1, 0, 0, 0, 1], 
[0, 0, 0, 0, 1], 
[0, 0, 0, 0, 1], 
[0, 0, 0, 1, 0], 
[0, 0, 1, 0, 0], 
[0, 1, 0, 0, 0], 
[1, 0, 0, 0, 0], 
[1, 1, 1, 1, 1]]

value3 = [[0, 1, 1, 1, 0],
[1, 0, 0, 0, 1], 
[0, 0, 0, 0, 1], 
[0, 0, 0, 0, 1], 
[0, 0, 0, 1, 0], 
[0, 0, 0, 0, 1], 
[0, 0, 0, 0, 1], 
[1, 0, 0, 0, 1], 
[0, 1, 1, 1, 0]]

value4 = [[0, 0, 0, 1, 0],
[0, 0, 1, 1, 0], 
[0, 0, 1, 1, 0], 
[0, 1, 0, 1, 0], 
[0, 1, 0, 1, 0], 
[1, 0, 0, 1, 0], 
[1, 1, 1, 1, 1], 
[0, 0, 0, 1, 0], 
[0, 0, 0, 1, 0]]

value5 = [[1, 1, 1, 1, 1],
[1, 0, 0, 0, 0], 
[1, 0, 0, 0, 0], 
[1, 1, 1, 1, 0], 
[1, 0, 0, 0, 1], 
[0, 0, 0, 0, 1], 
[0, 0, 0, 0, 1], 
[1, 0, 0, 0, 1], 
[0, 1, 1, 1, 0]]

value6 = [[0, 1, 1, 1, 0],
[1, 0, 0, 0, 1], 
[1, 0, 0, 0, 0], 
[1, 0, 0, 0, 0], 
[1, 1, 1, 1, 0], 
[1, 0, 0, 0, 1], 
[1, 0, 0, 0, 1], 
[1, 0, 0, 0, 1], 
[0, 1, 1, 1, 0]]

value7 = [[1, 1, 1, 1, 1],
[0, 0, 0, 0, 1], 
[0, 0, 0, 1, 0], 
[0, 0, 0, 1, 0], 
[0, 0, 1, 0, 0], 
[0, 0, 1, 0, 0], 
[0, 1, 0, 0, 0], 
[0, 1, 0, 0, 0], 
[0, 1, 0, 0, 0]]

value8 = [[0, 1, 1, 1, 0],
[1, 0, 0, 0, 1], 
[1, 0, 0, 0, 1], 
[1, 0, 0, 0, 1], 
[0, 1, 1, 1, 0], 
[1, 0, 0, 0, 1], 
[1, 0, 0, 0, 1], 
[1, 0, 0, 0, 1], 
[0, 1, 1, 1, 0]]

value9 = [[0, 1, 1, 1, 0],
[1, 0, 0, 0, 1], 
[1, 0, 0, 0, 1], 
[1, 0, 0, 0, 1], 
[0, 1, 1, 1, 1], 
[0, 0, 0, 0, 1], 
[0, 0, 0, 0, 1], 
[1, 0, 0, 0, 1], 
[0, 1, 1, 1, 0]]

def create_replication(input):

    value = input.copy()
    length = len(value)
    index_mutate = randint(0, length-1)
    if value[index_mutate] == 0:
        value[index_mutate] = 1
    else:
        value[index_mutate] = 0

    return value

# Method to Initialize dataset given the number of replications
def initialize_dataset(num_replicas):
    values = []
    values.append(value0)
    values.append(value1)
    values.append(value2)
    values.append(value3)
    values.append(value4)
    values.append(value5)
    values.append(value6)
    values.append(value7)
    values.append(value8)
    values.append(value9)

    # Initialize the input dataset
    input_dataset = []
    # convert the 2D arrays into 1 array and store in list
    for i in values:
        input1D = []
        for r in i:
            for value in r:
                input1D.append(value)
        
        input_dataset.append(input1D)
        # Add replications to the dataset
        for num in range(num_replicas):
            replica = create_replication(input1D)
            input_dataset.append(replica)
    
    # Initialize the output dataset
    output_dataset = []
    for i in range(len(values)):
        for j in range(num_replicas + 1):
            output_dataset.append(i)

    return input_dataset, output_dataset
