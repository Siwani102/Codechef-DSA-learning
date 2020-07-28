T = int(input())
for i in range(T):
    n, Nation = input().split(" ")
    sum = 0
    for i in range(int(n)):
        a = input()
        s = a.split(" ")
        if s[0] == 'CONTEST_WON':
            sum = sum + (300 + (20-int(s[1])))   
        elif s[0] == 'TOP_CONTRIBUTOR':
            sum = sum + 300    
        elif s[0] == 'BUG_FOUND':
            sum = sum + int(s[1])    
        elif s[0] == 'CONTEST_HOSTED':
            sum = sum + 50        
    if Nation == 'INDIAN':
        month = sum//200    
    elif Nation == 'NON_INDIAN':
        month = sum//400
    print(month)
