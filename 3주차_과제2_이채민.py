import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    visit = list(map(int, input().split()))
    
    # 충전소가 아님 (pop)
    if (len(visit)==1):                   
        if len(heap) == 0:
            print(-1)
            continue
        print(heapq.heappop(heap)[1])
        
    # 선물 충전소 (push)
    else:
        for i in range(1, len(visit)):
            # 최대 힙 구현을 위해 원소를 튜플 형태로 저장
            heapq.heappush(heap, (-visit[i], visit[i]))     