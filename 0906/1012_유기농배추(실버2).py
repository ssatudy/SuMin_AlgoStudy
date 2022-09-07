def enQ(item):
    global rear
    rear = (rear+1)%(N*M)
    Q[rear] = item

def deQ():
    global front
    front = (front+1)%(N*M)
    return Q[front]

def BFS(r,c):
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    table[r][c] = 0
    enQ((r,c))
    while rear != front:
        r,c = deQ()
        for d in range(4):
            cr = r + dr[d]
            cc = c + dc[d]
            if 0<= cr<N and 0<=cc<M and table[cr][cc] == 1:
                table[cr][cc] = 0
                enQ((cr,cc))


for tc in range(1,int(input())+1):
    M, N, bugs = map(int,input().split())
    table = [[0]*M for _ in range(N)]

    Q = [0]*(N*M); front = rear = 0

    for bug in range(bugs):
        c, r = map(int,input().split())
        table[r][c] = 1

    ans = 0
    for r in range(N):
        for c in range(M):
            if table[r][c] == 1:
                BFS(r,c)
                ans += 1

    print(ans)

