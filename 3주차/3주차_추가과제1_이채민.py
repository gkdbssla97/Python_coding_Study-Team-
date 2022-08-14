import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    num = int(input())
    if(num!=0):
        heapq.heappush(heap, (-num, num))
    else:
        if not len(heap):
            print(0)
            continue
        print(heapq.heappop(heap)[1])
