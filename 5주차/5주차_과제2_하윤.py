N = int(input())
card = list(map(int, input().split()))
card.sort()
length = len(card)

M = int(input())
pick = list(map(int, input().split()))

def binarySearch(card, target, lt, rt):
    while lt <= rt:
        mid = (lt + rt) // 2
        if card[mid] == target:
            return 1
        elif card[mid] > target:
            rt = mid - 1
        else:
            lt = mid + 1
    return 0

for i in range(M):
    print(binarySearch(card, pick[i], 0, length - 1))