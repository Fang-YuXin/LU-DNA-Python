import numpy as np
from fractions import Fraction

def 程式碼():
    global list1
    global list2
    global m
    m=eval(input('請輸入L的行列數和U的列數:'))
    n=eval(input('請輸入U的行數:'))

    list1=[]
    print('請輸入L矩陣元素(請由左至右、由上至下):')
    for i in range(m*m):
        a=float(Fraction(input()))
        list1.append(a)
    list1 = np.array(list1)
    list1 = list1.reshape(m,m)
    print(list1)
    
    list2=[]
    print('請輸入U矩陣元素(請由左至右、由上至下):')
    for i in range(m*n):
        b=float(Fraction(input()))
        list2.append(b)
    list2 = np.array(list2)
    list2 = list2.reshape(m,n)
    print(list2)
    
def 程式碼P():
    global list3
    list3=[]
    print('請輸入P矩陣元素(請由左至右、由上至下):')
    for j in range(m*m):
        c=float(Fraction(input()))
        list3.append(c)
    list3 = np.array(list3)
    list3 = list3.reshape(m,m)
    print(list3)
    list3 = np.linalg.inv(list3)
    
    
d=str(input('是否有需輸入P(Yes/No):'))
if d=='Yes' or d=='yes' or d=='YES':    
    程式碼()
    程式碼P()
    e=str(input('若P、L、U無誤請輸入Yes、若有誤請輸入No:'))    
    if  e=='Yes' or e=='yes' or e=='YES':
        print(list3@list1@list2)
    elif e=='no' or e=='No' or e=='NO':
        程式碼()
    else:
        print('請勿來亂、請重新輸入')
        程式碼()
elif d == 'No' or d == 'no' or d == 'NO':
    程式碼()
    f=str(input('若L和U無誤請輸入Yes、若有誤請輸入No:'))    
    if  f=='Yes' or f=='yes' or f=='YES':
        print(list1@list2)
    elif f=='no' or f=='No' or f=='NO':
        程式碼()
    else:
        print('請重新輸入')
        程式碼()
else:
    print('請重新執行')
    
    


    
    