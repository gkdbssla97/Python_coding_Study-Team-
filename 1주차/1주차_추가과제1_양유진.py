num = int(input())
words = []

for i in range(num):
    words.append(input().lower())

for i in range(num):
    if str(words[i]) == str(words[i])[::-1]:
        print(f"#{i+1} YES")
    else:
        print(f"#{i+1} NO")

