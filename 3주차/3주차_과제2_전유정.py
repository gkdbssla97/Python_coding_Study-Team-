import heapq, sys 

N = int(sys.stdin.readline())
present = []

for i in range(N): 
    x_list = list(map(int,sys.stdin.readline().split()))
    x = x_list[0]
    
    if x == 0: 
        if len(present) == 0: 
            print(-1)
        else: 
            print(heapq.heappop(present)[1])
   
    else:
         for j in range(1, x+1): 
             heapq.heappush(present, (-x_list[j], x_list[j]))