#step 1 사탕맵 만들기
n = int(input())
maps = [list(input()) for i in range(n)]
now_x = 0
now_y = 0
cnt = 0
result_max = 0

#step 2 가로세로 하나씩 번갈아가며 살펴보기
def checkCandyCol():
    global cnt, result_max

    result_max = 1
    for j in range(0, n):
        cnt = 1
        for i in range(1, n):
            if maps[i][j] == maps[i-1][j] :
                cnt += 1
                result_max = max(result_max, cnt)
            else :
                cnt = 1
    return result_max

def checkCandyRow():
    global cnt, result_max

    result_max = 1
    for i in range(0, n):
        cnt = 1
        for j in range(1, n):
            if maps[i][j] == maps[i][j-1] :
                cnt += 1
                result_max = max(result_max, cnt)
            else :
                cnt = 1
    return result_max


answer = 0
answer_tmp = 0
for i in range(0, n):
    for j in range(0, n-1):
        if (maps[i][j] != maps[i][j+1]):
            maps[i][j], maps[i][j+1] = maps[i][j+1], maps[i][j]
            answer_tmp = checkCandyCol()
            if answer_tmp > answer :
                answer = answer_tmp
            answer_tmp = checkCandyRow()
            if answer_tmp > answer :
                answer = answer_tmp
            maps[i][j], maps[i][j+1] = maps[i][j+1], maps[i][j]


for i in range(0, n-1):
    for j in range(0, n):
        if (maps[i][j] != maps[i+1][j]):
            maps[i][j], maps[i+1][j] = maps[i+1][j], maps[i][j]
            answer_tmp = checkCandyCol()
            if answer_tmp > answer:
                answer = answer_tmp
            answer_tmp = checkCandyRow()
            if answer_tmp > answer:
                answer = answer_tmp
            maps[i][j], maps[i+1][j] = maps[i+1][j], maps[i][j]

print(answer)