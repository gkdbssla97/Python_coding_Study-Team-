N, K = map(int, input().split())

card = list(map(int, input().split()))
#중복제거
result = set()

#print(card)
for i in range(len(card)):
    for j in range(i+1, len(card)):
        for k in range(j+1, len(card)):
            val = card[i] + card[j] + card[k]
            result.add(val)
result = list(result)
result.sort(reverse = True)
#print(result)
print(result[K-1])

'''
10 3
13 15 34 23 45 65 33 11 26 42
'''