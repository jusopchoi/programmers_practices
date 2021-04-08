def get_solution(s, length):
    dup = s[0:length]
    count = 1
    new_s = ''
    for index in range(length, len(s), length):
        tmp = s[index:index+length]
        if dup == tmp:
            count = count + 1
        else:
            if count != 1:
                new_s += str(count) + dup
                dup = tmp
                count = 1
            else:
                new_s += dup
                dup = tmp
    if count != 1:
        new_s += str(count) + dup
    else:
        new_s += dup
    return len(new_s)

def solution(s):
    answer = len(s)
    for cut_length in range(1, len(s)):
        length = get_solution(s, cut_length)
        if length < answer:
            answer = length
    return answer
