list1=['TAG','TAA','TGA']
n = str(input())
a = n.split('ATG')

if a[0] != n:    #字串沒有ATG就先剔除
    
    for i in range(0,len(a)):    #看n分割後有幾個字串
        
        for ii in range(0,len(list1)):    #將list1內的字串帶入迴圈
            b = a[i].split(list1[ii])     #將list1內的字串分割
            
            for j in range(0,len(b)):     #二維串列
                
                if len(b[j]) == 0:        #避免輸出空字串
                    continue
                
                elif b[j] == a[i]:        #可能還沒有分割到TAA，所以會一樣
                    continue
                
                elif len(b[j]) % 3 == 0:
                    print(b[j])
                 
else:
    print('None')