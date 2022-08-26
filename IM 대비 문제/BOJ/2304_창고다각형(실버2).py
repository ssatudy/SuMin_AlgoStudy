N = int(input())
num_count = [0]*1001
max_y = 0
for i in range(N):
    x, y = map(int,input().split())
    if max_y < y:
        max_y = y
        max_x = x
    num_count[x] += y



now = 0
for i in range(max_x+1):
    if now < num_count[i]:
        now = num_count[i]
    num_count[i] = now

now = 0
for i in range(1000,max_x,-1):
    if now < num_count[i]:
        now = num_count[i]
    num_count[i] = now

print(sum(num_count))
