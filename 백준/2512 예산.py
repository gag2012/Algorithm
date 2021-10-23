countLocal = int(input())
local = list(map(int, input().split()))
budget = int(input())
left, right = 0, max(local)

while left <= right:
    mid = (left+right) // 2
    total = 0
    for i in local:
        if i > mid:
            total += mid
        else:
            total += i
    if total <= budget:
        left = mid + 1
    else:
        right = mid - 1
print(right)