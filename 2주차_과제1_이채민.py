import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    num = int(input())
    if num:
        stack.append(num)
    else:
        stack.pop()
print(sum(stack))