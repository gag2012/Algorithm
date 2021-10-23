result = 0
count = 0
width = []
m, n, k = map(int, input().split())
s = [[0] * n for i in range(m)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x,y):
    global count

    if x < 0 or x >= m or y < 0 or y >= n:
        return

    if s[x][y] == 1:
        return

    count += 1
    s[x][y] = 1 # 탐색한 곳은 1로 갱신

    # 동서남북 탐색
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x,y+1)

for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            s[j][k] = 1

for i in range(m):
    for j in range(n):
        count = 0
        if s[i][j] == 0:
            dfs(i,j)
            result += 1
            width.append(count)

width.sort()

print(result)
print(width)