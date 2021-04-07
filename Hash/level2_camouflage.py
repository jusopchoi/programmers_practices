def solution(clothes):
    cloth = {}
    for c in clothes:
        try:
            cloth[c[1]] += 1
        except:
            cloth[c[1]] = 1
    answer = 1
    for c in cloth:
        answer *= (cloth[c] + 1)
    answer -= 1
    return answer
