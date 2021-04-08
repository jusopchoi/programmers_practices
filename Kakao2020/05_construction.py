def building_checker(answer, x, y, a):
    if a == 0:
        if y == 0:
            return True
        elif [x, y - 1, 0] in answer:
            return True
        elif [x - 1, y, 1] in answer:
            return True
        elif [x, y, 1] in answer:
            return True
    else:
        if [x, y - 1, 0] in answer:
            return True
        if [x + 1, y - 1, 0] in answer:
            return True
        if [x - 1, y, 1] in answer and [x + 1, y, 1] in answer:
            return True
    return False

def removing_checker(answer, x, y, a):
    answer.remove([x, y, a])
    for ans in answer:
        checker = building_checker(answer, ans[0], ans[1], ans[2])
        if not checker:
            answer.append([x, y, a])
            return False
    answer.append([x, y, a])
    return True
    
def solution(n, build_frame):
    answer = []
    for build in build_frame:
        x, y, a, b = build[0], build[1], build[2], build[3]
        if b == 1:
            checker = building_checker(answer, x, y, a)
        else:
            checker = removing_checker(answer, x, y, a)
        if checker:
            if b == 1:
                answer.append([x, y, a])
            elif [x, y, a] in answer:
                answer.remove([x, y, a])
    answer.sort()
    if answer == []:
        answer = [[]]
    return answer
