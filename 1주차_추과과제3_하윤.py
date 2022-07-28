block = []

block = [list(map(int, input().split())) for _ in range(7)]

#print(block)
cnt = 0
for i in range(7):
    for j in range(3):
        if block[i][j:j+5] == block[i][j:j+5][::-1]:
            #print(block[i][j:j+5][::-1])
            cnt += 1

for i in range(7):
    for j in range(3):
        tmp = []
        for k in range(5):
            tmp.append(block[k+j][i])
        if tmp == tmp[::-1]:
            #print(tmp)
            cnt += 1

print(cnt)