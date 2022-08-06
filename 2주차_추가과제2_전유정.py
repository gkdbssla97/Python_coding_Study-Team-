import sys

num = []

for i in range (10):
    A = int(sys.stdin.readline())
    B = A%42
    num.append(B)

sum = set(n)
print(len(sum))

