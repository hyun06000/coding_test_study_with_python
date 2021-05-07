import sys
import heapq
from collections import defaultdict


def solution(n, costs):
    graph = defaultdict(list)
    for f, t, c in costs:
        graph[f].append([t, c])
        graph[t].append([f, c])

    min_cost = sys.maxsize
    for K in list(graph):
        # if K is start node
        # (total_cost, current_node)
        Q = [(0, [K], set([K]))]
        dist = sys.maxsize
        while Q:
            total_cost, nodes, visited = heapq.heappop(Q)
            #print(graph)
            #print(total_cost, nodes, visited)
            #print(Q)
            #print(dist)
            #input()
            if len(nodes) < n and len(visited) < n:
                for v, c in graph[nodes[-1]]:
                    cumulated_cost = total_cost + c
                    heapq.heappush(Q, (cumulated_cost, nodes + [v], visited | {v}))
            if len(visited) == n:
                dist = min(dist, total_cost)
        min_cost = min(min_cost, dist)
    return min_cost


print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))