# beakjoon 10451

# Recursion limit을 늘려줘서 에러를 방지
import sys
sys.setrecursionlimit(100000)

# T개의 테스트를 풀어야 하므로 T번 수행한다.
T = int(input())
for _ in range(T):
    # 순열의 길이 N과 순열을 받아서 graph를 만든다.
    N = int(input())
    permutation = list(map(int, input().split(" ")))

    graph = {n + 1 : [permutation[n]] for n in range(N)}

    # dfs로 탐색하여 진행경로(trace)상에 있는 노드중에 한번 방문한 노드가 있다면
    # 순환구조로 판별하고 return한다. 진행경로는 갈림길마다 하나씩 reset 하므로
    # 해당 노드의 모든 갈래길을 다 탐색한 후에는 해당 노드를 지워주어야 한다.
    # 또 한번 탐색된 노드는 다시 방문했을때 순환구조가 중복 count 될 수 있으므로
    # 진행경로 추적을 위한 set 말고 방문 기록을 남기기 위한 set을
    # 추가적으로 만들어서 기록한다. 그리고 trace를 통해 순환 구조가 발견되면
    # count를 하나 증가시키면서 탐색을 마치고 visited에 의해 탐색이 마쳐질 경우는
    # count를 올리지 않아야 한다.

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
