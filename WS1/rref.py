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
        
