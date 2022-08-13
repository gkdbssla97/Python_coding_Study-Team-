from collections import deque

N = int(input())
pick = deque([i for i in range(1, N + 1)]) #List Comprehension
#print(len(pick))
while len(pick) != 1:
    pick.popleft()
    pick.append(pick.popleft())
print(pick[0])
