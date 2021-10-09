# x, y = map(int, input().split())
#
# z = round(y*100/x)
# result = 0
# while True:
#     y += 1
#     x += 1
#     result += 1
#
#     z_t = y*100//x
#     if z_t != z :
#         break
#     if z_t >= 99 :
#         result = -1
#         break
#
# print(result)

import sys

input = sys.stdin.readline

x, y = map(int, input().split())
z = (y * 100) // x
if z >= 99:
    print(-1)
else:
    answer = 0
    left = 1
    right = x

    while left <= right:
        mid = (left + right) // 2
        if (y + mid) * 100 // (x + mid) <= z:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1

    print(answer)