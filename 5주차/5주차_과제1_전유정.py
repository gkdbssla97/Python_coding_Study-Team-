import sys 

input = sys.stdin.readline
n = int(input())
card = list(map(int,input().split()))
m= int(input())
check = list(map(int,input().split()))

card.sort()

def binary_search(array, target, left, right):
    while left <= right: 
        mid = (left + right) //2
        
        if array[mid] == target: 
            return mid 
        elif array[mid] > target:
            right = mid -1 
        else:
            left  = mid + 1
    return None 

for i in range(m):
    if binary_search(card, check[i], 0, n-1)is not None: 
        print(1, end=" ")
    else: 
        print(0, end= " ")


