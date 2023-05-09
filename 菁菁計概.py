a="恭喜你抽到菁菁老師! all pass喔!"
b="恭喜你抽到亭甫老師! 經濟會過喔~"
c="恭喜你抽到承書老師! 線代會過喔~"
d="恭喜你抽到桂芳老師! 微積分會過喔~"
e="恭喜你抽到志偉老師! 微積分印象加分A_A"
f="恭喜你抽到瑞聰老師! 計概印象加分A_A"
g="恭喜你抽到震燦老師! 數導會過喔~"
h="恭喜你抽到英志老師! 全部被當!!"
import numpy as np
import random as rd
for num in range(10000):
    num = rd.random()
    if num <= 0.05:
        print(a)
        
    elif 0.05<num<=0.4:
        print(h)
    elif 0.4<num<=0.5:
        print(b)
    elif 0.5<num<=0.6:
        print(c)
    elif 0.6<num<=0.7:
        print(d)
    elif 0.7<num<=0.8:
        print(e)
    elif 0.8<num<=0.9:
        print(f)
    else:
        print(g)
        
計算次數 = 10000
成績結果 = []   # 將成績結果儲存在串列(list)中

for i in range(計算次數):
    點數 = rd.randint(0, 1)
    成績結果.append(點數)

print('平均值 =', np.mean(成績結果))
變異數 = np.var(成績結果)
print('變異數 =', 變異數)
print('標準差 =', 變異數**0.5)