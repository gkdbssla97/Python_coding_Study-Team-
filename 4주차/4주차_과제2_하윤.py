from collections import deque  # 큐 구현을 위해 deque 라이브러리 사용

# BFS 함수 정의
def bfs():
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append([nx, ny])

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0] #북, 동, 남, 서
dy = [0, 1, 0, -1]
result = 0

queue = deque([])

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append([i, j])
bfs()
#print(tomato)

for i in tomato:
    for j in i:
        #print(i, j)
        if j == 0:
            print(-1)
            exit(0) #강제종료
    result = max(result, max(i))

#토마토가 처음에 1일로 시작하므로
print(result - 1)
#모든 토마토가 저장될 때부터 다 익어있으면
# 1 1 1
# 1 1 1
# 1 1 1
# result = 1이므로 (result - 1) = 0으로 출력할 수 있다.