import sys 
import heapq
input = sys.stdin.readline


V,E = map(int,input().split()) #노드 개수, 간선 개수 입력 
#시작점 strat
start = int(input())

#연결된 노드가 있으면, 그 노드와 가는 데 드는 비용을 지정한 리스트 
graph = [[] for _ in range(V+1)]

INF = float('inf')

for _ in range(E): #간선 정보를 입력받기 
    u,v,e = map(int, input().split())
    graph[u].append((v,e)) #u에서 v로 갈 때 비용 w 

#초기값 셋팅하기 
distance = [INF]*(V+1) #stat에서 각각 노드로 갈 때 최단 비용을 저장한 리스트 
distance[start] = 0 #시작노드 거리 초기화 

visited = [False] * (V+1)
heap = []
heapq.heappush(heap,(0,start)) # K번 노드로부터 탐색을 시작하므로, 거리가 0인 상태로 시작한다

while heap:
    min_dis, cur_node = heapq.heappop(heap)
    
    # 현재 경로를 탐색할 노드가 이미 방문한 적이 있는 노드라면 스킵한다.
    if visited[cur_node]:
        continue
    # 방문 한 적이 없는 노드라면, 방문 처리를 해준다.
    visited[cur_node] = True

    # 현재 노드와 연결된 모든 노드와 거리를 대상으로 이하의 검사를 시행한다.
    for node,dis in graph[cur_node]:
        # new_d 는 현재 노드까지 오기 까지의 거리 min_dis와 현재 노드에서 node까지의 거리인 dis의 합이다.
        new_d = min_dis+dis

        # 만약에 이렇게 계산한 거리가  저장되어있었던 거리보다 작다면, 값을 바꿔준 다음, heap에 새로운 값을 투입해준다.
        if new_d < distance[node]:
            distance[node] = new_d
            heapq.heappush(heap,(new_d,node))

# 문제의 출력 형식에 맞추어 출력
for idx in range(1,len(distance)):
    if distance[idx] == INF:
        print('INF')
    else:
        print(distance[idx])
 