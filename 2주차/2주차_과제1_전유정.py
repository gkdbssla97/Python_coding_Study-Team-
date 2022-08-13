import sys 

cnt = int(sys.stdin.readline()) #입력하는 개수
stack = []


for i in range(cnt):
    num = int(sys.stdin.readline())

    if num == 0: 
        if len(stack) == 0: #빈 리스트에서 처음 입력받은 숫자가 0이라면 예외처리 
            try: 
                continue #오류 발생시 반복문으로 돌아가 실행 
            except: IndexError
        else:
             stack.pop() 

    else: 
        stack.append(num)

print(sum(stack))
