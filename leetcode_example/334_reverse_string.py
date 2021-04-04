# 334_reverse_string.py
from frame import Solution as frame
from copy import deepcopy

inputs = [["h", "e", "l", "l", "o"],
          ["H", "a", "n", "n", "a", "h"]]
labels = [["o", "l", "l", "e", "h"],
          ["h", "a", "n", "n", "a", "H"]]

# 1
inputs_ = deepcopy(inputs)
labels_ = deepcopy(labels)
class Solution(frame):
    def answer_method(self, strs : list[str]) -> list[str]:
        # two-pointer swap method
        p_left, p_right = 0, len(strs)-1

        while p_left < p_right:
            strs[p_left], strs[p_right] = strs[p_right], strs[p_left]
            p_left += 1
            p_right -= 1

        # In original problem,
        # return is not allowed.
        # So, in this case,
        # input arg and return val should be same for each other.
        return strs

sol_1 = Solution()
sol_1.checker(inputs_, labels_)

# 2
inputs_ = deepcopy(inputs)
labels_ = deepcopy(labels)
class Solution(frame):
    def answer_method(self, strs : list[str]) -> list[str]:
        # pythonic method
        strs.reverse()

        return strs
sol_2 = Solution()
sol_2.checker(inputs_, labels_)


# 3
inputs_ = deepcopy(inputs)
labels_ = deepcopy(labels)
class Solution(frame):
    def answer_method(self, strs : list[str]) -> list[str]:
        # list slice method
        strs = strs[::-1]

        return strs

sol_3 = Solution()
sol_3.checker(inputs_, labels_)
