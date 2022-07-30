S = input()
list = []

for i in range(len(S)):
    list.append(S[i:])
  
list = sorted(list)

print("\n".join(list))
