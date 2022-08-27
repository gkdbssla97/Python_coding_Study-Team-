K, N = map(int, input().split())

def binarySearch(LAN, target, lt, rt):
    while lt <= rt:
        sum = 0
        mid = (lt + rt) // 2
        for x in LAN:
            sum += (x // mid)
        if sum >= target:
            lt = mid + 1
            result = mid
        elif sum < target:
            rt = mid - 1
        #print(1)
    return result



LAN = []
for _ in range(K):
    LAN.append(int(input()))
if K == N == 1:
    print(LAN[0])
    exit(0)

global result
max_val = max(LAN)
print(binarySearch(LAN, N, 1, max_val))
