List = list
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def DFS_search(grid, i, j):
            if i >= len(grid[0]) or i < 0:
                return
            if j >= len(grid) or j < 0:
                return

            if grid[j][i] != "1":
                return

            grid[j][i] = 0  # prunning

            DFS_search(grid, i + 1, j)  # east
            DFS_search(grid, i, j + 1)  # south
            DFS_search(grid, i - 1, j)  # west
            DFS_search(grid, i, j - 1)  # north

        count = 0
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if grid[j][i] == "1":
                    DFS_search(grid, i, j)
                    count += 1
        return count