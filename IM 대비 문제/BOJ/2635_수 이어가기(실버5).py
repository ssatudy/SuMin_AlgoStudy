N = int(input())

if N == 1:
    print(4)
    print(1,1,0,1)
elif N >= 15:
    r = 2*N//3 + 2
    l = 3*N//5 - 1
    max_cnt = 0
    for n in range(l,r):
        num_list = [N,n]
        i = 0
        num = num_list[i] - num_list[i + 1]
        while num>=0:
            num_list.append(num)
            i += 1
            num = num_list[i] - num_list[i+1]
        if max_cnt < len(num_list):
            max_cnt = len(num_list)
            result = num_list[:]
    print(max_cnt)
    print(*result)
else:
    max_cnt = 0
    for n in range(1,N):
        num_list = [N,n]
        i = 0
        num = num_list[i] - num_list[i + 1]
        while num >= 0:
            num_list.append(num)
            i += 1
            num = num_list[i] - num_list[i + 1]
        if max_cnt < len(num_list):
            max_cnt = len(num_list)
            result = num_list[:]
    print(max_cnt)
    print(*result)