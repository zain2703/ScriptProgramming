import sequence
import matplotlib.pyplot as plt
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Create an instance of the Sequence class.
example_sequence1 = sequence.Sequence('AGCTAATA')

# Call the first_base method on our instance. Notice that we don't specify the 'self' parameter when we call the method.
example_first_base = example_sequence1.first_base()
print(f'The first base is: {example_first_base}')


# Task 1
example_sequence2 = sequence.Sequence('AAGTAATA')
example1_first_base = example_sequence2.first_base()
print(f'Task 1: The first base by : {example1_first_base}')

# Task 2
example_sequence2_base_count = example_sequence2.bases_in_DNA()
print(f'Task 2: Number of basses of sequence in Task1: {example_sequence2_base_count}')

# Task3
print(f'Task 3: DNA sequence of Task1: {example_sequence2.bool_dna()}')

# Task4
print(f'Task 4: compliment of Task1 sequence {example_sequence2.bases} is: {example_sequence2.compliment_of_sequence()}')

# Task5
print(f'Task 5: pair of non-matching bases: {example_sequence1.matching_sequence(example_sequence2.bases)}')


