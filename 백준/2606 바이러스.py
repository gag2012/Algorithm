from sys import stdin
read = stdin.readline
dic = {}
visited = []

for i in range(int(read())):
    dic[i+1] = set()

for j in range(int(read())):
    a, b = map(int,read().split())
    # 양쪽에 그래프 값을 넣어줌
    dic[a].add(b)
    dic[b].add(a)

def dfs(start, dic):
    for i in dic[start]:
        print(i)
        if i not in visited:
            visited.append(i)
            print(visited)
            dfs(i, dic)

dfs(1, dic)

print(dic)
print(len(visited)-1)



