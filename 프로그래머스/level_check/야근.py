from heapq import heappop, heappush

def solution(n, works):
    if sum(works) <= n:
        return 0

    hq = []
    for work in works:
        heappush(hq, -work)

    while n:
        heappush(hq, (heappop(hq) + 1))
        n -= 1

    return sum([k ** 2 for k in hq])