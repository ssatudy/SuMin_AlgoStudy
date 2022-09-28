N, M = map(int,input().split())

word = list(input().split())
word.sort()

v = ['a', 'e', 'i', 'o', 'u']

def dfs(start=0,now=0,flag1=0,flag2=0,ans=""):
    if now==N:
        if flag1 and flag2 > 1:
            print(ans)
        return

    for i in range(start,M):
        if word[i] in v:
            dfs(i + 1, now + 1, 1,flag2, ans + word[i])
        else:
            dfs(i+1,now+1,flag1,flag2+1,ans+word[i])
dfs()
