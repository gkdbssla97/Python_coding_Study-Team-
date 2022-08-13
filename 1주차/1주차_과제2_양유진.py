numbers = []

for i in range(9):
    number = input()
    numbers.append(int(number))

maxnum = max(numbers)
print(maxnum)
print(numbers.index(maxnum) + 1)
