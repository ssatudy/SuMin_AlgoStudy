c, r = map(int,input().split())
num = int(input())

c_list = [0,c]
r_list = [0,r]
for i in range(num):
    d, n = map(int,input().split())
    if d%2:
        c_list.append(n)
    else:
        r_list.append(n)

c_list.sort()
r_list.sort()

result = 0
height = 0
for dc in range(1,len(c_list)):
    for dr in range(1,len(r_list)):
        width = c_list[dc] - c_list[dc-1]
        height = r_list[dr] - r_list[dr-1]
        if result < width * height:
            result = width * height

print(result)