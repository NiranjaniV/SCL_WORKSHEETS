n = int(input("Enter the number of rows"))
m = int(input("Enter the number of cols"))

a = []
b = []
final = []
for i in range(n):
    b = []
    for j in range(m):
        t = int(input())
        b.append(t)
    a.append(b);
    
    
print("The matrix you entered is :",a);

flag = 1;
iter_ = 0
zero = [0]*m
b=[]
while flag:
    c = 0
    b = []
    for i in a:
        if i != zero:
            b.append(i)
        else:
            c +=1
    j=0
    while j<c:
        b.append(zero)
        j+=1
    
    print("The array with all zeroes in the bottom is :",b)
    
    pos = m+1;
    value = -1000
    swap = 0;
    for i in range(n-c):
        for j in range(m):
            if b[i][j] != 0:
                if j<=pos and value<b[i][j]:
                    value = b[i][j]
                    pos = j
                    swap = i
                    
            break;
    if pos == m+1:
        pos = 0
    
    c_ = b[swap]
    b[swap] = b[0]
    b[0] = c_
    
    print(b[0])
    
    scalar = b[0][pos]
    
    if scalar!=0:
        for i in range(m):
            b[0][i] /=scalar
    
    print("After converting the leading 1 to 1 : ",b)
    
    for i in range(1,n):
        scalar = b[i][pos]
        if scalar != 0:
            for j in range(m):
                b[i][j] -= scalar*b[0][j]
     
    print("After making all the values in the column of leading 1 zero : ",b)
    
    if len(b) == 1:
        flag = 0
        d = [0]*iter_ + b[0]
        final.append(d)
        
    else:
        d = [0]*iter_ + b[0]
        final.append(d)
        a = []
        for i in range(1,n):
            a_ = []
            for j in range(1,m):
                a_.append(b[i][j])
            a.append(a_)
        
        print("Matrix for next iteration : ",a)
        n = n-1
        m = m-1
        iter_ +=1 
               
print("Gauss jordern elemination : ",final)  
                
-----------------------------------------------------------
import numpy as np
import sys

# Reading number of unknowns
n = int(input('Enter number of unknowns: '))

# Making numpy array of n x n+1 size and initializing 
# to zero for storing augmented matrix
a = np.zeros((n,n+1))

# Making numpy array of n size and initializing 
# to zero for storing solution vector
x = np.zeros(n)

# Reading augmented matrix coefficients
print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

# Applying Gauss Jordan Elimination
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Divide by zero detected!')
        
    for j in range(n):
        if i != j:
            ratio = a[j][i]/a[i][i]

            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]

# Obtaining Solution

print("Matrix is :",a)
for i in range(n):
    x[i] = a[i][n]/a[i][i]

# Displaying solution
print('\nRequired solution is: ')
for i in range(n):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')
        
-------------------------------------------------------------------------------
import math
def non_zero(row):
  for i in range(len(row)):
    if row[i] != 0:
      return i

def rref(matrix):
  rows = len(matrix)
  columns = len(matrix[0])
  non_zero_index = -1

  # Arrange the rows by leftmost non-zero entry
  matrix.sort(key = non_zero)
  for i in range(0, rows):
  # Making the first non-zero element 1
    for j in range(columns):
      if not math.isclose(matrix[i][j], 0.0):
        non_zero_index = j
        matrix[i] = [x / matrix[i][j] for x in matrix[i]]
        break

  # Making leading coefficient column corresponding values 0
    for j in range(rows):
      if j == i:
        continue
      else:
        ratio = matrix[j][non_zero_index] / matrix[i][non_zero_index]
        row = [x * ratio for x in matrix[i]]
        matrix[j] = [x - y for x, y in zip(matrix[j], row)]
  print("The given matrix in RREF is:")
  for row in matrix:
    print(row)
  return matrix

lin_sys = ["1x1 + 1x2 + 2x3 = 8", "-1x1 - 2x2 + 3x3 = 1", "3x1 - 7x2 + 4x3= 10"]

# Finding the augmented matrix
aug = []
for eqn in lin_sys:
  row = []
  for i in range(len(eqn)):
    if eqn[i] == 'x':
      if eqn[i - 2] == '-' or eqn[i - 3] == '-':
        row.append(-int(eqn[i - 1]))
      else:
        row.append(int(eqn[i - 1]))
    if eqn[i] == '=':
      row.append(int(eqn[i + 1:]))
  aug.append(row)
    
aug = rref(aug)
rank = len(aug)
zeros = [0] * len(aug[0])
solution = []
for row in aug:
  if row == zeros:
    rank -= 1
# Unique Solution
if rank == len(aug[0]) - 1:
  for i in range(len(aug) - 1, -1, -1):
    for j in range(len(aug[0]) - 1):
      if math.isclose(aug[i][j], 0.0):
        continue
      else:
        solution.insert(0, aug[i][len(aug[0]) - 1])
  print("Unique Solution:", solution)
# Infinite Solutions
elif rank < len(aug[0]) - 1:
  print("Infinite Solutions")
# No solution
else:
  print("No Solution")
