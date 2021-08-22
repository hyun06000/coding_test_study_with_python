# 백준 2104 번 부분배열 고르기

# 최대 부분 배열 문제는 분할정복으로 풀 수 있다.
# 참고한 곳 : https://blog.naver.com/PostView.nhn?isHttpsRedirect=true&blogId=hongjg3229&logNo=221731014713
#            https://devbelly.tistory.com/61
# 
# 기본적으로 2분할 하여 분할정복한다.
# subarray의 경우의 수를 따져보면
# 1. 0 에서 i 까지
# 2. i 에서 len(A)까지
# 3. i 에서 j까지
# 이때 i, j 는 임의의 인덱스다.
# 1번과 2번은 분할정복으로 구할 수 있다고 해도 3번은 구하기 힘들다.
# 1과 2를 재귀로 분할정복한 뒤 3을 찾아주는 부분도 추가해서 검색한다.
#  EOS


import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split(" ")))

def solution(
    start_p : int, # subarray를 찾고자 하는 array의 시작점
     end_p : int   # subarray를 찾고자 하는 array의 시작점
     ) -> int:     # 조건에 맞게 찾아진 subarray의 점수
    
    
    # 시작점과 끝점의 중간지점을 기준으로
    # 재귀적으로 분할하여 탐색한다.
    # 최소 단위의 부분 배열인 길이 1 짜리에 도달하면
    # 규칙에 따라 자신의 값을 제곱하여 리턴하고 더 큰 값에서 비교를 시작한다.
    # 그리고나서 배열을 확장시켜줘야 하는데 어느 방향으로 확장할 것인지는
    # greedy 로 결정한다.
    # 분할이 일어나는 분기의 순서에 따라 왼쪽에서 오른쪽으로  탐색된다고 생각하면 편하다.
    # EOS

    if start_p == end_p:
        return A[start_p] * A[end_p]
    
    mid = (start_p + end_p) // 2  
    score = max(solution(start_p, mid), solution(mid+1, end_p))

    left, right = mid, mid + 1
    _sum = A[left] + A[right]
    _min_val = min( A[left], A[right] )
    score = max(score,  _sum * _min_val ) 

    while left > start_p or right < end_p:
        
        # left와 right 모두 양 끝에 도달하면 while을 멈춘다.
        # 어느 한쪽이 먼저 끝에 도달하면 그 다음부터는
        # 무조건 다른 한쪽도 끝에 닿을때까지 증가시킨다.
        # 어느 한쪽도 끝에 도달하지 않았으면
        # 옮겼을때 더 큰 쪽으로 증가시킨다.
        # EOS

        if right < end_p and (left == start_p or A[left-1] < A[right + 1]):

            right += 1
            _sum += A[right]
            _min_val = min(_min_val, A[right])
        else:
            left -= 1
            _sum += A[left]
            _min_val = min(_min_val, A[left])
            
        score = max(score,  _sum * _min_val ) 
    
    return score

print(solution(0, N - 1))