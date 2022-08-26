num = int(input())

table = [[0]*100 for _ in range(100)]

for n in range(num):
    x, y = map(int,input().split())
    for r in range(y,y+10):
        for c in range(x,x+10):
            table[r][c] = 1


result = 0
for n in range(100):
    for m in range(100):
        result += table[n][m]
print(result)