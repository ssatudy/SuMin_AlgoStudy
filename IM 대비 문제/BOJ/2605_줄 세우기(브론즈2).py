num = int(input())

num_list = list(map(int,input().split()))
for i in range(num-1):
    for j in range(i+1,num):
        if num_list[i] >= num_list[j]:
            num_list[i] += 1
num_list = list(enumerate(num_list))
sort_list = []
for i in range(num-1):
    max_num = i
    for j in range(i+1, num):
        if num_list[max_num][1] <= num_list[j][1]:
            max_num = j
    num_list[max_num], num_list[i] = num_list[i], num_list[max_num]

# print(num_list)
for nums in num_list:
    print(nums[0]+1, end = ' ')
print()
