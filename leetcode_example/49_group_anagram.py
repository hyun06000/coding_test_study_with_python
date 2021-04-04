from frame import Solution as frame

inputs = [["eat", "tea", "tan", "ate", "nat", "bat"]]
labels = [[
    ["ate", "eat", "tea"],
    ["nat", "tan"],
    ["bat"]
]]

# 1
import collections
class Solution(frame):
    def answer_method(self, words: list[str]) -> list[list[str]]:
        sorted_words = collections.defaultdict(list)
        for word in words:
            sorted_words["".join(sorted(word))].append(word)

        anagrams = []
        for anagram in sorted_words.values():
            anagrams.append(sorted(anagram))

        return anagrams

sol_1 = Solution()
sol_1.checker(inputs, labels)