pick = []

for i in range(9):
    pick.append(int(input()))
max_val = max(pick)
print(max_val)
print(pick.index(max_val) + 1)
