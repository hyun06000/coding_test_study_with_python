def solution(progresses, speeds):
    answer = []
    complete = []
    for pro, spe in zip(progresses, speeds):
        div, mod = divmod((100 - pro), spe)
        if mod:
            div += 1

        if complete and complete[0] < div:
            answer.append(len(complete))
            complete = []

        complete.append(div)

    if complete:
        answer.append(len(complete))
    else:
        answer.append(div)
    return answer