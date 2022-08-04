K = int(input())

pick = []
for i in range(K):

    pick.append((int(input())))
    #print(pick[-1])
    if pick[-1] == 0:
        pick.pop()
        pick.pop()
print(sum(pick))

