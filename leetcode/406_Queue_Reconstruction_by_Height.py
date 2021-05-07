class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        pq = []
        for h, k in people:
            heapq.heappush(pq, [-h, k])

        result = []
        while pq:
            h, k = heapq.heappop(pq)
            result.insert(k, [-h, k])
        return result