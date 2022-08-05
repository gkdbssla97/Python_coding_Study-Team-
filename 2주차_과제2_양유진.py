from collections import deque

count = int(input())
card_stack = deque()

for i in range (count):
    card_stack.append(count - i)

while(len(card_stack) > 1):
    card_stack.pop()
    card_stack.appendleft(card_stack.pop())

print(card_stack.pop())
