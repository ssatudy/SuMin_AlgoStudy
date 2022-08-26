for tc in range(4):
    x_list = [0]*50001
    y_list = [0]*50001

    x1,y1,x2,y2,xx1,yy1,xx2,yy2 = map(int,input().split())
    for x in range(x1,x2+1):
        x_list[x] += 1
    for y in range(y1,y2+1):
        y_list[y] += 1

    for x in range(xx1,xx2+1):
        x_list[x] += 1
    for y in range(yy1,yy2+1):
        y_list[y] += 1

    a = x_list.count(2)
    b = y_list.count(2)
    if a > 1 and b > 1:
        print('a')
    elif (a > 1 and b ==1) or (a== 1 and b > 1):
        print('b')
    elif a == 1 and b == 1:
        print('c')
    else:
        print('d')