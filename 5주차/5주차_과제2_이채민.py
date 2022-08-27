import sys
input = sys.stdin.readline

def binary_search(lst, target):
    left = 0; right = len(lst) - 1

    while left <= right:
        mid = (left+right) // 2
        if lst[mid] == target:
            return 1 
        elif lst[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return 0

N = int(input())
numbers = list(map(int, input().split()))

numbers.sort()
M = int(input())
for i in list(map(int, input().split())):
    print(binary_search(numbers, i))