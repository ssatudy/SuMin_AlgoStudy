num = int(input())

ga_max = 0
se_max = 0
v = []
ind = []
for i in range(6):
    a, b = map(int,input().split())
    if a <= 2 and ga_max < b:
        ga_max = b
    elif a > 2 and se_max < b:
        se_max = b
    v.append(b)
    ind.append(a)

ga_min = 0
se_min = 0
for i in range(6):
    if ind.count(ind[i]) == 2:
        if ind[i] <= 2:
            if i == 0:
                if v[-1] != se_max and v[1] != se_max:
                    ga_min = v[i]
            elif i == 5:
                if v[0] != se_max and v[4] != se_max:
                    ga_min = v[i]
            elif v[i-1] != se_max and v[i+1] != se_max:
                ga_min = v[i]
        else:
            if i == 0:
                if v[-1] != ga_max and v[1] != ga_max:
                    se_min = v[i]
            elif i == 5:
                if v[0] != ga_max and v[4] != ga_max:
                    se_min = v[i]
            elif v[i-1] != ga_max and v[i+1] != ga_max:
                se_min = v[i]

print(num*(ga_max*se_max - ga_min*se_min))