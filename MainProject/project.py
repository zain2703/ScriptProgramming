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


###### Task 1
example_sequence2 = sequence.Sequence('AAGTAATA')
example1_first_base = example_sequence2.first_base()
print(f'Task 1: The first base by : {example1_first_base}')

###### Task 2
example_sequence2_base_count = example_sequence2.bases_in_DNA()
print(f'Task 2: Number of basses of sequence in Task1: {example_sequence2_base_count}')

###### Task3
print(f'Task 3: DNA sequence of Task1: {example_sequence2.bool_dna()}')

###### Task4
print(f'Task 4: Compliment of Task1 sequence {example_sequence2.bases} is: {example_sequence2.compliment_of_sequence()}')

##### Task5
print(f'Task 5: Pair of non-matching bases: {example_sequence1.matching_sequence(example_sequence2.bases)}')

##### Task6
def read_genome_file(file):
    with open(file, "r") as genome:
        genome_read_lines= genome.readlines()
    return sequence.Sequence(genome_read_lines[1])

file_genome_01 = read_genome_file('genome_01.dat')
print(f'Task 6: Total number of characters in "genome_01" is: {file_genome_01.bases_in_DNA()}')


#Splitter_sequence='ATTTGAAGGTGGG'
Splitter_sequence='AAAAAAAAAATTTTTTTTTT' ##this splitter sequence is most common found in shell task 4

##### Task7
splitted_genome_01 = file_genome_01.split_sequence(Splitter_sequence) 
print(f'Task 7: Length of first genes is: {len(splitted_genome_01[0].bases)}')
print(f'Task 7: Numer of DNA sequence "genome_01.dat" file: {len(splitted_genome_01)}')

##### Task8 
def genome_lengths(splitted_genome):
    genome_length=[]
    for i in range(len(splitted_genome)):
        genome_length.append(splitted_genome[i].bases_in_DNA())
    return genome_length

file_genome01_length = genome_lengths(splitted_genome_01)

#print(file_genome01_length) 

##### Task 9
file_genome_02= read_genome_file('genome_02.dat')
compare_results = file_genome_02.compare_sequence(file_genome_01,Splitter_sequence)
print(f'Task 9: Total Numer of DNA sequence "genome_02.dat" file: {compare_results[3]}')


################################Plots#########################################################
#####plots for Task 8
#plotting the 2 subplots one showing number of genes and other showing length of genes
plt.subplots(1,figsize=(10,4), sharey=True, tight_layout=True)
#Subplot 1 for length of genes and number o genes
plt.suptitle("Genes in genome_01 file")
plt.subplot(1,2,1)
n, bins, patches = plt.hist(file_genome01_length,color='r', rwidth=0.8, alpha=0.75)
#plt.title("Genes status in genome_01 file")
plt.xlabel("Length of genes")
plt.ylabel("Number of genes")
plt.grid(True)

#Subplot 2  for genes and number of genes
plt.subplot(1,2,2)
plt.plot(file_genome01_length, color='r', linewidth=0.8)
plt.scatter(range(len(file_genome01_length)),file_genome01_length, color='b')

plt.xlabel("Genes")
plt.ylabel("No of genes")
plt.grid(True)

#saving data in files
plt.savefig("Task8.png")
plt.show()
plt.close()

####plots for Task 9
plt.scatter(compare_results[1], compare_results[2], color='b')
plt.rc('font', size=8)
plt.title(
    f" Task 9:'genome_02' vs 'genome_01'\nNumber of bases (dots) with mismatch is: {compare_results[0]}")
plt.xlabel("Length of genes")
plt.ylabel("Swap mutations")
plt.grid(True)
plt.savefig("Task9.png")
plt.show()
plt.close()

################################################Extended tasks##################################################

######Task 10





