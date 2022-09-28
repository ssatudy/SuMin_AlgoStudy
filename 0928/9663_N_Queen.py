def queen(level=0):
    global ans
    if level == N:
        ans += 1
        return
    for n in range(N):
        for y,x in xy:
            if x == n or abs(x-n) == abs(y-level):
                break
        else:
            xy.append((level,n))
            queen(level+1)
            xy.pop()

N = int(input())

ans = 0
xy = []
queen()
print(ans)

