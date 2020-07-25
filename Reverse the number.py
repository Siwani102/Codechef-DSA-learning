n = int(input())
list1 = []
for i in range(n):
    a = input()
    b = a[::-1]
    while(b[0] == '0'):
        b = b[1::]
    list1.append(b)
for i in list1:
    print(i)
