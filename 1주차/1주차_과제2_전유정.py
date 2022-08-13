list = []
for i in range(9):
  S = int(input())
  list.append(S)
max = 0 
for i in range(9):
  if list[i] > max:
    max = list[i]
    r= i+1
print(max)
print(r)
