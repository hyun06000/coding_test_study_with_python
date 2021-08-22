# 백준 2668번 숫자고르기

# 전략
# 그래프를 그렸을때 순환하는 그래프가 있는지 찾는다.
# 단, 순환하는 그래프는 완전한 모든 점에서 출발하여
# 자기 자신으로 돌아올 수 있는 완전한 고리 모양만을 말한다.

N = int(input())

graph = {i : int(input()) for i in range(1, N + 1)}

def dfs(v, circle : list, head : set):
    if circle and v in circle:
        if v == circle[0]:
            for i in circle:
                head.add(i)
            return head
        else :
            return head
    circle.append(v)
    return dfs(graph[v], circle, head)

head = set()
for i in range(1, N + 1):
    circle = []
    head = dfs(i, circle, head)

print(len(head))
for i in sorted(head):
    print(i)