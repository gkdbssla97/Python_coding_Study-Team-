import sys
from collections import deque

input = sys.stdin.readline

def DFS(graph, visited, start):
    visited[start] = 1
    print(start, end=" ")
    for node in graph[start]:
        if not visited[node]:
            DFS(graph, visited, node)
            
def BFS(graph, visited, start):
    queue = deque([start])
    visited[start] = 1
    while(queue):
        i = queue.popleft()
        print(i, end=" ")
        for node in graph[i]:
            if not visited[node]:
                queue.append(node)
                visited[node] = 1

    
# main
N, E, start = list(map(int, input().split()))

node = [x for x in range(1, N+1)]   # 노드 정보
graph = [[] for _ in range(N+1)]    # 연결 정보
visited = [0] * (N+1)               # 방문 정보

for _ in range(E):
    src, dest = list(map(int, input().split()))
    # 양방향 -> 무방향 그래프이므로 양쪽 모두에 기록
    graph[src].append(dest)
    graph[dest].append(src)

# 작은 노드부터 방문해야하므로 오름차순 정렬
for i in graph:
    i.sort()

DFS(graph, visited, start)
print()
visited = [0] * (N+1)            # 하단 설명 글 참고
BFS(graph, visited, start)


# DFS와 BFS 외부에 존재하는 visited 변수를 초기화해주는 이유

# 함수 외부에 존재하지만, 리스트나 딕셔너리와 같이 mutable로 분류되는 객체를 함수의 파라미터로 받은 경우, 
# 함수 내부에서 해당 mutable 객체의 원소만 변경 시 변경 사항이 본래의 자료구조에 영향을 끼친다. 
# why? 해당 자료구조가 저장된 주소는 바뀌지 않고, 내부 원소가 저장되는 주소값만 바뀌었기 때문.

# 하지만 원소 변경이 아닌, 리스트 혹은 딕셔너리를 새로이 할당하는 경우에는 기존의 자료구조에 영향을 끼치지 않는다.
# 파이썬에서는 별도의 변수 취급.



# 예제 1) 변경사항이 반영 안됨. 리스트 통째로 새로이 할당했기 때문에 main과 구분된 별도의 변수(id가 됨.
def a(d):
    print(id(d))
    d = [1, 2, 3]
    print(id(d))
    
d = []
print(id(d))
a(d)
print(d)

# >>> 139801621263680        => main에 존재하는 d의 id값
# >>> 139801621263680        => 함수 a에서 d의 값을 변경하기 전 d의 id값
# >>> 139801620389632        => 함수 a에서 d의 값을 변경한 후 d의 id값
# >>> []                     => main에 존재하는 d (함수로 인한 값 변경 無)


# 예제 2) 변경사항이 반영됨. append를 통해 "원소"만을 추가했기 때문.
def a(d):
    print(id(d))
    d.append(1)
    print(id(d))

d = []
print(id(d))
a(d)
print(d)

# >>> 140466058274112         => main에 존재하는 d의 id값
# >>> 140466058274112         => 함수 a에서 d의 값을 변경하기 전 d의 id값
# >>> 140466058274112         => 함수 a에서 d의 값을 변경한 후 d의 id값
# >>> [1]                     => main에 존재하는 d (함수로 인한 값 변경 有)