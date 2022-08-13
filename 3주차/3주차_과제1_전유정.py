import heapq, sys

N = int(sys.stdin.readline())

H = [] 

for i in range(N):
    x = int(sys.stdin.readline())

    if x != 0: 
        heapq.heappush(H,x)
    else: 
        if len(H)!=0:
            print(heapq.heappop(H))
        else:
            print(0)