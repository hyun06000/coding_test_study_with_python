# 561_array_partition_1.py

from frame import Solution as frame

inputs = [[1, 4, 3, 2]]
labels = [4]

# 1
class Solution(frame):
    def answer_method(self, nums: list[int]) -> int:
        mul = 1
        result = []
        for i in range(len(nums)):
            result.append(mul)
            mul *= nums[i]

        mul = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * mul
            mul *= nums[i]

        return result

sol = Solution(1)
sol.checker(inputs, labels)