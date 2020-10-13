
import math
import numpy as np
import matplotlib.pyplot as plt
import time
import random

ITERATIONS_LIMIT = 10000
##21 different size of matrix 
MATRIX_SIZE_N = [x for x in range(100, 2200, 100)]
DefaultTol = 10**-6  # Default value for tolerance
#Take different time
rows, cols = (3,1)
Time = [[0 for i in range(cols)] for j in range(rows)] 

def VectorProduct(matrix, vector):
    temp = 0
    temp_next_row = []
    method_result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            temp += matrix[i][j] * vector[j][0]
        temp_next_row.append(temp)
        method_result.append(temp_next_row)
        temp = 0
        temp_next_row = []
    return method_result


def L2Norm(vector):
    temp = 0
    for i in range(len(vector)):
        temp += (vector[i][0])**2
    return math.sqrt(temp)


def ScalarDivision(vector, scalar):
    temp = 0
    temp_next_row = []
    method_result = []
    for i in range(len(vector)):
        temp = vector[i][0] / scalar
        temp_next_row.append(temp)
        method_result.append(temp_next_row)
        temp = 0
        temp_next_row = []
    return method_result


def VectorSubtract(vector1, vector2):
    temp = 0
    temp_next_row = []
    method_result = []
    for i in range(len(vector1)):
        temp = vector1[i][0] - vector2[i][0]
        temp_next_row.append(temp)
        method_result.append(temp_next_row)
        temp = 0
        temp_next_row = []
    return method_result


def Print(strings):
    print('*******************************************************************')
    print(strings)
    print('*******************************************************************')

def Approach1(a,Approch1_eigenvalue,Approch1_eigenvector): 
    Approch1_eigenvector = [[1] for i in range(len(a))]  # Initial value of Approch1_eigenvector
    time1 = time.time()
    iterations_counter = 0
    while True:
        dot_product = VectorProduct(a, Approch1_eigenvector)
        Approch1_eigenvalue = L2Norm(dot_product)
        new_eigenvector = ScalarDivision(dot_product, Approch1_eigenvalue)
        difference = L2Norm(VectorSubtract(Approch1_eigenvector, new_eigenvector))
        Approch1_eigenvector = new_eigenvector

        iterations_counter += 1
        if difference < Tolerance:
            time2 = time.time()
            Print(f'Number of elements in matrix:{MATRIX_SIZE_N[i]}\n'
                        f'Number of iterations with approach 1: {iterations_counter}\n'
                        f'The l2 norm of difference between last two successive eigenvectors is: {difference}\n'
                        f'Approch1_eigenvalue is: {Approch1_eigenvalue}\n'
                        f"Running time with 'Approach 1' is:{time2-time1} seconds!")
            Time[0].append(time2-time1)
            break
        elif iterations_counter > ITERATIONS_LIMIT:
            Print(
                f'Number of elements in matrix:{MATRIX_SIZE_N[i]}\n'
                f"The power method did not converge after:{ITERATIONS_LIMIT} iterations! in 'Approach 1'\n"
                f"Running time with 'Approach 1' was:{time2-time1} seconds!")
            Time[0].append(math.nan)
            break

def Approach2(a_np,Approch2_eigenvalue,Approch2_eigenvector):
    time1 = time.time()
    iterations_counter = 0
    while True:
        dot_product_np = np.dot(a_np, Approch2_eigenvector)
        Approch2_eigenvalue = L2Norm(dot_product_np)
        new_eigenvector_np = dot_product_np / Approch2_eigenvalue
        difference_np = L2Norm(Approch2_eigenvector - new_eigenvector_np)
        Approch2_eigenvector = new_eigenvector_np
        iterations_counter += 1
        if difference_np < Tolerance:
            converge = True
            time2 = time.time()
            Print(f'Number of elements in matrix:{MATRIX_SIZE_N[i]}\n'
                        f'Number of iterations with approach 2: {iterations_counter}\n'
                        f'The l2 norm of difference between last two successive eigenvectors is: {difference_np}\n'
                        f'Approch1_eigenvalue is: {Approch2_eigenvalue}\n'
                        f"Running time with 'Approach 2' is:{time2-time1} seconds!")
            Time[1].append(time2-time1)
            break
        elif iterations_counter > ITERATIONS_LIMIT:
            time2 = time.time()
            Print(
                f'Number of elements in matrix:{MATRIX_SIZE_N[i]}\n'
                f"The power method did not converge after:{ITERATIONS_LIMIT} iterations! in 'Approach 2'\n"
                f"Running time with 'Approach 2' was:{time2-time1} seconds!")
            Time[1].append(math.nan)
            break
    return converge

