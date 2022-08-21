import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []



######### 1) heappush #########
nums = list(map(int, input().split()))

# N개의 숫자만 갖는 heap 생성
for i in range(N):
    heapq.heappush(heap, nums[i]) 
    
# 이후에는 heappushpop을 이용하여 heap의 원소를 N개 유지
for _ in range(N-1):
    nums = list(map(int, input().split()))
    for i in range(N):
        heapq.heappushpop(heap, nums[i])

# heappushpop
# [12 7 9 15 5] => [5, 7, 9, 12, 15]
# 13 삽입시,
# [7, 9, 12, 13, 15]
print(heap[0], flush=False)




######### 2) nlargest (메모리 초과) #########

for _ in range(N):
    nums = list(map(int, input().split()))
    for i in range(N):
        heapq.heappush(heap, nums[i])

print(min(heapq.nlargest(N, heap)), flush=False)

"""
메모리 초과 이유
length
    nums: 1,500 
    heap: 1,500 * 1,500 = 2,250,000
size
    int: 4byte, 
total
    nums: 1,500 * 4(byte) = 6000(byte) ≒ 5.86(KB) ≒ 0.006
    heap: 2,250,000 * 4(byte) = 9,000,000(byte) ≒ 8790(KB) ≒ 8.6(MB)

8.6 + alpha(module, IObuffer, ...) > 12

"""