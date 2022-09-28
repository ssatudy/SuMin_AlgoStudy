def DFS(r,c,now,level):
    global ans
    if level == 0:
        ans += 1
    elif now + level <= 4:
        return
    if arr[r][c] == 'S':
        now += 1
    for d in range(2):
        tr = r + dr[d]
        tc = c + dc[d]
        if 0<= tr < 5 and 0<= tc < 5 and visited[tr][tc]:
            DFS(tr,tc,now,level-1)
            visited[tr][tc] = True



dr = [1,0]
dc = [0,1]
visited = [[True] * 5 for _ in range(5)]
arr = [list(input()) for _ in range(5)]
ans = 0
for i in range(5):
    for j in range(5):
        visited[i][j] = False
        DFS(i,j,0,7)

print(ans)