n = int(input())
list1, list2 = [],[]
for i in range(n):
    list1.append(int(input()))  
list1.sort()    
for i in range(n):
    total = list1[i] * (n-i)
    list2.append(total)
print(max(list2))  
