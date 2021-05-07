class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start, fuel = 0, 0
        for i, gc in enumerate(zip(gas, cost)):
            g, c = gc
            if fuel + g < c:
                start = i + 1
                fuel = 0
            else:
                fuel += g - c

        return start