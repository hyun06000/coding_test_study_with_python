from collections import deque

R, C = map(int, input().split(' '))

board = []
for _ in range(R):
    row = []
    for char in input():
        row.append(char)
    board.append(row)

di_dj = [(-1, 0), (0, -1), (1, 0), (0, 1)]
def bfs(i, j):
    visited = [board[i][j]]
    queue = deque([(i, j)])
    while queue:
        i, j = queue.popleft()
        print(i, j)
        print(visited)
        for di, dj in di_dj:
            if i + di >= 0 and j + dj >= 0 and i + di < R and j + dj < C:
                if not board[i + di][j + dj] in visited:
                    visited.append(board[i + di][j + dj])
                    queue.append((i + di, j + dj))
    return visited
visited = bfs(0, 0)
print(len(visited))

'''
route = []
def dfs(i, j, visited = []):
    global route, board

    if i < 0 or j < 0 or i >= R or j >= C:
        route.append(len(visited))
        return
    if board[i][j] in visited:
        route.append(len(visited))
        return

    visited.append(board[i][j])

    dfs(i - 1, j, visited[:])
    dfs(i, j - 1, visited[:])
    dfs(i + 1, j, visited[:])
    dfs(i, j + 1, visited[:])

dfs(0, 0)
print(max(route))
'''