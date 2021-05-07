class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        result = 0
        for pre, post in zip(prices, prices[1:] + [0]):
            if pre < post:
                result += post - pre
        return result