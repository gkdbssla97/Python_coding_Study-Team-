N = int(input())

for i in range(N):
    S = input().upper()
    if S == S[::-1]:
        result = "YES"
    else:
        result = "NO"
    print(f'#{i+1} {result}')