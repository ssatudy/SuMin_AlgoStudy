for tc in range(1,int(input()) + 1):
    data = input()
    cnt = 0
    version = '0'
    for d in data:
        if version != d:
            version = d
            cnt += 1
    print(f'#{tc}',cnt)