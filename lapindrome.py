n = int(input())
list1 = []
for i in range(n):
    a = input()
    list1.append(a)

for j in list1:
   
    if (len(j)%2==0):
        a1 = j[:len(j)//2]
        
        a2 = j[len(j)//2:]
        l1 = list(a1)
        l2 = list(a2)
        l1.sort()
        l2.sort()
        
        
        if("".join(l1)=="".join(l2)):
            print('Yes')
        else:
            print('No')
    else: 
        a1=j[:len(j)//2]
        a2=j[len(j)//2+1:]
        l1 = list(a1)
        l2 = list(a2)
        l1.sort()
        l2.sort()
        if("".join(l1)=="".join(l2)):
            print('Yes')
        else:
            print('No')
       
    
    
        
        
    
