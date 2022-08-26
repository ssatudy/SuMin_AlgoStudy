C, R = map(int,input().split())
target = int(input())
r, c = R-1, 0

table = [[0]*C for _ in range(R)]

result = 0
table[r][c] = 1
i = 2; d = 0
dr = [-1,0,1,0]
dc = [0,1,0,-1]
while i <= C*R:
    r = r + dr[d]
    c = c + dc[d]
    if 0 <= r < R and 0 <= c < C and table[r][c] == 0:
        table[r][c] = i
    else:
        r = r - dr[d]
        c = c - dc[d]
        d = (d+1)%4
        i -= 1
    if i == target:
        result = (c,r)
    i += 1

if target == 1:
    print(1,1)
elif R*C < target:
    print(0)
else:
    x, y = result
    x = x + 1
    y = R - y
    print(x,y)