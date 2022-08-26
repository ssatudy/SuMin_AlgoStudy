N, K = map(int,input().split())
temp = list(map(int,input().split()))

for t in range(1,N):
    temp[t] = temp[t-1] + temp[t]

max_t = temp[K-1]
for t in range(K,N):
    if max_t < temp[t] - temp[t-K]:
        max_t = temp[t] - temp[t-K]
print(max_t)