def Approach3(converge,Approch1_eigenvalue,Approch2_eigenvalue,Approch3_eigenvalue,Approch3_eigenvector):
    time1 = time.time()
    eig_values, eig_vects = np.linalg.eig(a_np)
    time2 = time.time()

    # Returns a bool array, where True if input element is real with no imaginary part
    real_eigenvalues_bo = np.isreal(eig_values)
    real_eigenvectors_bo = np.isreal(eig_vects)

    Approch3_eigenvalue = eig_values[real_eigenvalues_bo]
    Approch3_eigenvector = eig_vects[real_eigenvectors_bo]
    if converge:

        eigenvalue_places = np.where(
            (np.round(eig_values, 4)) == np.round(Approch2_eigenvalue, 4))

        Print(      f'Number of elements in matrix:{MATRIX_SIZE_N[i]}\n'
                    f'The place of biggest Approch1_eigenvalue:{np.max(Approch3_eigenvalue)} in '
                    f'main array result is:{eigenvalue_places[0]}\n'
                    f'Running time with Approach 3 was:{time2-time1} seconds!')
        Time[2].append(time2-time1)
    else:
        Print(f'Number of elements in matrix:{MATRIX_SIZE_N[i]}\n'
                    f'Last calculated Approch1_eigenvalue with Approach 1: {Approch1_eigenvalue}\n'
                    f'Last calculated Approch1_eigenvalue with Approach 2: {Approch2_eigenvalue}\n'
                    f'Real eigenvalues with Approach 3 are:\n{Approch3_eigenvalue}\n'
                    f"Running time with 'Approach 3' was:{time2-time1} seconds!\n"
                    f'The power method did not converged though!')
        Time[2].append(math.nan)


# Getting user input for tolerance
while True:
    try:
        Tolerance = float(input('Enter tolerance in format 0.00...1='))
        if Tolerance > 0 and Tolerance < 1:
            break
    except:
        print('Invalid number default (10e⁻6) tolerane is set')
        Tolerance = DefaultTol
        break

###Eigenvalues & Eigenvectors for all aprooaches initlize with zero
Approch1_eigenvalue=Approch2_eigenvalue=Approch3_eigenvalue=0
Approch1_eigenvector=Approch2_eigenvector=Approch3_eigenvector=0
converge = False
#Approach1

for i in range(len(MATRIX_SIZE_N)):
    ##Initial value of eigenvector
    a = [[random.random() for i in range(MATRIX_SIZE_N[i])]
         for j in range(MATRIX_SIZE_N[i])]
    print('Approach 1')     
    Approach1(a,Approch1_eigenvalue,Approch1_eigenvector)  
# ------------------------------------------------------------------------------------------------------
# Approach 2 – The Power Method with NumPy Functions
# To convert existing data to ndarray type
    print('Approach 2')
    a_np = np.asarray(a)
    Approch2_eigenvector = np.ones((len(a_np), 1))
    converge=Approach2(a_np,Approch2_eigenvalue,Approch2_eigenvector)
    
###Just create the function to send the data 
# ------------------------------------------------------------------------------------------------------
# Approach 3 – NumPy Implementation
    print('Approach 3')
    Approach3(converge,Approch1_eigenvalue,Approch2_eigenvalue,Approch3_eigenvalue,Approch3_eigenvector)
   
# ------------------------------------------------------------------------------------------------------
#  Performance characteristics of the approaches and result plotting
##popout the starting values
Time[0].pop(0)
Time[1].pop(0)
Time[2].pop(0)

plt.subplots(1, figsize=(7, 7))
plt.loglog(MATRIX_SIZE_N, Time[0], '-*')
plt.loglog(MATRIX_SIZE_N, Time[1], '-o')
plt.loglog(MATRIX_SIZE_N, Time[2], '-d')

plt.title(
    f"Different approaches with tolerance: {Tolerance}")
plt.ylabel('Performance time for different approaches')
plt.xlabel('Size of a Matrix N')
plt.legend(['Approach 1', 'Approach 2', 'Approach 3'])
plt.savefig("A2.png")

plt.show()
plt.clf()
plt.close()