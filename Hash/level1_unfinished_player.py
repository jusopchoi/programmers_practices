def solution(participant, completion):
    answer = ''
    parti = {}
    for name in participant:
        try:
            parti[name] += 1
        except:
            parti[name] = 1
    for name in completion:
        parti[name] -= 1
        if parti[name] == 0:
            parti.pop(name)
            
    answer = list(parti.keys())[0]
    return answer
