# 화가 많이 난 사람의 코드
import sys
sys.setrecursionlimit(100000)

class ICEBERG:
    def __init__(self):
        self.years = 0
        self.N, self.M = map(int, sys.stdin.readline().split(" "))
        self.iceberg = [ list(map(int, sys.stdin.readline().split(" "))) for _ in range(self.N) ]
        self.didj = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def get_melt(self):
        melt = [[0]*self.M for _ in range(self.N)]
        for i in range(1, self.N - 1):
            for j in range(1, self.M - 1):
                if self.iceberg[i][j]:
                    count = 0
                    for di, dj in self.didj:
                        count += (not self.iceberg[i + di][j + dj])
                    melt[i][j] = count
        self.melt = melt

    def apply_melt(self):
        self.global_is_iceberg = False
        is_iceberg = [[False] * self.M for _ in range(self.N)]
        for i in range(1, self.N - 1):
            for j in range(1, self.M - 1):
                self.iceberg[i][j] = max(0, self.iceberg[i][j] - self.melt[i][j])
                if self.iceberg[i][j]:
                    is_iceberg[i][j] = True
                    self.global_is_iceberg = True
        self.is_iceberg = is_iceberg

    def get_num_of_piece(self):
        def dfs_stack(i, j): # 재귀 DFS 로 풀면 망한다.
            queue = set([(i, j)])
            self.is_iceberg[i][j] = False

            while queue:
                i, j = queue.pop()
                for di, dj in self.didj:
                    _i, _j = i + di, j + dj
                    if 0 < _i < self.N - 1 and 0 < _j < self.M - 1 and \
                            self.is_iceberg[_i][_j]:
                        queue.add((_i, _j))
                        self.is_iceberg[_i][_j] = False

        self.num_of_piece = 0
        for i in range(1, self.N - 1):
            for j in range(1, self.M - 1):
                if self.is_iceberg[i][j]:
                    dfs_stack(i, j)
                    self.num_of_piece += 1
                    if self.num_of_piece > 2:
                        return

    def single_year(self):
        self.get_melt()
        self.apply_melt()
        if self.global_is_iceberg:
            # 2조각 이상으로 안나뉘는 경우 고려 안하면 인생 조진다.
            self.get_num_of_piece()
            self.years += 1

    def simulation(self):
        while True:
            self.single_year()
            if not self.global_is_iceberg or self.num_of_piece > 1:
                break
        if not self.global_is_iceberg:
            print(0)
        else:
            print(self.years)

if __name__ == "__main__":
    _ICEBERG =ICEBERG()

    _ICEBERG.simulation()
