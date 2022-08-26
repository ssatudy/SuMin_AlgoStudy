import sys

cases = int(sys.stdin.readline())

table = [[0]*1001 for _ in range(1001)]
for case in range(cases):
    x1,y1,width,height = map(int,sys.stdin.readline().split())
    for i in range(y1,y1+height):
        for j in range(x1,x1+width):
            table[i][j] = case+1

for case in range(cases):
    t_result = 0
    for i in range(1001):
        for j in range(1001):
            if table[i][j] == case + 1:
                t_result += 1
    print(t_result)