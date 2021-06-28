from collections import defaultdict
import sys

R, C = map(int, input().split(" "))

board = defaultdict(str)
for r in range(R):
    #row = input()
    row = sys.stdin.readline().strip()
    for c in range(C):
        board[f'{r}_{c}'] = row[c]

route = 0
di_dj = [(-1, 0), (0, -1), (1, 0), (0, 1)]
def dfs(i, j, visited = set()):
    global board, route
    if board[f'{i}_{j}'] in visited:
        route = max(route, len(visited))
        return

    visited.add(board[f'{i}_{j}'])

    for di, dj in di_dj:
        _i = i + di
        _j = j + dj
        if i < 0 or j < 0 or i >= R or j >= C:
            route = max(route, len(visited))
            continue
        dfs(_i, _j, visited.copy())

dfs(0, 0)
print(route-1)