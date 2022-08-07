from collections import deque

S = input()
S = deque(S)

array = []
array.append(list(S))

while len(S) != 1:
    S.popleft()
    tmp = list(S)
    array.append(tmp)

for i in sorted(array):
    print(''.join(i))
    
# '''
# baekjoon
# '''
