N = int(input())

num_list = list(map(int,input().split()))

result = 0
if N <= 2:
    print(N)
else:
    cnt1 = cnt2 = 1
    result = 0
    for i in range(1,N):
        if num_list[i-1] <= num_list[i]:
            cnt1 += 1
        else:
            cnt1 = 1
        if num_list[i-1] >= num_list[i]:
            cnt2 += 1
        else:
            cnt2 = 1
        if result < cnt1:
            result = cnt1
        if result < cnt2:
            result = cnt2

    print(result)
