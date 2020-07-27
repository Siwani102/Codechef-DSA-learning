T = int(input())
for i in range(T):
    G = int(input())
    for j in range(G):
        I, N, Q = input().split(" ")
        if (int(N)%2==0):
            mid = int(int(N)/2)  
            H = mid
            T1 = mid 
        else:
            if I == '1':
                H = int(int(N)//2)
                T1 = int(N) - H      
            else:
                T1 = int(int(N)//2)
                H = int(N) - T1         
        if Q == '1':
            print(H)
        elif Q == '2':
            print(T1)
            
            
        

                

