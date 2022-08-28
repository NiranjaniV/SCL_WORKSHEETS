# AGUMENT MATRIX

n = int(input("Enter the number of variables"))
m = int(input("Enter the number of equations"))
matrix = []
print("Enter the coefficient and rhs sep by ','")

for i in range(m):
    s = input()
    s = list(map(lambda x : int(x),s.split(',',maxsplit=n)))
    matrix.append(s)
    
print("the agumented matrix is ",matrix)

# REF AND RREF CHECKING

pos = -1
flag = 0
zero = [0]*(n+1)
for i in range(m):
    if matrix[i] == zero:
        for k in range(i+1,m):
            if matrix[k] != zero:
                print("Not a REF")
                flag = 1
    else:
        for index in range(0,n+1):
            if matrix[i][index] != 0:
                if index > pos:
                    pos = index                    
                    break
                else:
                    print("Not REF here in pos of  leading zero")
                    flag = 1
                    break

                    
        for k in range(i+1,m):
            if matrix[k][pos] != 0:
                print("Not REF cause below the leading non-zero not all are zero")
                flag = 1
                break

    if flag == 1:
        break
        
        
    else:
        if matrix[i][pos] != 1:
            print(pos)
            print('RF but not RREF')
            break
        
        for k in range(0,m):
            if k!=i:
                print(pos)
                if matrix[k][pos] !=0:
                    flag = 1
                    print("REF but not RREF")
                    break
         
    if flag == 1:
        break
 ------------------------------------------------------------------------
import numpy
ref = True
rref = True
arr = numpy.array([[1, 2, 0 ,3, 0],[0 ,0, 1, 1, 1],[0, 0, 0 ,0, 1],[0, 0, 0, 0, 0]])
row,col = arr.shape
for i in range(row):
    for j in range(col):
        if arr[i][j]==1 and i!=row-1:
            if j!=0 and arr[i][j]-arr[i][j-1]==0:
                continue
            for k in range(i+1,row):
                if arr[k][j]!=0:
                    ref = False
                    print("Not in REF")
                    break
            if i!=0:
             for l in range(i-1,-1,-1):
                if arr[l][j]!=0:
                    rref = False
                    print("Not in RREF")
                    break
if rref and ref:
    print("It is in rref")
elif ref:
    print("It is in Ref")
else :
    print("It is not in ref")
    
------------------------------
def augmented_matrix(eqn_list,eqn_count):
    aug_matrix=[]
    for i in eqn_list:
         val = re.findall(r'[\d\.\-\+]+',i)
         val = [int(x) for x in val]
         aug_matrix.append(val)
    return aug_matrix
        
