# 819 most_common_word.py
from frame import Solution as frame

inputs = ["Bob hit a ball, the hit BALL, flew far after it was hit."]
labels = ["ball"]

# 1
import re
import collections
class Solution(frame):
    def answer_method(self, string: str) -> str:
        # banned word
        banned = ["hit"]

        # replace what is not alphabet to a single space.
        filtered_str = re.sub(r"[^\w]", " ", string.lower())
        # make split list with condition
        list_filtered_str = [word
                             for word in filtered_str.split()
                             if word not in banned]
        # count it
        count = collections.Counter(list_filtered_str)
        return count.most_common(1)[0][0]

sol_1 = Solution()
sol_1.checker(inputs, labels)