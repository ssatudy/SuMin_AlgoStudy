def nCr(s,n,r,arr=[]):
    if r == 0:
        if arr:
            print(*arr)
        return

    for i in range(s,n-r+1):
        nCr(i+1,n,r-1,arr+[N[i]])

while True:
    N = list(map(int,input().split()))
    if N == [0]: break
    nCr(1,len(N),6)
    print()