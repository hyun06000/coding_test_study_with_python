### 백준
### 1655번
### 가운데를 말해요

### 풀이 참고
# https://yabmoons.tistory.com/478

# 1. 최대 힙의 크기는 항상 최소힙의 크기보다 같거나 1만큼 크다.
# 2. 최소 힙의 모든 원소는 최대힙의 모든 원소보다 항상 크거나 같아야 한다.


import sys
from heapq import heappop, heappush

def readline():
    return int(sys.stdin.readline().strip())

N = readline()
median = []
max_pq, min_pq = [], []
for i in range(N):
    n = readline()
    
    if len(max_pq) == len(min_pq):
        heappush(max_pq, -n)
    else:
        heappush(min_pq, n)
    
    if max_pq and min_pq :
        max_pop = -heappop(max_pq)
        min_pop = heappop(min_pq)
        if max_pop > min_pop:
            heappush(max_pq, -min_pop)
            heappush(min_pq, max_pop)
        else:
            heappush(max_pq, -max_pop)
            heappush(min_pq, min_pop)

    max_pop = -heappop(max_pq)
    median.append(max_pop)
    heappush(max_pq, -max_pop)

for m in median:
    print(m)
