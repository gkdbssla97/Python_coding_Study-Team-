S = input()
array = []

for i in range(len(S)):
    array.append(S[i:])

array.sort()

for i in range(len(S)):
    print(array[i])