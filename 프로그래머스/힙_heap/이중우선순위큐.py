from heapq import heappush


def solution(operations):
    pq = []
    for ops in operations:
        if ops.startswith("I"):
            heappush(pq, int(ops[2:]))
        elif pq and ops == "D 1":
            pq.pop()
        elif pq and ops == "D -1":
            pq.pop(0)

    if not pq:
        return [0, 0]
    else:
        return [max(pq), pq[0]]