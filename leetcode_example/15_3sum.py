# 15_3sum.py

from frame import Solution as frame

inputs = [ [-1, 0, 1, 2, -1, -4] ]
labels = [ [
    [-1, -1, 2],
    [-1, 0, 1]

] ]
# 1
class Solution(frame):
    def answer_method(self, nums: list[int]) -> list[int]:
        # sort and two pointer
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            p_left, p_right = i + 1, len(nums) - 1
            while p_left < p_right:
                summation = nums[i] + nums[p_left] + nums[p_right]
                if summation > 0:
                    p_right -= 1
                elif summation < 0:
                    p_left += 1
                else:
                    result.append([nums[i], nums[p_left], nums[p_right]])
                    while p_left < p_right and nums[p_left] == nums[p_left + 1]:
                        p_left += 1
                    while p_left < p_right and nums[p_right - 1] == nums[p_right]:
                        p_right -= 1
                    p_left += 1
                    p_right -= 1
        return result

sol = Solution(1)
sol.checker(inputs, labels)