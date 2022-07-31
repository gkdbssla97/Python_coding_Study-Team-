from collections import deque

N = int(input())
queue = deque([ x for x in range(1, N+1)])
    
while(len(queue)!=1):
    queue.popleft()
    queue.rotate(-1)
    
print(queue[0])
