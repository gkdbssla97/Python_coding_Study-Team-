
k = int(input())

money = []
for i in range(k):
    a = int(input())
    if a == 0:
        money.pop()
    else:
        money.append(a)

print(sum(money))

        
