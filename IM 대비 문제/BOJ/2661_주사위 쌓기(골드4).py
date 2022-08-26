N = int(input())
dices = []
for case in range(N):
    a, b, c, d, e, f = map(int,input().split())
    dices.append([a,f,b,d,c,e])

top = 0
result = 0
for i in range(6):
    num_sum = 0
    # 첫 주사위는 내가 위치를 조정할 수 있음
    dice = dices[0][:]
    if i % 2:  # 홀수이면 그 전 숫자와 짝지
        bottom = dice[i]
        top = dice[i - 1]
        dice.remove(top)
        dice.remove(bottom)
        num_sum += max(dice)
    else:  # 짝수이면 그 뒤 숫자와 짝지
        bottom = dice[i]
        top = dice[i + 1]
        dice.remove(top)
        dice.remove(bottom)
        num_sum += max(dice)
    for j in range(1,N): # 두 번째 주사위 ~ 끝까지
        dice = dices[j][:] # 다음 주사위 설정
        for k in range(6):
            if dice[k] == top:
                if k%2:
                    bottom = dice[k]
                    top = dice[k - 1]
                    dice.remove(bottom)
                    dice.remove(top)
                    num_sum += max(dice)
                    break
                else:
                    bottom = dice[k]
                    top = dice[k + 1]
                    dice.remove(bottom)
                    dice.remove(top)
                    num_sum += max(dice)
                    break

    if result < num_sum:
        result = num_sum

print(result)

