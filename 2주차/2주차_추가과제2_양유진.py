count = []

for i in range (10):
    num = int(input())
    count.append(num % 42)

print(len(set(count)))
