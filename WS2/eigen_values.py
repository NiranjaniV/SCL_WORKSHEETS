import sympy as sp
x=sp.var('x')

def CALCULATE_EIGEN_VECTORS(A,l):
    length=A.shape[0]
    I=sp.eye(length)
    Z=I.multiply(l)
    H=A-Z
    J=H.nullspace()
    for i in range(len(J)):
        print("EIGEN VECTOR FOR EIGEN VALUE {} IS => {}".format(l,J[i].tolist()))   
    
def CALCULATE_EIGEN_VALUES(A):
    length=A.shape[0]
    I=sp.eye(length)
    Z=I.multiply(x)
    H=A-Z
    DET=H.det()
    print("EIGEN VALUE OF {} is {}\n".format(A.tolist(),sp.solve(DET,x)))
    L=sp.solve(DET,x)
    for i in L:
        CALCULATE_EIGEN_VECTORS(A,i)
    print("\n")

A=sp.Matrix([[4,0,1],[-2,1,0],[-2,0,1]])
B=sp.Matrix([[1,0,-2],[0,0,0],[-2,0,4]])
C=sp.Matrix([[6,3,-8],[0,-2,0],[1,0,-3]])
D=sp.Matrix([[3,0,0],[-2,7,0],[4,8,1]])

CALCULATE_EIGEN_VALUES(A)
CALCULATE_EIGEN_VALUES(B)
CALCULATE_EIGEN_VALUES(C)
CALCULATE_EIGEN_VALUES(D)
