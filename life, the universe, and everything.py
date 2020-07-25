list1=[]
CheckNum = True
while CheckNum:
    n = int(input())
    if n!=42:
        list1.append(n)
    else:
        CheckNum = False

for i in list1:
    print(i)
