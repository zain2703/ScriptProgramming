import matplotlib.pyplot as plt
import numpy as np
###Assignment1
import csv
def refactor(rf,rows):
# print (rf)
 # den=2**(10-1)*0.6
 # print (den)
  for i in range(len(rows)):
    for j in range(len(rows[i])):
#        print(i,j) 
#        print (rows[i][j])
#        print (rf[i][j])
#      print(rf[i][j])
        rf[i][j]= int(rows[i][j]) / (2**10-1)*0.6

def mean(rf,avg):
   for i in range(len(rows)):
    for j in range(10):
      avg[i]=rf[i][j]+avg[i]
    avg[i]=avg[i]/10

def sub(rf,avg):
  for i in range(len(rows)):
    for j in range(len(rows[i])):
      rf[i][j]=avg[i]- rf[i][j]


## need to add the formula and stroe in same place

filename = "pulses.csv"
Drows,Dcols =(1000,56)
fields = [] 
rows = []
C1=[]
# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
  #  csvreader = csv.reader(csvfile, delimiter=",") 
    csvreader = csv.reader(csvfile)
    for i in csvreader:
     #print (i)
     #   print (i[0])
     fields.append(i[0])
     rows.append(i[2:56])
      #  C1[i]=i[0]
    # extracting field names through first row 
   # fields = next(csvreader) 
  
    # extracting each data row one by one 
   #  for row in csvreader: 
   #     rows.append(row[2:56]) 
    # get total number of rows 
#print("Total no. of rows: %d \n"%(csvreader.line_num)) 
#print(rows)
#print(rows[3][4])
r=len(rows)
c=len(rows[0])
print(c) 
print(r)
#rf=[]
rf = [[0 for i in range(c)] for j in range(r)]
#for i in range(r-1):
#    for j in range(c-1):
#      rf[r][c]=0
#print(rf)
#print(fields)

refactor(rf,rows)
#print(rf)
###Taking mean
avg=[0 for i in range(r)]
t= np.arange(0.,54.,1)
mean(rf,avg)

print(avg)
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
# giving a title to my graph 
plt.title('Two lines on same graph!') 
# printing the field names 
#x1 = [1,2,3] 
#y1 = [2,4,1]
#plt.subplot(2,1,1)
plt.plot(t, rf[0], label = "line 1") 
sub(rf,avg)
#plt.subplot(2,2,2)
plt.plot(t, rf[0], label = "line 2")
plt.show()
#print('Field names are:' + ', '.join(field for field in fields)) 




