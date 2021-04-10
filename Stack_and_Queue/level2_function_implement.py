import math
def solution(progresses, speeds):
    answer = []
    date = {}
    last_date = 0
    for p, s in zip(progresses, speeds):
        d = math.ceil(float(100-p)/float(s))
        if last_date > d:
            d = last_date
        else:
            last_date = d
        try:
            date[d] += 1
        except:
            date[d] = 1
    for d in date:
        answer.append(date[d])
    return answer
