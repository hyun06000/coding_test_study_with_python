from tictoc import tictoc

@tictoc
def hyun_sol(verbose):

    #햄버거랑 토핑 주어짐
    m = 27
    hamberger = [8, 11]
    topping = [3, 5]

    _max = [0]
    # 메뉴로 모으면서 토핑이면 True, 햄버거면 False 추가한 튜플로 구성
    menu = []
    for h in hamberger:
        menu.append((h, False))
    for t in topping:
        menu.append((t, True))

    # dfs 로 탐색하는데 토핑은 중복을 허용하지 않고
    # 햄버거는 중복을 허용해야한다면 아래와같이 구성
    def dfs(
            v,          # dfs로 탐색할 노드
            nodes,      # 이때까지 탐색한 노드
            selection,  # 탐색과정에서 선택된 메뉴들
            visited,    # 토핑의 중복을 허용하지 않기위한 방문기록
    ):

        # 중단조건
        if _max[0] < selection <= m:           # 예산과 같거나 적으면 탐색 중단
            _max[0] = max(_max[0], selection)
            if verbose >= 2:
                print(selection, nodes)  # 탐색된 노드들
        else:
            return

        # 토핑 중복만 차단
        if v[1]:               # 만약에 토핑이면
            visited.append(v)  # 중복 차단

        # dfs 재귀 탐색
        for w in menu:

            if w not in visited:       # 여기서 걸리는건 토핑의 중복여부, 햄버거는 통과 가능
                dfs(                   # dfs시작
                    w,                 # 다음 탐색 노드 : (가격, 토핑?)
                    nodes + [w],       # 탐색된 노드 기록
                    selection + w[0],  # 가격 누적해서 중단 조건 검사
                    visited[:],        # 이때까지 방문한 토핑 모두 복사
                )

    for v in menu:
        if not v[1]:                  # 만약에 햄버거면 dfs 시작
            dfs(
                v         = v,        # 햄버거 v 부터 시작
                nodes     = [v],      # v 부터 탐색 기록
                selection = v[0],     # 총 매뉴들의 가격 합, v 부터 시작
                visited   = [],       # 토핑의 중복을 허용하지 않기위한 방문기록
            )                         # 햄버거는 반드시 1개 이상 골라야하고
                                      # 토핑은 하나도 고르지 않아도 되므로
                                      # 햄버거면 시작, 토핑이면 시작 안함
    if verbose >= 1:
        print(_max[0])