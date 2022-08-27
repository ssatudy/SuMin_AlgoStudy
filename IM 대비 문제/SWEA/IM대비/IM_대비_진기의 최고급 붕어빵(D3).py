for tc in range(1,int(input()) + 1):
    N, M, K = map(int,input().split()) # N 명 사람, M초 시간, K 개 붕어빵
    sec = list(map(int,input().split())) # 각 사람이 언제 오는지

    counting = [0]*11115    # 초 마다 붕어빵 개수 저장용 배열
    num_max = 0
    for i in sec:           # 손님 오는 시간 마다 -1 해주기
        counting[i] -= 1
        if num_max < i:
            num_max = i

    i = 1
    while i*M <= 11114:     # 붕어빵 나오는 시간마다 +K개 해주기
        counting[i*M] += K
        i += 1

    result = 'Possible'
    for i in range(0,11114):
        counting[i+1] = counting[i] + counting[i+1]
        if counting[i] < 0:        # 모든 시간에서 음수가 있으면 못 받아가는 손님이 있다는 의미
            result = 'Impossible'
            break

    print(f'#{tc}', result)