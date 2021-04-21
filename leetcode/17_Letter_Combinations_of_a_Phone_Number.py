class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, word):
            if index >= len(digits):
                result.append(word)
                return

            for w in key_pad[digits[index]]:
                dfs(index + 1, word + w)

        if digits == "":
            return []

        result = []
        key_pad = {"2": "abc",
                   "3": "def",
                   "4": "ghi",
                   "5": "jkl",
                   "6": "mno",
                   "7": "pqrs",
                   "8": "tuv",
                   "9": "wxyz"}

        dfs(0, "")

        return result