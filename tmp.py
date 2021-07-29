import sys
sys.setrecursionlimit(100000)

T = int(input())
for _ in range(T):
    N = int(input())
    permutation = list(map(int, input().split(" ")))

    graph = {n + 1 : [permutation[n]] for n in range(N)}

    visited = set()
    cicle_count = [0]
    def dfs(v, trace = set()):
        if v in trace:
            cicle_count[0] += 1
            return

        if v in visited:
            return

        visited.add(v)
        trace.add(v)
        for w in graph[v]:
            dfs(w, trace)
        trace.remove(v)

    for v in list(graph):
        dfs(v)

    print(cicle_count[0])
