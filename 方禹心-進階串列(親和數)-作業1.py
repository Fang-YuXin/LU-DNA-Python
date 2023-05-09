a=int(input()) #輸入兩個數 判斷是否親和數
b=int(input())
list1=[] #設一串列 用以計算總合
list2=[]
for i in range(1,a):
    if a%i==0: #找a的因式
        list1.append(i) #把a的因式加到串列list1裡面,在串列裡面比較好加總
        x=sum(list1) #將串列裡的因式加總起來,放在迴圈內外都可,因為此程式碼只執行一次
for ii in range(1,b):
    if b%ii==0: #找b的因式
        list2.append(ii) #把b的因式加到串列list2裡面,在串列裡面比較好加總
        y=sum(list2) #將串列裡的因式加總起來,放在迴圈內外都可,因為此程式碼只執行一次
if a==y and b==x: #如果a=y,b=x 則判斷a b為親和數
    print("A and B is Amicable numbers.")
else: #其他的則不是親和數
    print("A and B is not Amicable numbers.")
