import sys

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if I[mid] == target:
            return True
        elif I[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

N = int(sys.stdin.readline()) # 숫자 카드의 개수
I = list(map(int, sys.stdin.readline().split())) # 숫자 카드에 적혀있는 정수
M = int(sys.stdin.readline()) 
C = list(map(int, sys.stdin.readline().split())) # 판단 해야할 카드들

I.sort()

start = 0
end = len(I) -1

for i in range(M):
    if binary_search(I, C[i], start, end):
        print(1, end=" ")
    else:
        print(0, end=" ")





