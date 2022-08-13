import heapq
import sys

insert = int(sys.stdin.readline())
heap = []

for i in range(insert):
    a = list(map(int, sys.stdin.readline().split()))
    if len(a) == 1:
        if(len(heap) == 0):
            print("-1")
        else:
            print(heapq.heappop(heap)[1])
    else:
        for j in range(a[0]):
            heapq.heappush(heap, (-a[j+1], a[j+1]))
