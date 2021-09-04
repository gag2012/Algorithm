N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
B = list(map(int, input().split()))

for num in B:
    left, right = 0, len(A) - 1
    is_find = False
    while True:
        median = (left + right) // 2
        if num == A[median]:
            print(1)
            is_find = True
            break
        elif num > A[median]:
            left = median + 1
        elif num < A[median]:
            right = median - 1

        if left > right:
            break

    if not is_find: print(0)



