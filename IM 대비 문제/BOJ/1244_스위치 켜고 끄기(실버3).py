switch = int(input())
bulbe = list(map(int,input().split()))
student = int(input())
for i in range(student):
    x, y = map(int,input().split())
    s = y - 1
    if x == 1:
        for j in range(s,switch,y):
            if bulbe[j]:
                bulbe[j] = 0
            else:
                bulbe[j] = 1
    else:
        n = 1
        while s-n>=0 and s+n < switch and bulbe[s+n] == bulbe[s-n]:
            n += 1
        for j in range(s-n+1,s+n):
            if bulbe[j]:
                bulbe[j] = 0
            else:
                bulbe[j] = 1

for j in range(switch):
    if j > 1 and (j+1)%20 == 1:
        print()
    print(bulbe[j], end = " ")