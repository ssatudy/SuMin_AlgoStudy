for tc in range(1,int(input()) + 1):
    N, M = map(int,input().split())
    table = [list(map(int,input().split())) for _ in range(N)]

    ans = 0                     # 결과 값
    for m in range(M):          # 빨간 사각형 값 받아오기
        r, c, n = map(int,input().split())  # 좌표 행, 열, 크기 받아오기
        for i in range(n):
            for j in range(n):
                cr = r + i
                cc = c + j      # tc로 저장하면 위의 test case를 줄인 tc와 중복되서 오답 발생.
                if 0 <= cr < N and 0 <= cc < N:
                    ans += table[cr][cc]     # 해당 영역 숫자를 ans에 더하기
                    table[cr][cc] = 0       # 중복 더하기 피하는 방법

    print(f'#{tc}',ans)
