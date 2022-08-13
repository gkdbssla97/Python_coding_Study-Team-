import sys 
from collections import deque

num = int(sys.stdin.readline())
queue = deque()

for i in range(num):
    queue.append(i+1)

while len(queue)>1:
    queue.popleft()
    queue.rotate(-1)

print(queue.pop())


