import sys

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == target:
            return True
        elif A[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort()

M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    if binary_search(A, B[i], 0, N-1):
        print(1)
    else:
        print(0)

