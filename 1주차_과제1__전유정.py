S = input()
array = []

for i in range(len(S)):
    array.append(S[i:])
  
array = sorted(array)

print("\n".join(array))
