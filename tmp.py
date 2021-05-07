from collections import Counter
a = [1,1,1,2,2,2,3,3,3,4,5,5]
b = [1,2,3,4,5,6]

a_c = Counter(a)
b_c = Counter(b)

print(a_c)
print(b_c)
print(a_c - b_c)



def solution(n, costs):
    # sort with cost
    costs.sort(key=lambda x: x[2])

    total_cost = 0
    visited = set([costs[0][0]])
    while len(visited) < n:
        for i, cost in enumerate(costs):
            print('costs : ', costs)
            print('cost : ', cost)
            print('visited : ',visited)
            # if cyclic
            if cost[0] in visited and cost[1] in visited:
                print('continue')
                input()
                continue
            # if not cyclic graph but edge can start
            if cost[0] in visited or cost[1] in visited:
                visited.add(cost[0])
                visited.add(cost[1])

                total_cost += cost[2]
                print('update : ', total_cost, visited)
                input()
                del(costs[i])
                break
    return total_cost

n=6
costs = [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]
print(solution(n, costs)) # 11