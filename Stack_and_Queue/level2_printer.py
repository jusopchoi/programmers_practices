def solution(priorities, location):
    answer = 0
    pdx = 0
    poped = 1
    while True:
        if priorities == []:
            break
        p = priorities.pop(0)
        chk = True
        for p2 in priorities:
            if p2 > p:
                priorities.append(p)
                chk = False
                break
        if chk:
            if location == 0:
                answer = poped
                break
            poped += 1
        location -= 1
        if location == -1:
            location = len(priorities) - 1
    return answer
