# leetcode 125 valid palindrome

def checker(Sol):
    # ex_1
    in_chars_1 = "A man, a plan, a canal: Panama"
    label_1 = True

    print('case_1')
    ans_1 = Sol.isPalindrome(in_chars_1)
    print(ans_1 == label_1)


    # ex_2
    in_chars_2 = "race a car"
    label_2 = False

    print('case_2')
    ans_2 = Sol.isPalindrome(in_chars_2)
    print(ans_2 == label_2)


# 1
class Solution:
    def isPalindrome(self, s: str) -> bool:

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
checker(sol_1)

# 2
import collections

Deque = collections.deque()

class Solution:
    def isPalindrome(self, s: str) -> bool:
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
checker(sol_2)

# 3
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # make s as lower case
        s = s.lower()

        # filtering with regular expression
        s = re.sub('[^0-9a-z]', '', s)

        # String s is not list. So .reverse() is not working.
        # In this case indexing with step -1 is the method to reverse.
        return s == s[::-1]


print('### Solution_3')
sol_3 = Solution()
checker(sol_3)