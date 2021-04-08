def make_string(w):
    if w == '':
        return ''
    u = w[0]
    count = 1 if u == '(' else -1
    chk_perfect = (True if count > 0 else False)
    for ch in w[1:]:
        u += ch
        count += (1 if ch == '(' else -1)
        if count == 0:
            break
        if chk_perfect and count < 0:
            chk_perfect = False
    if chk_perfect:
        return u + make_string(w[len(u):])
    else:
        new_u = ''
        for ch in u[1:-1]:
            if ch == '(':
                new_u += ')'
            else:
                new_u += '('
        return '(' + make_string(w[len(u):]) + ')' + new_u

def solution(p):
    answer = make_string(p)
    return answer
