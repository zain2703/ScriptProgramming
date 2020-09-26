
import math
import numpy as np
import matplotlib.pyplot as plt
import time
import random

ITERATIONS_UPPER_LIMIT = 10000
MATRIX_SIZE_N = [x for x in range(100, 2200, 100)]
DefaultTol = 10**-6  # Default value
POWER_METHOD_CONVERGENCE = False

# Approach 1 – The Power Method with For Loops

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
    print('-------------------------------------------------------------------')
    print(strings)
    print('-------------------------------------------------------------------')

#def Approach1():


# User input for tolerance
while True:
    try:
        Tolerance = float(input('Enter tolerance in format 0.00...1='))
        if Tolerance > 0 and Tolerance < 1:
            break
    except:
        print('Invalid number default (10e⁻6) tolerane is set')
        Tolerance = DefaultTol
        break

time_record_approach_1 = []
time_record_approach_2 = []
time_record_approach_3 = []
rows, cols = (3,1)
Time = [[1]*cols]*rows

print("Length of Matrix_size =",(len(MATRIX_SIZE_N)))
print("Matrix =",(MATRIX_SIZE_N))
for i in range(len(MATRIX_SIZE_N)):
    a = [[random.random() for i in range(MATRIX_SIZE_N[i])]
         for j in range(MATRIX_SIZE_N[i])]
    eigenvector = [[1] for i in range(len(a))]  # Initial value of eigenvector

    time1 = time.time()
    iterations_counter = 0
    while True:
        dot_product = VectorProduct(a, eigenvector)
        eigenvalue = L2Norm(dot_product)
        new_eigenvector = ScalarDivision(dot_product, eigenvalue)
        difference = L2Norm(
            VectorSubtract(eigenvector, new_eigenvector))
        eigenvector = new_eigenvector

        iterations_counter += 1
        if difference < Tolerance:
            time2 = time.time()
            Print(f'Number of elements in matrix:{MATRIX_SIZE_N[i]}\n'
                        f'Number of iterations with approach 1: {iterations_counter}\n'
                        f'The l2 norm of difference between last two successive eigenvectors is: {difference}\n'
                        f'Eigenvalue is: {eigenvalue}\n'
                        f"Running time with 'Approach 1' is:{time2-time1} seconds!")
            time_record_approach_1.append(time2-time1)
            Time[0].append(time2-time1)
            break
        elif iterations_counter > ITERATIONS_UPPER_LIMIT:
            time2 = time.time()
            Print(
                f'Number of elements in matrix:{MATRIX_SIZE_N[i]}\n'
                f"The power method did not converge after:{ITERATIONS_UPPER_LIMIT} iterations! in 'Approach 1'\n"
                f"Running time with 'Approach 1' was:{time2-time1} seconds!")
            time_record_approach_1.append(math.nan)
            Time[0].append(math.nan)
            break

# ------------------------------------------------------------------------------------------------------
# Approach 2 – The Power Method with NumPy Functions
# To convert existing data to ndarray type
    a_np = np.asarray(a)
    eigenvector_np = np.ones((len(a_np), 1))

    time3 = time.time()
    iterations_counter = 0
    while True:
        dot_product_np = np.dot(a_np, eigenvector_np)
        eigenvalue_np = L2Norm(dot_product_np)
        new_eigenvector_np = dot_product_np / eigenvalue_np
        difference_np = L2Norm(eigenvector_np - new_eigenvector_np)
        eigenvector_np = new_eigenvector_np



        iterations_counter += 1
        if difference_np < Tolerance:
            time4 = time.time()
            Print(f'Number of elements in matrix:{MATRIX_SIZE_N[i]}\n'
                        f'Number of iterations with approach 2: {iterations_counter}\n'
                        f'The l2 norm of difference between last two successive eigenvectors is: {difference_np}\n'
                        f'Eigenvalue is: {eigenvalue_np}\n'
                        f"Running time with 'Approach 2' is:{time4-time3} seconds!")
            time_record_approach_2.append(time4-time3)
            Time[1].append(time4-time3)

            POWER_METHOD_CONVERGENCE = True
            break
        elif iterations_counter > ITERATIONS_UPPER_LIMIT:
            time4 = time.time()
            Print(
                f'Number of elements in matrix:{MATRIX_SIZE_N[i]}\n'
                f"The power method did not converge after:{ITERATIONS_UPPER_LIMIT} iterations! in 'Approach 2'\n"
                f"Running time with 'Approach 2' was:{time4-time3} seconds!")
            time_record_approach_2.append(math.nan)
            Time[1].append(math.nan)
            break

# ------------------------------------------------------------------------------------------------------
# Approach 3 – NumPy Implementation
    time5 = time.time()
    eig_values, eig_vects = np.linalg.eig(a_np)
    time6 = time.time()

    # Returns a bool array, where True if input element is real with no imaginary part
    real_eigenvalues_bo = np.isreal(eig_values)
    real_eigenvectors_bo = np.isreal(eig_vects)

    only_real_eigenvalues = eig_values[real_eigenvalues_bo]
    only_real_eigenvectors = eig_vects[real_eigenvectors_bo]

    if POWER_METHOD_CONVERGENCE:

        eigenvalue_places = np.where(
            (np.round(eig_values, 4)) == np.round(eigenvalue_np, 4))
        eigenvectors_places = np.where(
            (np.round(eig_vects, 4)) == np.round(eigenvector_np, 4))

        Print(f'Approach 3:\n'
                    f'Number of elements in matrix:{MATRIX_SIZE_N[i]}\n'
                    f'The place of biggest eigenvalue:{np.max(only_real_eigenvalues)} in '
                    f'main array result is:{eigenvalue_places[0]}\n'
                    f'Running time with Approach 3 was:{time6-time5} seconds!')
        Time[2].append(time6-time5)
        time_record_approach_3.append(time6-time5)
    else:
        Print(f'Number of elements in matrix:{MATRIX_SIZE_N[i]}\n'
                    f'Last calculated eigenvalue with Approach 1: {eigenvalue}\n'
                    f'Last calculated eigenvalue with Approach 2: {eigenvalue_np}\n'
                    f'Real eigenvalues with Approach 3 are:\n{only_real_eigenvalues}\n'
                    # f'Real eigenvectors with Approach 3 are:\n{only_real_eigenvectors}\n'
                    f"Running time with 'Approach 3' was:{time6-time5} seconds!\n"
                    f'The power method did not converged though!')
        time_record_approach_3.append(math.nan)
        Time[2].append(math.nan)
Time[0].pop(0)
Time[1].pop(0)
Time[2].pop(0)
print ("Approch1 = ",time_record_approach_1)
print ("Approch2 = ",time_record_approach_2)
print ("Approch3 = ",time_record_approach_3)
print ("The data in first row = ",Time[0])
print ("The data in second row = ",Time[1])
print ("The data in third row = ",Time[2])        
# ------------------------------------------------------------------------------------------------------
#  Performance characteristics of the approaches and result plotting
plt.subplots(1, figsize=(7, 7))
plt.loglog(MATRIX_SIZE_N, Time[0], '-*')
plt.loglog(MATRIX_SIZE_N, Time[1], '-o')
plt.loglog(MATRIX_SIZE_N, Time[2], '-d')

plt.title(
    f"Characteristics of the approaches with tolerance: {Tolerance}")
plt.ylabel('Running/Performance time for different approaches measured per seconds')
plt.xlabel('Matrix of size N')
plt.legend(['Approach 1', 'Approach 2', 'Approach 3'])
plt.savefig("Performance_of_approaches.png")

plt.show()
plt.clf()
plt.close()