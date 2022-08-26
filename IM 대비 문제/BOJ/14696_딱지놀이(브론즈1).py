# 별 > 동그라미 > 네모 > 세모 > 무승부

R = int(input()) # 라운드
for r in range(R):
    aa = list(map(int,input().split()))
    bb = list(map(int,input().split()))
    a = aa[1:]
    b = bb[1:]
    a.sort(reverse=True)
    b.sort(reverse=True)
    i, j = 0, 0
    result = 0
    while i < len(a) and j < len(b):
        if a[i] == b[i]:
            i += 1
            j += 1
            continue
        else:
            result = 'A' if a[i]>b[i] else 'B'
            break

    if result != 0:
        pass
    elif len(a) != len(b):
        result = 'A' if len(a) > len(b) else 'B'
    else:
        result = 'D'
    print(result)