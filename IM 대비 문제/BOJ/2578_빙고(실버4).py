import sys
table = [list(map(int,sys.stdin.readline().split())) for _ in range(5)]
call_table = [list(map(int,sys.stdin.readline().split())) for _ in range(5)]
bingo_dict = {}
for r in range(5):
    for c in range(5):
        bingo_dict[call_table[r][c]] = (r,c)

bingo = []
max_bingo3 = 0
max_bingo4 = 0
for r in range(5):
    max_bingo1 = 0
    max_bingo2 = 0
    r3, c3 = bingo_dict[table[r][r]]
    r4, c4 = bingo_dict[table[4-r][r]]
    if max_bingo3 < (r3*5) + (c3 + 1):
        max_bingo3 = (r3*5) + (c3 + 1)
    if max_bingo4 < (r4*5) + (c4 + 1):
        max_bingo4 = (r4*5) + (c4 + 1)
    for c in range(5):
        r1, c1 = bingo_dict[table[r][c]]
        r2, c2 = bingo_dict[table[c][r]]
        if max_bingo1 < (r1*5)+(c1+1):
            max_bingo1 = (r1*5)+(c1+1)
        if max_bingo2 < (r2*5)+(c2+1):
            max_bingo2 = (r2*5)+(c2+1)
    bingo.append(max_bingo1)
    bingo.append(max_bingo2)
bingo.append(max_bingo4)
bingo.append(max_bingo3)
bingo.sort()

print(bingo[2])


