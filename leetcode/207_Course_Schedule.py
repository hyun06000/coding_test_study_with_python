import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # graph
        graph = collections.defaultdict(list)
        for a_i, b_i in prerequisites:
            graph[a_i].append(b_i)

        traced = set()
        visited = set()

        def dfs(i):
            if i in traced:
                return False
            if i in visited:
                return True

            traced.add(i)

            for w in graph[i]:
                if not dfs(w):
                    return False

            traced.remove(i)
            visited.add(i)

            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True