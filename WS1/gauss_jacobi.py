from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot

def jacobi(A, b, N=25, x=None):
    if x is None:
        x = zeros(len(A[0]))
    D = diag(A)
    R = A - diagflat(D)
    for i in range(N):
        x = (b - dot(R, x)) / D
    return x


n = int(input("Enter the number of equations: "))
m = int(input("Enter the number of unknowns: "))
a = []
c=[]
for i in range(n):
    b = []
    for j in range(m+1):
        if j == m:
            num = int(input("Enter constant term: "))
            c.append(num)
        else:
            num = int(input("Enter matrix entry ["+str(i)+"]["+str(j)+"]: "))
            b.append(num)
    a.append(b)
# print(a)
# print(c)
print("Input Matrix :")
for i in range(len(a)):
    print(a[i])
    
A = array(a)
b = array(c)
guess = array([1.0]*n)
sol = jacobi(A, b, N=25, x=guess)
print("A: ")
pprint(A)
print("B: ")
pprint(b)
print("x = ")
pprint(sol)

-------------------------------
def f1(x,y,z):
    return (2-y-z)/4
def f2(x,y,z):
    return (-6-x-2*z)/5
def f3(x,y,z):
    return (-4-x-2*y)/3


x0 = 0
y0 = 0
z0 = 0

count =1

e = float(input("Enter the tolerable error"))
condition = True

while condition:
    x1 = f1(x0,y0,z0)
    y1 = f2(x0,y0,z0)
    z1 = f3(x0,y0,z0)
    
    print("%d\t%0.4f\t%0.4f\t%0.4f\t",(count,x1,y1,z1))
    e1 = abs(x1-x0)
    e2 = abs(y1-y0)
    e3 = abs(z1-z0)
    
    count+=1
    x0=x1
    y0=y1
    z0=z1
    
    condition = e1>e and e2>e and e3>e
    
    print('\nSolution: x=%0.3f, y=%0.3f and z = %0.3f\n'% (x1,y1,z1))
