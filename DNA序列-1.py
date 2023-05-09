n = str(input())
a = n.split('ATG')
print(a)
if a[0] != n:
    for i in range(0,len(a)):
        
        b = a[i].split('TAG')
        for j in range(0,len(b)):  
            if len(b[j]) == 0:
                continue
            elif len(b[j]) % 3 == 0:
                print(b[j])
                 
                
        c = a[i].split('TAA')
        for k in range(0,len(c)):
            if len(c[k]) == 0:
                continue
            elif len(c[k]) % 3 == 0:
                print(c[k])
                
        d = a[i].split('TGA')
        for l in range(0,len(d)):  
            if len(d[l]) == 0:
                continue
            elif len(d[l]) % 3 == 0:
                print(d[l])
else:
    print('None')