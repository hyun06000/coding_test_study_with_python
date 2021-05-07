import heapq


def solution(scoville, K):
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)

    i = 0
    while len(heap) > 1 and heap[0] < K:
        new_food = heapq.heappop(heap) + heapq.heappop(heap) * 2
        heapq.heappush(heap, new_food)
        i += 1

    if len(heap) == 1 and heap[-1] < K:
        return -1
    else:
        return i