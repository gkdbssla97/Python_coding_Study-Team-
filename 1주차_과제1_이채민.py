import sys
input = sys.stdin.readline

numbers = []
for i in range(9):
    num = int(input())
    numbers.append(num)


# 1. 내장 함수 sorted 사용시
'''
sorted_numbers = sorted(numbers, reverse=True)
max_num = sorted_numbers[0]
print(max_num)
print(numbers.index(max_num)+1)
'''

# 2. 리스트 함수 sort 사용시
'''
list는 mutable한 객체로서, = 연산자를 통해 바로 대입하면
두 변수의 주소값이 같아져버림. 즉 numbers 원소 변경시 origin_numbers도 변경됨.
여기서 numbers는 1차원 list이므로 슬라이싱만으로 깊은 복사 가능
'''
origin_numbers = numbers[:] 
numbers.sort(reverse=True)
max_num = numbers[0]
print(max_num)
print(origin_numbers.index(max_num)+1)

