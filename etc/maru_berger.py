from tictoc import tictoc

@tictoc
def maru_sol(verbose):
    m = 27
    b = [8, 11]
    t = [3, 5]

    n_t = len(t)
    n_b = len(b)

    _max = [0]

    def dfs(tot, visited, tot_list):
        #global m, n_t, n_b, _max


        if _max[0] == m:
            return
        if tot <= m:
            _max[0] = max(_max[0], tot)
            if verbose >= 2:
                print(tot, tot_list)

        '''
        if _max< tot <= m:
            _max = max(_max, tot)
            if verbose >= 2:
                print(tot, tot_list)
        else:
            return
        '''
        if not visited:
            visited = set()

        for b_ in b:
            if tot + b_ <= m:
                tot_list.append(b_)
                dfs(tot + b_, None, tot_list)
                tot_list.pop()

            for t_ in t:
                if t_ not in visited:
                    visited.add(t_)
                    tot_list.append(t_)
                    dfs(tot + t_, visited, tot_list)
                    tot_list.pop()

    for i in b:
        if _max[0] == m:
            break
        dfs(i, None, [i])

    if verbose >= 1:
        print(_max[0])
