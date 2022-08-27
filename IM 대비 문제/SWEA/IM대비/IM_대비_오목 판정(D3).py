for tc in range(1,int(input())+1):
    N = int(input())
    table = [list(input()) for _ in range(N)]
    result = 0
    dr = [1,1]
    dc = [-1,1]
    for i in range(N):
        r_cnt = 0
        c_cnt = 0
        for j in range(N):  # 가로 세로
            if table[i][j] == 'o':
                r_cnt += 1
            else:                       # o가 아닌 .이 나오면 다시 숫자 세기
                r_cnt = 0
            if table[j][i] == 'o':
                c_cnt += 1
            else:                       # o가 아닌 .이 나오면 다시 숫자 세기
                c_cnt = 0

            if r_cnt == 5 or c_cnt == 5:
                result = 1
                break

            for d in range(2):          # 대각선 방향 (좌상 우하, 우상 좌하)
                cr_cnt = 0
                for k in range(5):      # 대각선 길이 가중치
                    r = i + dr[d]*k
                    c = j + dc[d]*k
                    if 0 <= r < N and 0<= c < N:
                        if table[r][c] == 'o':
                            cr_cnt += 1
                        else:
                            cr_cnt = 0
                        if cr_cnt == 5:
                            result = 1
                            break

                if result:
                    break

        if result:
            break

    print(f'#{tc}', end = " ")
    print('YES') if result else print('NO')