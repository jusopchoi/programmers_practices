def locate(key, M):
    new_key = []
    for x in range(M):
        tmp_key = []
        for y in range(M - 1, -1, -1):
            tmp_key.append(key[y][x])
        new_key.append(tmp_key)
    return new_key

def match(lock, key, empty_holes, M, N):
    for start_x in range(N-M):
        for start_y in range(N-M):
            chk = True
            holes = 0
            for x in range(M):
                if not chk:
                    break
                for y in range(M):
                    if key[x][y] == 1:
                        if lock[x + start_x][y + start_y] == 1:
                            chk = False
                            break
                        else:
                            if x + start_x >= M and x + start_x < N - M:
                                if y + start_y >= M and y + start_y < N - M:
                                    holes += 1
            if chk and holes == empty_holes:
                return True
    return False

def solution(key, lock):
    answer = False
    M = len(key)
    N = len(lock)
    holes = 0
    for x in range(N):
        for y in range(N):
            if lock[x][y] == 0:
                holes += 1
    new_lock = []
    for x in range(M):
        tmp = []
        for y in range(N + M * 2):
            tmp.append(0)
        new_lock.append(tmp)
    for x in range(N):
        tmp = []
        for y in range(M):
            tmp.append(0)
        for y in range(N):
            tmp.append(lock[x][y])
        for y in range(M):
            tmp.append(0)
        new_lock.append(tmp)
    for x in range(M):
        tmp = []
        for y in range(N + M * 2):
            tmp.append(0)
        new_lock.append(tmp)
    if holes == 0:
        return True
    answer = match(new_lock, key, holes, M, N + 2 * M)
    if answer:
        return answer
    key = locate(key, M)
    answer = match(new_lock, key, holes, M, N + 2 * M)
    if answer:
        return answer
    key = locate(key, M)
    answer = match(new_lock, key, holes, M, N + 2 * M)
    if answer:
        return answer
    key = locate(key, M)
    answer = match(new_lock, key, holes, M, N + 2 * M)
    return answer
