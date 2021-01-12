import sequence
import matplotlib.pyplot as plt
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Create an instance of the Sequence class.
example_sequence1 = sequence.Sequence('AGCTAATA')
example_sequence2 = sequence.Sequence('AAGTAATA')

# sequences for spliting
Splitter_sequence_01='ATTTGAAGGTGGG'
    #This splitter sequence is most common found in shell task 4
Splitter_sequence='AAAAAAAAAATTTTTTTTTT'

# Call the first_base method on our instance. Notice that we don't specify the 'self' parameter when we call the method.
example_first_base = example_sequence1.first_base()

###### Task 1
example1_first_base = example_sequence2.first_base()
task_1=example1_first_base

###### Task 2
example_sequence2_base_count = example_sequence2.bases_in_DNA()
task_2=example_sequence2_base_count

###### Task3
task_3=example_sequence2.bool_dna()

###### Task4
task_4=example_sequence2.compliment_of_sequence()

##### Task5
task_5= example_sequence1.matching_sequence(example_sequence2.bases)

##### Task6
def read_genome_file(file):
    with open(file, "r") as genome:
        genome_read_lines= genome.readlines()
    return sequence.Sequence(genome_read_lines[1])

file_genome_01 = read_genome_file('genome_01.dat')
task_6=file_genome_01.bases_in_DNA()

##### Task7
splitted_genome_01 = file_genome_01.split_sequence(Splitter_sequence)
task_7=len(splitted_genome_01[0].bases)
task_7_1=len(splitted_genome_01)


##### Task8 
def genome_lengths(splitted_genome):
    genome_length=[]
    for i in range(len(splitted_genome)):
        genome_length.append(splitted_genome[i].bases_in_DNA())
    return genome_length

file_genome01_length = genome_lengths(splitted_genome_01)

##### Task 9
file_genome_02= read_genome_file('genome_02.dat')
compare_results = file_genome_02.compare_sequence(file_genome_01,Splitter_sequence)
task_9=compare_results[3]

################################################Extended tasks##################################################

##### Task 10
 
x = np.asarray(compare_results[1]).reshape(-1,1)  #### attribute gene length  
y = np.asarray(compare_results[2]).reshape(-1,1)  #### label numer of mutations

test_size=0.5
test_size_01 = 0.7

# Split raandomly into train and test subsets for both test size

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=test_size, random_state=0) 

x_train_01, x_test_01, y_train_01, y_test_01 = train_test_split(
    x, y, test_size=test_size_01, random_state=0) 

# regression model to find best fit for both test size

regression_model = LinearRegression()
regression_model.fit(x_train, y_train)
y_predicted = regression_model.predict(x_test)

regression_model_01 = LinearRegression()
regression_model_01.fit(x_train, y_train)
y_predicted_01 = regression_model_01.predict(x_test_01)

#Taking the root mean squared error to show difference
mean=round(np.sqrt(metrics.mean_squared_error(y_test, y_predicted)))
mean_01=round(np.sqrt(metrics.mean_squared_error(y_test_01, y_predicted_01)))

#stroing results for both test_size
task_10_test_size=regression_model.intercept_
task_10_1_test_size=regression_model.coef_
task_10_test_size_01=regression_model_01.intercept_
task_10_1_test_size_01=regression_model_01.coef_



#######################################Prints########################################################
print(f'The first base is: {example_first_base}')
print(f'Task 1: The first base by : {task_1}')
print(f'Task 2: Number of basses of sequence in Task1: {task_2}')
print(f'Task 3: DNA sequence of Task1: {task_3}')
print(f'Task 4: Compliment of Task1 sequence {example_sequence2.bases} is: {task_4}')
print(f'Task 5: Pair of non-matching bases: {task_5}')
print(f'Task 6: Total number of characters in "genome_01" is: {task_6}')
print(f'Task 7: Length of first genes is: {task_7}')
print(f'Task 7: Numer of DNA sequence "genome_01.dat" file: {task_7_1}')
print(f'Task 9: Total Number of DNA sequence "genome_02.dat" file: {task_9}')
print(f'Task 10: test_size={test_size} Intercept of predicted line : {task_10_test_size}')
print(f'Task 10: test_size={test_size} The slope of line is : {task_10_1_test_size}')
print(f'Task 10: test_size={test_size_01} Intercept of predicted line : {task_10_1_test_size_01}')
print(f'Task 10: test_size={test_size_01} The slope of line is : {task_10_1_test_size_01}')


#######################################Plots#########################################################

##### Task 8

#plotting the 2 subplots to represent genes length &number of genes with histogram and and scatter plot.
plt.subplots(1,figsize=(10,4), sharey=True, tight_layout=True)
#Subplot 1 for length of genes and number o genes
plt.suptitle("Genes in genome_01 file")
plt.subplot(1,2,1)
n, bins, patches = plt.hist(file_genome01_length,color='r')
#plt.title("Genes status in genome_01 file")
plt.xlabel("Length of genes")
plt.ylabel("Number of genes")
plt.grid(True)

#Subplot 2  for genes and number of genes
plt.subplot(1,2,2)
plt.plot(file_genome01_length, color='r')
plt.scatter(range(len(file_genome01_length)),file_genome01_length, color='b')

plt.xlabel("Genes")
plt.ylabel("No of genes")
plt.grid(True)

#saving data in files
plt.savefig("Task8.png")
plt.show()
plt.close()

##### Task 9

plt.scatter(compare_results[1], compare_results[2], color='b')
plt.rc('font', size=8)
plt.title(
    f" Task 9:'genome_02' vs 'genome_01'\n Mismatch count= {compare_results[0]}")
plt.xlabel("Length of genes")
plt.ylabel("Swap mutations")
plt.grid(True)
plt.savefig("Task9.png")
plt.show()
plt.close()

#### Task 10

#plotting the 2 subplots for both test size
plt.subplots(1,figsize=(10,4), sharey=True, tight_layout=True)

#Subplot 1 for  test_size
plt.suptitle(f"Task 10: Predicated Mutattion on genes length")
plt.subplot(1,2,1)
plt.plot(x_test, y_predicted, color='red')
plt.scatter(x_test, y_test, color='gray')
plt.title(f" Test size={test_size} and RMSD = {(mean,2)}")
plt.xlabel("Length of genes")
plt.ylabel("Swap mutations")
plt.legend(['Li Tations'])

#Subplot 2  for test_szie_01
plt.subplot(1,2,2)
plt.plot(x_test_01, y_predicted_01, color='red')
plt.scatter(x_test_01, y_test_01, color='gray')
plt.title(f" Test size={test_size_01} and RMSD = {(mean_01,2)}")
plt.xlabel("Length of genes")
plt.ylabel("Swap mutations")
plt.legend(['Linear regression','Mutations'])

#saving data in files
plt.savefig("Task10.png")
plt.show()
plt.close()
