from frame import Solution as frame

inputs = ["babad", "babad", "cbbd"]
labels = ["aba", "bab", "bb"]


# 1
class Solution(frame):
    def answer_method(self, string: str) -> str:
        # two pointer method
        # moving palindrome filter
        def pal_filter(p_left, p_right):
            while p_left >= 0 and p_right <= len(string) and \
                    string[p_left] == string[p_right]:
                    # expand filter
                    p_left -= 1
                    p_right += 1
            return string[p_left + 1 : p_right]

        # return directly when the string is a single character
        # or the longest palindrome is itself
        if len(string) < 1 and string == string[::-1]:
            return string

        # search all palindrome with pal_filter
        # and return the longest one
        longest_pal = ""
        for i in range(len(string)-1):
            print("odd filter : ", pal_filter(i, i))
            print("even filter : ", pal_filter(i, i+1))
            longest_pal = max(longest_pal,
                              pal_filter(i, i),
                              pal_filter(i, i + 1),
                              key=len)
        print(longest_pal)
        return longest_pal


sol_1 = Solution()
sol_1.checker(inputs, labels)
