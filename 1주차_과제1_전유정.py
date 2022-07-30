import sys

S = input(map(str,sys.stdin.readline().strip()))
array = []

for i in range(len(S)):
    array.append(S[i:])
  
array = sorted(array)

print("\n".join(array))