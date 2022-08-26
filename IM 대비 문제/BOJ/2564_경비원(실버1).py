W, H = map(int,input().split())
N = int(input())

spot = []
for n in range(N+1):
    d,x = map(int,input().split())
    spot.append((d,x))



dis = []
for d,x in spot:
    if d == 1:
        dis.append(x)
    elif d == 2:
        dis.append(2*W+H-x)
    elif d == 3:
        dis.append(2*W+2*H-x)
    else:
        dis.append(W+x)

result = 0
for n in range(N):
    d = dis[-1] - dis[n] if dis[-1] > dis[n] else dis[n] - dis[-1]
    result += d if d < 2*W+2*H-d else 2*W+2*H-d
print(result)
