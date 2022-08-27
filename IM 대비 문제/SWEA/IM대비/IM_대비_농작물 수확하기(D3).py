def farm(N, i = 0, sum = 0):
    if i*2 + 1 == N:
        for c in range(N//2-i, N//2+i+1):
            sum += table[i][c]
        return sum

    for c in range(N // 2 - i, N // 2 + i + 1):
        sum += table[i][c]
    sum = farm(N,i+1,sum)

    for c in range(N//2-i, N//2+i+1):
        sum += table[N-i-1][c]

    return sum

for tc in range(1,int(input())+1):
    N = int(input())
    table = [list(map(int,input())) for _ in range(N)]
    print(f'#{tc}',farm(N))