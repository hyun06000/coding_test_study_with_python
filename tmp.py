# Beakjoon 9466

import sys
sys.setrecursionlimit(100000)

def cyclic_graph():
    N = int(sys.stdin.readline())
    graph = list(map(int, sys.stdin.readline().split(" ")))

    answer = [[]]
    visited = set()
    def dfs(v, trace = []):
        if trace and v in trace:
            answer[0] += trace[trace.index(v):]
            return

        if v in visited:
            return

        visited.add(v)
        trace.append(v)
        dfs(graph[v-1], trace)
        trace.pop()


    for v in range(1, N + 1):
        if v not in visited:
            dfs(v)

    print(N - len(answer[0]))


T = int(sys.stdin.readline())
for _ in range(T):
    cyclic_graph()