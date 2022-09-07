def BFS():
    def deQ():
        global front
        front = (front + 1)%(N*N)
        return Q[front]

    def enQ(item):
        global rear
        rear = (rear + 1)%(N*N)
        Q[rear] = item

    global ans
    dr = [1,-1,0,0]
    dc = [0,0,-1,1]
    for i in range(N):
        for j in range(N):
            if table[i][j] == 1:
                cnt = 1
                table[i][j] = 0
                enQ((i,j))
                ans += 1
                while front != rear:
                    r, c = deQ()
                    for d in range(4):
                        tr = r + dr[d]
                        tc = c + dc[d]
                        if 0<= tr < N and 0<= tc< N:
                            if table[tr][tc] == 1 :
                                table[tr][tc] = 0
                                enQ((tr,tc))
                                cnt += 1

                danji.append(cnt)




N = int(input())

table = [list(map(int,input())) for _ in range(N)]

ans = 0
danji = []
Q = [0] * N * N
front = rear = 0

BFS()

danji.sort()
print(ans)
for i in range(ans):
    print(danji[i])