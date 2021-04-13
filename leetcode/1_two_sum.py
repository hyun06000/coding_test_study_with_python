# 1_two_sum.py

from frame import Solution as frame

inputs = [[2, 7, 11, 15]]
labels = [[0, 1]]

# 1 Brute-Force
class Solution(frame):
    def answer_method(self, nums: list[str]) -> list[str]:
        target = 9
        for i in range(len(nums)):
            for j in range((i + 1), len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

sol_1 = Solution(1)
sol_1.checker(inputs, labels)


# 2
class Solution(frame):
    def answer_method(self, nums: list[str]) -> list[str]:
        target = 9
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[(i + 1):]:
                return [i, nums.index(complement)]


sol_2 = Solution(2)
sol_2.checker(inputs, labels)


# 3
class Solution(frame):
    def answer_method(self, nums: list[str]) -> list[str]:
        target = 9

        nums_dict={}
        for i, n in enumerate(nums):
            nums_dict[n] = i

        for i, n in enumerate(nums):
            if target - n in nums_dict and i != nums_dict[target - n]:
                return [i, nums_dict[target - n]]

sol_3 = Solution(3)
sol_3.checker(inputs, labels)

# 4
class Solution(frame):
    def answer_method(self, nums: list[str]) -> list[str]:
        target = 9

        nums_dict={}
        for i, n in enumerate(nums):
            if target - n in nums_dict:
                return [nums_dict[target - n], i]
            nums_dict[n] = i

sol_4 = Solution(4)
sol_4.checker(inputs, labels)

