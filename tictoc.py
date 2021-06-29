import time as T
from collections import defaultdict

def tictoc(func):
    def wrapper(i,j):
        tic = T.time()

        func(i, j)

        toc = T.time()
        print(toc - tic)
    return wrapper

@tictoc
def defaultdict_map(N, M):
    board = defaultdict(str)
    for r in range(N):
        row = input()
        for c in range(M):
            board[f'{r}_{c}'] = row[c]

    for r in range(N):
        for c in range(M):
            k = board[f'{r}_{c}']

R, C = map(int, input().split(" "))

defaultdict_map(R, C)

# faster way !
@tictoc
def defaultdict_map(N, M):
    board = []
    for r in range(N):
        board.append(input())

    for r in range(N):
        for c in range(M):
            k = board[r][c]

R, C = map(int, input().split(" "))

defaultdict_map(R, C)