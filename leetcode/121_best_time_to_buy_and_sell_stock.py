from frame import Solution as frame

inputs = [[7, 1, 5, 3, 6, 4]]
labels = [5]

# 1
class Solution(frame):
    def answer_method(self, prices: list[int]) -> int:

        min_val = prices[0]
        profit = 0
        for i in range(len(prices)):
            min_val = min(prices[i] , min_val)
            profit = max(profit, prices[i] - min_val)

        return profit
sol = Solution(1)
sol.checker(inputs, labels)
