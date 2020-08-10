T = int(input())
for i in range(T):
    K, d0, d1 = list(map(int, input().split()))
    Sum = d0 + d1
    number = (((2*Sum) % 10) + ((4*Sum) % 10) + ((8*Sum) % 10) + ((6*Sum) % 10))
    num_cycle = (K - 3)//4
    if K == 2:
        total = Sum
    else:
        total = Sum + Sum % 10 + number * num_cycle
        left_number = (K-3) - (num_cycle*4)
        a = 2
        for i in range(left_number):
            total += ((a*Sum) % 10)
            a = (a*2) % 10
            
    if total % 3 == 0:
        print("YES")
    else:
        print("NO")
    
