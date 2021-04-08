def search_start(n, weak):
    short = weak[-1] - weak[0]
    new_weak = weak
    for ith in range(1, len(weak)):
        temp_short = n - weak[ith] + weak[ith - 1]
        if temp_short < short:
            short = temp_short
            new_weak = weak[ith:] + weak[:ith]
    weak = []
    for w in new_weak:
        if w < new_weak[0]:
            weak.append(w + n - new_weak[0])
        else:
            weak.append(w - new_weak[0])
    return short, weak

def search_paths(weak, dist, answer, max_answer):
    if answer >= max_answer:
        return max_answer + 1
    if weak == []:
        return answer
    lowest = max_answer + 1
    st = weak[0]
    for idx in range(len(dist)):
        wdx = 0
        d = dist[idx]
        while True:
            if wdx >= len(weak):
                break
            point = weak[wdx]
            if point - st > d:
                break
            wdx += 1
        tmp_answer = search_paths(weak[wdx:], dist[:idx] + dist[idx + 1:], answer + 1, max_answer)
        if tmp_answer < lowest:
            lowest = tmp_answer
    return lowest

def solution(n, weak, dist):
    answer = len(dist) + 1
    st, weak = search_start(n, weak)
    if weak == []:
        return answer
    st = weak[0]
    for idx in range(len(dist)):
        wdx = 0
        d = dist[idx]
        while True:
            if wdx >= len(weak):
                break
            point = weak[wdx]
            if point - st > d:
                break
            wdx += 1
        tmp_answer = search_paths(weak[wdx:], dist[:idx] + dist[idx + 1:], 1, answer)
        if tmp_answer < answer:
            answer = tmp_answer
    if answer == len(dist) + 1:
        answer = -1
    return answer
