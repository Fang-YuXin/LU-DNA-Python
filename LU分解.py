import numpy as np
import sympy as sy

from fractions import Fraction
def amatrix():
    global list1
    m=eval(input('請輸入A的列數:'))
    n=eval(input('請輸入A的行數:'))
    
    list1=[]
    print('請輸入A矩陣元素(請由左至右、由上至下):')
    for i in range(m*n):
        a=float(Fraction(input()))
        list1.append(a)
    list1 = np.array(list1)
    list1 = list1.reshape(m,n)
    print(list1)
    
amatrix()

A = list1

A = sy.Matrix(A)
L,U,P = A.LUdecomposition()

sy.pprint(L)
sy.pprint(U)
sy.pprint(P) 