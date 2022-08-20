import sys
from collections import deque

#bfs 탐색
def bfs(x):
    queue = deque([x])
    count = 0

    #자기 자신부터 방문한다.
    visited[x] = 1 

    while queue: 
        friend = queue.popleft()
        count += 1 

        #친구의 친구를 확인 
        for j in graph[friend]:
            #방문하지 않았다면 방문 
            if not visited[j]:
                #방문 순서를 카운트 
                visited[j] = visited[friend] +1 
                queue.append(j)

    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())

    #노드 방문 여부와 순서 확인 
    visited = [0 for i in range(n+1)]

    #각 연결된 노드를 표현 
    graph = [[] for _ in range(n+1)]
    for _ in range(m): 
        a,b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    bfs(1)

    print(visted.count(2) + visited.count(3))