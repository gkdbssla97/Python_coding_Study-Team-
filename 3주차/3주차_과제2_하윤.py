import heapq
import sys
N = int(sys.stdin.readline())

heap = []
for i in range(N):
    x = list(map(int, sys.stdin.readline().split()))
    if x[0] == 0:
        if len(heap) == 0:
            print(-1)
        else:
            print(heapq.heappop(heap)[1])
    else:
        for i in range(x[0]):
            heapq.heappush(heap, (-x[i+1], x[i+1]))


