import sys
read = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y):
    dx = [0, 0, 1, -1, -1, 1, 1, -1]
    dy = [1, -1, 0, 0, 1, 1, -1, -1]

    maps[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and maps[nx][ny]==1:
            dfs(nx, ny)

while True:
    input_ = list(map(int, read().split()))

    w = input_[0]
    h = input_[1]
    maps = []
    map_count = 0
    if w==0 and h==0:
        break

    for _ in range(h):
        maps.append(list(map(int, read().split())))
        print(maps)
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                dfs(i, j)
                map_count+=1
    print(map_count)