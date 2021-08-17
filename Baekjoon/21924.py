# 백준 21924
# 가장 적은 비용으로 모든 노드를 탐색하는 크루스칼 문제이면서
# 가지를 가장 적게 펼친 트리를 구하는 문제로
# MST(Minimum Spanning Tree, 최소 신장 트리) 문제 이다.
# Kruskal 알고리즘, prim 알고리즘을 이용하여 풀이 가능하다.

# 전략 : 
# 도로의 비용이 저렴한 순서로 그래프를 정렬한뒤
# 그 순서대로 꺼내가며 트리를 만든다.
# 트리의 최고 부모 노드로 타고 올라갈 수 있으면
# 같은 트리에 속한 노드 끼리는
# 이미 저렴한 순서대로 도로를 놓은 상태이므로
# 더 이상 도로를 놓을 필요가 없다.
# 다른 트리에 속한 노드 끼리는 
# 현재 탐색중인 간선이 정렬에 의해 가장 저렴하므로
# 현재의 도로를 추가하고 트리를 병합한다.


# 패키지 불러오기
import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline


# 노드와 간선, 그래프에 관한 정보 입력 받기
N, M = map(int, input().split())             # 건물의 수 : 노드의 수 
                                             # 도로의 수 : 간선의 수

parent_index_of_ = [n for n in range(N + 1)] # i번째 노드에 해당하는 건물의 부모 노드가 있을때 부모 노드의 index를 저장하는 리스트
rank_of_ = [0] * (N + 1)                     # 트리 구조에 따른 랭크가 발생하면 i번째 노드의 랭크를 저장하는 리스트
graph = []                                   # 도로의 양 끝 노드와 도로의 비용이 저장되는 리스트

# 전체 그래프 입력받기

COST = 0                                             # 얼마나 절약되는지 계산해야 하므로 전체 비용을 누적해서 계산 
for i in range(1, M + 1):
    node_a, node_b, cost = map(int, input().split()) # 양 끝 노드와 도로의 비용 
    graph.append([cost, node_a, node_b])             # 도로 비용, 노드 a, 노드 b 순서로 정렬
    COST += cost                                     # 모든 도로에 대한 비용 누적



# 최고 부모 탐색, 트리 병합 알고리즘

def find(node):
    if parent_index_of_[node] == node:
        return node                      # 만약 a의 부모 노드가 a 자신이면 a 를 그대로 반환
    p = find(parent_index_of_[node])     # 그렇지 않으면 재귀적으로 부모 노드를 거슬러 올라가면서 탐색
    parent_index_of_[node] = p           # 입력받은 노드의 부모 노드로 부모 노드 갱신
    return p                             # 갱신한 부모노드 반환
                                         # 최종적으로는 같은 줄기에 있는 모든 노드의 부모 노드 값이
                                         # 최고 부모 노드로 모두 변경되는 결과

def union(node_a, node_b):
    highest_node_A = find(node_a)         # a가 속한 트리의 최고 부모 노드로 치환
    highest_node_B = find(node_b)         # b가 속한 트리의 최고 부모 노드로 치환
    if highest_node_A == highest_node_B:  # 부모노드가 동일한 경우 
        return                            # 같은 트리에 속했으므로 아무 작업 없이 끝
    
    if rank_of_[highest_node_A] > rank_of_[highest_node_B]:       # a 가 속한 트리의 최고 랭크가 더 높을 경우
        parent_index_of_[highest_node_B] = highest_node_A         # a 가 속한 트리 쪽으로 병합 ( 최고 부모 노드 통합 )
    else:                                                         # a가 속한 트리의 최고 랭크가 같거나 작을 경우
        parent_index_of_[highest_node_A] = highest_node_B         # b 쪽으로 병합
        if rank_of_[highest_node_A] == rank_of_[highest_node_B]:  # 랭크가 같은 트리 끼리 병합한 경우
            rank_of_[highest_node_B] += 1                         # 최고 부모노드의 랭크를 1 올려줌
            

# 크루스칼 알고리즘
def kruskal(graph):
    graph.sort()   # 비용을 오름차순으로 정렬하여 저렴한 순서대로 추출
    total_cost = 0 # MST 의 비용

    # 간선 연결 탐색
    for edge_and_node in graph:
        cost, start, end = edge_and_node # 간선의 정보
        if find(start) != find(end):     # 서로 다른 트리에 속한 경우 아직 탐색하지 않은 도로 이므로 탐색
            union(start, end)            # 트리 병합
            total_cost += cost           # 비용 누적

    return total_cost

min_cost = kruskal(graph)
p_set = set([find(node) for node in range(1, N + 1)])
if len(p_set) == 1: 
    print(COST - min_cost)
else:
    print(-1)