import heapq
import sys
N = int(sys.stdin.readline())

heap = []
for i in range(N):
    x = list(map(int, sys.stdin.readline().split()))

    if not heap:
        for i in x:
            heapq.heappush(heap, i)
    else:
        for i in x:
            if heap[0] < i:
                #print(heap[0], i)
                heapq.heappush(heap, i)
                heapq.heappop(heap)
#print(heap)
print(heap[0])



