class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, subset):
            if len(nums) < index:
                return

            result.append(subset)

            for i in range(index, len(nums)):
                dfs(i + 1, subset + [nums[i]])

        result = []
        dfs(0, [])

        return result