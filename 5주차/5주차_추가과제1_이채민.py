import sys
N, K = map(int, input().split())
lan = list(map(int, sys.stdin.readlines()))
maximum = 0
low = 1; high = sum(lan)//K; mid = (low+high)//2
while low<=high:
    bundle = 0; 
    for l in lan:
        bundle+=(l//mid)
    if bundle < K:
        high = mid-1
    else:
        maximum = mid if mid>maximum else maximum
        low = mid+1
    mid = (low+high)//2
print(maximum)