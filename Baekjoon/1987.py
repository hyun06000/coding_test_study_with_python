import sys

sys.setrecursionlimit(100000)

R, C = map(int, input().split(" "))

board =[]
for _ in range(R):
    board.append(input())

di_dj = [(1, 0), (0, 1), (-1, 0), (0, -1)]

max_len = 0
def dfs(i, j , visited):
    global max_len

    if i < 0 or j < 0 or i >= R or j >= C:
        max_len = max(max_len, len(visited))
        return

    if board[i][j] in visited:
        max_len = max(max_len, len(visited))
        return

    for di, dj in di_dj:
        dfs(i+di, j+dj, visited + board[i][j])

dfs(0, 0 , '')
print(max_len)