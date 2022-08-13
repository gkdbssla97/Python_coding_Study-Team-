import heapq
import sys

heap = []

insert = int(sys.stdin.readline())

for i in range(insert):
    num = int(sys.stdin.readline())
    if num == 0 :
        if len(heap) == 0:
           print("0")
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, num)
