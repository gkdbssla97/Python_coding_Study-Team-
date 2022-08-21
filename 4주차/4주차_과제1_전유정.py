from collections import deque 

# 차레대로 정점 개수, 간선 개수, 탐색 시작점 
N, M, start = list(map(int, input().split()))

matrix = [[0]*(N+1) for i in range(N+1)]

#방문한 곳에 체크 기록할 리스트 
visited_dfs = [0]*(N+1)
visited_bfs = [0]*(N+1)

#입력받는 값에 대해 1삽입해서, 인접리스트 생성
for i in range(M):
    a,b = map(int,input().split())
    matrix[a][b] = 1 
    matrix[b][a] = 1 

def dfs(V): 
    visited_dfs[V] = 1 
    print(V, end = ' ')
    # 재귀
    for i in range(1,start+1): 
        if(visited_dfs[i] == 0 and matrix[start][i] == 1):
            dfs(i)

def bfs(start): 
    #방문해야 할 곳을 순서대로 넣을 큐 
    queue = deque([start]) 
    visited_bfs[start] = 1 

    #큐 안에 데이터 없을 때까지 
    while queue: 
        V = queue.popleft()
        print(V, end= ' ')
        for i in range(1,N+1):
            if(visited_bfs[i] == 0 and matrix[start][i] == 1):
                queue.append(i)
                visited_bfs[i] = 1 
dfs(start)
print()
bfs(start)
