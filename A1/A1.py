import matplotlib.pyplot as plt
###Assignment1
import csv

Volt_Con = (2**10-1)*0.6
BASELINE =10

#question2 converting reading into voltages
def convert_to_volt(rf,rows):
  for i in range(len(rows)):
    for j in range(len(rows[i])):
        rf[i][j]= float(rows[i][j]) / Volt_Con

#Question3 Compute the mean
def mean(rf,avg):
   for i in range(len(rows)):
    for j in range(BASELINE):
      avg[i]=rf[i][j]+avg[i]
    avg[i]=avg[i]/BASELINE

#Question3 subtract the mean
def sub(rf,avg):
  for i in range(len(rows)):
    for j in range(len(rows[i])):
      rf[i][j]=rf[i][j] - avg[i] 


filename = "pulses.csv"
fields = [] 
rows = []
# Question1 reading csv file 
with open(filename, 'r') as csvfile: 
    csvreader = csv.reader(csvfile)
    for i in csvreader:
#Question1 Seperating time step and the readings
     fields.append(i[0])
     rows.append(i[2:56])

r=len(rows)
c=len(rows[0])
rf = [[0 for i in range(c)] for j in range(r)]
#print("********************Rows****************************************************")
#print(rows)
#print("****************************************************************************")
#Question 2 #Function to convert reading into Volatges
convert_to_volt(rf,rows)
#print("********************RF******************************************************")
#print(rf[0][:5])
#print("****************************************************************************")
#Question 3 #INitilizing the avg array with zero
avg=[0 for i in range(r)]
#Question 3 To plot the x-axis 
t=[]
t=[0 for x in range(c)]
for i in range(c):
  t[i]=i
#print(i)
#print(t)
#t= np.arange(0.,54.,1)
mean(rf,avg)
#print("***************************Print Average************************************")
#print(len(avg))
#print(avg)
#print("****************************************************************************")
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
plt.title('Converted_to_Volatges!') 
plt.plot(t, rf[0])
plt.savefig("Refactor.png")
plt.show()




