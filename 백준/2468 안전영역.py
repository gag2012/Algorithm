import sys
import copy
read = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y, n, k, maps_tmp):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    maps_tmp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and maps_tmp[nx][ny] > k:
            dfs(nx, ny, n, k, maps_tmp)

maps = []
n = int(input())
for _ in range(n):
    maps.append(list(map(int, read().split())))

result = 0
for k in range(n):
    maps2 = copy.deepcopy(maps)
    map_count = 0
    for i in range(n):
        for j in range(n):
            if maps2[i][j] > k:
                dfs(i, j, n, k, maps2)
                map_count+=1
    if map_count > result:
        result = map_count
print(result)