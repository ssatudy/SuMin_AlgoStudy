for tc in range(1,11):
    N = int(input())
    table = [list(map(int,input().split())) for _ in range(N)]
    # 1은 N 2는 S     N극은 위 S 극은 아래
    ans = 0
    for c in range(N):
        cnt = 0
        for r in range(N):
            if table[r][c] == 1 and cnt != 1:
                cnt = 1
            elif table[r][c] == 2 and cnt == 1:
                ans += 1
                cnt = 0
    print(f'#{tc}',ans)
