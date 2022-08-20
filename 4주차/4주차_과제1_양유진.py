from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i ,visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


N, M, V = map(int, input().split())


dfs_visited = [False] * (N+1)
bfs_visited = [False] * (N+1)

graph = [[] for _ in range(N+1)]

for _ in range(M):
     a, b = map(int, input().split())
     graph[a].append(b)
     graph[b].append(a)
     graph[a].sort()
     graph[b].sort()

dfs(graph, V, dfs_visited)
print("")
bfs(graph, V, bfs_visited)

