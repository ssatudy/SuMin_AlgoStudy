for tc in range(1,int(input())+1):
    N = int(input())
    result = [0] * N
    word = input().split()

    part1 = []
    part2 = []
    if N%2:
        for i in range(N//2+1):
            part1 += [word[i]]
        for i in range(N//2+1,N):
            part2 += [word[i]]
    else:
        for i in range(N//2):
            part1 += [word[i]]
        for i in range(N//2,N):
            part2 += [word[i]]

    for i in range(N):
        if i%2:
            result[i] = part2[(i-1)//2]
        else:
            result[i] = part1[i//2]
    print(f'#{tc}',*result)