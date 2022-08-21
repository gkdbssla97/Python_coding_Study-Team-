import sys
from collections import deque

input = sys.stdin.readline
cols, rows = 0, 0

def BFS(field, visited, start):
    day = -1;    queue = deque([])
    for row, col in start: 
        visited[row][col] = True
        queue.append((row, col))

    # 이동 방향
    dr, dc = [0,1,0,-1], [1,0,-1,0]
    # 하루 = 사방면에 있는 토마토를 queue에 담는 작업 수행
    while(queue):
        day+=1; temp = []
        # 기존에 담겨 있던 토마토를 기준으로 사방면에 있는 토마토를 temp에 임시로 넣어둠.
        while(queue):
            row, col = queue.popleft() 
            for i in range(4):
                nextR = row+dr[i]
                nextC = col+dc[i]
                if nextR>=0 and nextR<rows and nextC>=0 and nextC<cols and visited[nextR][nextC]:
                    visited[nextR][nextC] = True
                    if field[nextR][nextC] != -1:
                        temp.append((nextR, nextC))
        # 여기서 큐가 비가 되면, 하루가 마무리된것. 
        # 마무리 후 temp를 queue에 삽입 => 그래야 다음 루프문에서 그 다음 익을 토마토 선별 가능
        queue = deque(temp)
    
    # 모든 토마토가 익었는지 확인
    for i in range(rows):
        for j in range(cols):
            if visited[i][j]==False:
                print(-1)
                return 
    print(day)
                    
        

cols, rows = list(map(int, input().split()))

field = []
visited = [[False for _ in range(cols)] for _ in range(rows)]   # [[False for _ in range(cols)]] * rows 로 선언시 얕은 복사라서 사용 불가. 
start = []

for row in range(rows):
    temp = list(map(int, input().split()))
    for col in range(cols):
        if temp[col] == 1:
            start.append((row, col))    # 시작 지점을 튜플 형식(row, col)으로 저장
        if temp[col] == -1:             # 토마토가 들어있지 않은 곳은 미리 visited 값을 True로
            visited[row][col] = True
    field.append(temp)
    
BFS(field, visited, start)