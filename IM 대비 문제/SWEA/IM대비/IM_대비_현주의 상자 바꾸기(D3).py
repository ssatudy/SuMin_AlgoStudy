for tc in range(1,int(input())+ 1):
    N, Q = map(int,input().split())
    num_list = [0] * N
    for i in range(Q):
        L, R = map(int,input().split())
        for j in range(L-1,R):
            num_list[j] = i+1

    print(f'#{tc}',*num_list)