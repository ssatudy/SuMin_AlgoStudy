w, h = map(int,input().split())
p, q = map(int,input().split())
time = int(input())

nc = (p + time)
nr = q + time
if (nc//w)%2: # 가로 짝 홀 수 나누기
    x = w - (nc%w)
else:
    x = 0 + nc%w

if (nr//h)%2: # 세로 짝 수 홀 수 나누기
    y = h - (nr%h)
else:
    y = 0 + (nr%h)
print(x,y)
