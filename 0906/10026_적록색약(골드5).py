def deQ():
    global front
    front = (front + 1) % (N * N)
    return Q[front]


def enQ(item):
    global rear
    rear = (rear + 1) % (N * N)
    Q[rear] = item


def isEmpty():
    return rear == front

def abnormal(r,c,now):
    visited[i][j] = 1
    dr = [-1,1,0,0]
    dc = [0,0,1,-1]
    enQ((r,c))
    while not isEmpty():
        r, c = deQ()
        for d in range(4):
            cr = r + dr[d]
            cc = c + dc[d]
            if 0<= cr <N and 0<= cc <N and visited[cr][cc] == 0:
                if now == 'R' or now == 'G':
                    if table[cr][cc] == 'R' or table[cr][cc] =='G':
                        visited[cr][cc] = 1
                        enQ((cr,cc))
                elif now == table[cr][cc]:
                    visited[cr][cc] = 1
                    enQ((cr,cc))


def normal(r,c,now):
    visited2[i][j] = 1
    dr = [-1,1,0,0]
    dc = [0,0,1,-1]
    enQ((r,c))
    while not isEmpty():
        r, c = deQ()
        for d in range(4):
            cr = r + dr[d]
            cc = c + dc[d]
            if 0<= cr <N and 0<= cc <N and visited2[cr][cc] == 0 and table[cr][cc]==now:
                visited2[cr][cc] = 1
                enQ((cr, cc))




N = int(input())
before = 'W'
table = [list(input()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
visited2 = [[0]*N for _ in range(N)]
Q = [0]*N*N; front = rear = 0
ans1 = ans2 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            abnormal(i, j, table[i][j])
            ans2 += 1

        if visited2[i][j] == 0:
            normal(i, j, table[i][j])
            ans1 += 1

print(ans1,ans2)

