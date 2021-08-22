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