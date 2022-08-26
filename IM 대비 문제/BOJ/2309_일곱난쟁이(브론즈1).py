tall_list = []

for i in range(9):
    tall_list.append(int(input()))

for i in range(1<<9):
    part_list = []
    for j in range(9):
        if i&(1<<j):
            part_list.append(tall_list[j])
    if sum(part_list)==100 and len(part_list)==7:
        break
part_list.sort()
for i in part_list:
    print(i)
