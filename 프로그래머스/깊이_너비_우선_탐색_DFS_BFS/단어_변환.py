def solution(begin, target, words):
    if not target in words:
        return 0

    def single_diff(ref: str, comp: str) -> bool:
        for i in range(len(ref)):
            if ref[:i] + ref[i + 1:] == \
                    comp[:i] + comp[i + 1:]:
                return True

    min_step = []

    def dfs(v, step=0, visited=[]):
        visited.append(v)

        if v == target:
            min_step.append(step)
            return
        elif step == len(words):
            return

        step += 1
        for w in words:
            if single_diff(v, w) and not w in visited:
                dfs(w, step, visited[:])

    dfs(begin)
    return min(min_step)