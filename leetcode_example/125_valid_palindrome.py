# leetcode 125 valid palindrome
from frame import Solution as frame

inputs = ["A man, a plan, a canal: Panama",
          "race a car"]
labels = [True,
          False]

# 1
class Solution(frame):
    def answer_method(self, s: str) -> bool:

        # encode input 's' to the list of strings
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        # check palindrome
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True

print('### Solution_1')
sol_1 = Solution()
sol_1.checker(inputs, labels)

# 2
import collections

Deque = collections.deque()

class Solution(frame):
    def answer_method(self, s: str) -> bool:
        # encode input s to a Deque of strings
        strs: Deque = collections.deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # check it is palindrome
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True


print('### Solution_2')
sol_2 = Solution()
sol_2.checker(inputs, labels)

# 3
import re

class Solution(frame):
    def answer_method(self, s: str) -> bool:
        # make s as lower case
        s = s.lower()

        # filtering with regular expression
        s = re.sub('[^0-9a-z]', '', s)

        # String s is not list. So .reverse() is not working.
        # In this case indexing with step -1 is the method to reverse.
        return s == s[::-1]


print('### Solution_3')
sol_3 = Solution()
sol_3.checker(inputs, labels)
