for tc in range(1, int(input()) + 1):
    N, M = map(int,input().split())
    table = [list(map(int,input().split())) for _ in range(N)]
    bomb = [list(map(int,input().split())) for _ in range(M)]

    # 델타 사용해서 방문한 곳은 1로 체크하는 방법말고 set으로 중복 값 제거해보자
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]

    kill_set = set()
    for r, c, k in bomb:
        for i in range(k+1):
            for j in range(4):
                cr = r + dr[j]*i
                cc = c + dc[j]*i
                if 0 <= cr < N and 0 <= cc < N:
                    kill_set |= {(cr,cc)}

    ans = 0
    for r, c in kill_set:
        ans += table[r][c]

    print(f'#{tc}',ans)