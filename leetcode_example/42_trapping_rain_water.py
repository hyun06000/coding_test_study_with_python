# 42_trapping_rain_water.py

from frame import Solution as frame

inputs = [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]]
labels = [ 6 ]

# 1
class Solution(frame):
    def answer_method(self, height : list[int]) -> int:
        # two pointer method
        if not len(height):
            return 0
        else:
            p_left, p_right = 0, len(height) - 1
            max_left, max_right = height[p_left], height[p_right]
            volume = 0
            while p_left < p_right:
                if max_left < max_right:
                    if max_left < height[p_left + 1]:
                        max_left = height[p_left + 1]
                    else:
                        volume += max_left - height[p_left + 1]
                    p_left += 1
                else:
                    if max_right < height[p_right - 1]:
                        max_right = height[p_right - 1]
                    else:
                        volume += max_right - height[p_right - 1]
                    p_right -= 1

            return volume

sol = Solution(1)
sol.checker(inputs, labels)