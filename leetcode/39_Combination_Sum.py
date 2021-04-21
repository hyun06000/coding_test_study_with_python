class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(cumulated, index, path):
            if cumulated > target:
                return
            if cumulated == target:
                result.append(path)
                return
            for i in range(index, len(candidates)):
                n = candidates[i]
                dfs(cumulated + n, i, path + [n])

        result = []
        dfs(0, 0, [])

        return result

