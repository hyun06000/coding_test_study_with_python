def solution(n, computers):
    visited = [0] * n

    def dfs(v):
        visited[v] = 1
        for i, w in enumerate(computers[v]):
            if w and not visited[i]:
                dfs(i)

    count = 0
    for v in range(n):
        if not visited[v]:
            dfs(v)
            count += 1

    return count