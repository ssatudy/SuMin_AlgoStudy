def abc(now):
    global ans
    if now == 11:
        s = arr[0][0] + arr[1][1] + arr[2][2] + arr[3][3] + arr[4][4] + arr[5][5] + arr[6][6] + arr[7][7] + arr[8][8] + arr[9][9] + arr[10][10]
        if ans < s:
            ans = s
        return
    for i in range(now,11):
        if arr[i][now] != 0:
            arr[now], arr[i] = arr[i], arr[now]
            abc(now+1)
            arr[now], arr[i] = arr[i], arr[now]



for T in range(1, int(input()) + 1):
    arr = []
    ans = 0
    for i in range(11):
        n = list(map(int,input().split()))
        arr.append(n)

    abc(0)
    print(ans)