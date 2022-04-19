# 백준 12865
# 분할 불가능 배낭 문제

def solution_1():
    N, K = list(map(int, input().split(" ")))

    cargo = []
    for _ in range(N):
        cargo.append(list(map(int, input().split(" "))))

    def tabulation(cargo, capacity):
        pack = []
        for i in range(len(cargo) + 1):
            pack.append([])
            for c in range(capacity + 1):
                if i == 0 or c == 0:
                    pack[i].append(0)
                elif cargo[i-1][0] <= c:
                    pack[i].append(
                        max(
                            cargo[i-1][1] + pack[i-1][c - cargo[i-1][0]],
                            pack[i-1][c]
                        )
                    )
                else:
                    pack[i].append(pack[i-1][c])
        return pack[-1][-1]

    r = tabulation(cargo, K)
    print(r)

def solution_2():
    import sys

    readline = sys.stdin.readline
    N, K = list(map(int, readline().strip().split(" ")))

    cargos = []
    for _ in range(N):
        thing = list(map(int, readline().strip().split(" ")))
        cargos.append(thing)

    def tabulatation(cargos, capacity):
        pack = [0 for _ in range(capacity + 1)]
        pack = [pack[:] for _ in range(len(cargos) + 1)]

        for i in range(len(cargos) + 1):
            for j in range(capacity + 1):
                if i == 0 or j == 0:
                    continue
                else:
                    cur_weight, cur_value = cargos[i-1]
                    if cur_weight <= j:
                        pack[i][j] += max(
                            cur_value + pack[i-1][j - cur_weight],
                            pack[i-1][j]
                        )
                    else:
                        pack[i][j] += pack[i-1][j]
        return pack[i][j]

    r = tabulatation(cargos, K)
    print(r)
