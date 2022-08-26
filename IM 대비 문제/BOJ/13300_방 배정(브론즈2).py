student, room = map(int,input().split())

class_list = [[] for _ in range(6)] # (x,y) index + 1 = 반, x, 남자, y: 여자
for s in range(student): # 성별, 반 순으로 input 값 제공
    y, i = map(int,input().split())
    class_list[i-1].append(y)

result = 0
for c in class_list:
    for i in range(2):
        if c.count(i):
            if c.count(i)%room:
                result += c.count(i)//room + 1
            else:
                result += c.count(i)//room
print(result)