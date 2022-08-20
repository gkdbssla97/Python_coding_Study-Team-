from collections import deque

M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

queue = deque([])

# 이동할 4방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

 # 입력 받은 위치중 1의 자리를 큐에 넣기!
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            queue.append([i, j])

def bfs():
    #큐가 빌때까지 반복
    while queue:
        x, y = queue.popleft()
        #현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0:
                # 토마토를 익히면서 1을 더해주기
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])

bfs()
for i in matrix:
    for j in i:
        if j == 0: # 0이 존재할때
            print(-1)
            exit(0)
    result = max(res, max(i))
print(result - 1) # 처음 1이 포함되어있어서 빼주어야 한다. 
