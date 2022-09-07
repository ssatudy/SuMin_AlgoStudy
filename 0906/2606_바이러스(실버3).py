def push(item):
    global top
    top += 1
    S[top] = item

def pop():
    global top
    top -= 1
    return S[top+1]

node = int(input())
line = int(input())
S = [0]*(node)*2
top = -1
line_list = [[]*node for _ in range(node+1)]
virus = [0]*(node+1)

for i in range(line):
    n, m = map(int,input().split())
    line_list[n].append(m)
    line_list[m].append(n)

push(1)

while top != -1:
    now = pop()
    for i in line_list[now]:
        if virus[i] != 1:
            push(i)
            virus[i] = 1


print(sum(virus)-1)