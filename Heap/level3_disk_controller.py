import heapq as hq
def solution(jobs):
    answer = 0
    length = len(jobs)
    jbs = []
    for j in jobs:
        hq.heappush(jbs, [j[0], j[1], j[0]])
    time = 0
    sum_time = 0
    while True:
        t = hq.heappop(jbs)
        time = t[0] + t[1]
        sum_time += (t[0] + t[1] - t[2])
        if not jbs:
            break
        while True:
            t2 = hq.heappop(jbs)
            if t2[0] >= time:
                hq.heappush(jbs, t2)
                break
            hq.heappush(jbs, [time, t2[1], t2[2]])
    answer = int(sum_time / length)
    return answer
