import sys

K, N = map(int, sys.stdin.readline().split())
L = []

for _ in range(K):
    L.append(int(sys.stdin.readline()))

start = 1
end = max(L)

while start <= end:
    result = 0
    mid = (start + end) // 2

    for l in L:
        result += l // mid

    if result >= N:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)