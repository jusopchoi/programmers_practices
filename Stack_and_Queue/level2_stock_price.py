def solution(prices):
    answer = []
    lists = []
    for pdx in range(len(prices)):
        p = prices[pdx]
        ldx = len(lists) - 1
        while True:
            if ldx < 0:
                break
            l = lists[ldx]
            if l[0] <= p:
                break
            answer[l[2]] = pdx - l[2]
            ldx -= 1
        lists = lists[:ldx + 1]
        lists.append([p, 0, pdx])
        answer.append(0)
    for l in lists:
        answer[l[2]] = pdx - l[2]
    return answer
