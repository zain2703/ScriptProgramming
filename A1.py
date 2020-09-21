import matplotlib.pyplot as plt
import numpy as np
###Assignment1
import csv

#question2 converting reading into voltages
def refactor(rf,rows):
  for i in range(len(rows)):
    for j in range(len(rows[i])):
        rf[i][j]= int(rows[i][j]) / (2**10-1)*0.6

#Question3 Compute the mean
def mean(rf,avg):
   for i in range(len(rows)):
    for j in range(10):
      avg[i]=rf[i][j]+avg[i]
    avg[i]=avg[i]/10

#Question3 subtract the mean
def sub(rf,avg):
  for i in range(len(rows)):
    for j in range(len(rows[i])):
      rf[i][j]=avg[i]- rf[i][j]


filename = "pulses.csv"
fields = [] 
rows = []
# Question1 reading csv file 
with open(filename, 'r') as csvfile: 
    csvreader = csv.reader(csvfile)
    for i in csvreader:
#Seperating time step and the readings
     fields.append(i[0])
     rows.append(i[2:56])

r=len(rows)
c=len(rows[0])
rf = [[0 for i in range(c)] for j in range(r)]

#Question 2 #Function to convert reading into Volatges
refactor(rf,rows)

#Question 3 #INitilizing the avg array with zero
avg=[0 for i in range(r)]
t= np.arange(0.,54.,1)
mean(rf,avg)

# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('Voltages') 
# giving a title to my graph 
plt.title('Pulse of single row!') 
plt.plot(t, rf[0]) 
plt.savefig("Pusle.png")
plt.show()
sub(rf,avg)
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('Voltages') 
# giving a title to my graph
plt.title('After Refactoring!') 
plt.plot(t, rf[0])
plt.savefig("Refactor.png")
plt.show()




