A, B = input().split()
a, b = len(A), len(B)
flag = False
for i in range(a):
    for j in range(b):
        if A[i] == B[j]:
            r = j
            c = i
            flag = True
            break
    if flag:
        break

for i in range(b):
    if i == r:
        print(A)
        continue
    for j in range(a):
        if j == c:
            print(B[i],end="")
            continue
        print('.',end="")
    print()

