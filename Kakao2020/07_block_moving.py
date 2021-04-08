def BFS(board, answer, max_answer, n):
    queue = [[0, 0, 0, 1, 0]]
    visited = [[0, 0, 0, 1]]
    while True:
        if len(queue) == 0:
            break
        visit = queue.pop(0)
        x1, y1, x2, y2 = visit[0], visit[1], visit[2], visit[3]
        value = visit[4]
        if x2 == n - 1 and y2 == n - 1:
            return value
        if x1 == x2:
            if y1 > 0:
                if board[x1][y1 - 1] == 0 and [x1, y1 -1, x2, y2 - 1] not in visited:
                    queue.append([x1, y1 - 1, x2, y2 - 1, value + 1])
                    visited.append([x1, y1 - 1, x2, y2 - 1])
            if y2 < n - 1:
                if board[x2][y2 + 1] == 0 and [x1, y1 + 1, x2, y2 + 1] not in visited:
                    queue.append([x1, y1 + 1, x2, y2 + 1, value + 1])
                    visited.append([x1, y1 + 1, x2, y2 + 1])
            if x1 > 0:
                if board[x1 - 1][y1] == 0 and board[x2 - 1][y2] == 0:
                    if [x1 - 1, y1, x2 - 1, y2] not in visited:
                        queue.append([x1 - 1, y1, x2 - 1, y2, value + 1])
                        visited.append([x1 - 1, y1, x2 - 1, y2, value + 1])
                    if [x1 - 1, y1, x2, y2 - 1] not in visited:
                        queue.append([x1 - 1, y1, x2, y2 - 1, value + 1]) # rotate |0
                        visited.append([x1 - 1, y1, x2, y2 - 1])
                    if [x1 - 1, y1 + 1, x2, y2] not in visited:
                        queue.append([x1 - 1, y1 + 1, x2, y2, value + 1]) # rotate 0
                        visited.append([x1 - 1, y1 + 1, x2, y2])
            if x1 < n - 1:
                if board[x1 + 1][y1] == 0 and board[x2 + 1][y2] == 0:
                    if [x1 + 1, y1, x2 + 1, y2] not in visited:
                        queue.append([x1 + 1, y1, x2 + 1, y2, value + 1])
                        visited.append([x1 + 1, y1, x2 + 1, y2])
                    if [x1, y1, x2 + 1, y2 - 1] not in visited:
                        queue.append([x1, y1, x2 + 1, y2 - 1, value + 1]) # rotate |0
                        visited.append([x1, y1, x2 + 1, y2 - 1])
                    if [x1, y1 + 1, x2 + 1, y2] not in visited:
                        queue.append([x1, y1 + 1, x2 + 1, y2, value + 1]) # rotate 0|
                        visited.append([x1, y1 + 1, x2 + 1, y2])
        elif y1 == y2:
            if y1 > 0:
                if board[x1][y1 - 1] == 0 and board[x2][y2 - 1] == 0:
                    if [x1, y1 - 1, x2, y2 - 1] not in visited:
                        queue.append([x1, y1 - 1, x2, y2 - 1, value + 1])
                        visited.append([x1, y1 - 1, x2, y2 - 1])
                    if [x1, y1 - 1, x2 - 1, y2] not in visited:
                        queue.append([x1, y1 - 1, x2 - 1, y2, value + 1])   # rotate --
                        visited.append([x1, y1 - 1, x2 - 1, y2]) # rotate 00
                    if [x1 + 1, y1 - 1, x2, y2] not in visited:
                        queue.append([x1 + 1, y1 - 1, x2, y2, value + 1])   # rotate 00
                        visited.append([x1 + 1, y1 - 1, x2, y2]) # rotate --
            if y1 < n - 1:
                if board[x1][y1 + 1] == 0 and board[x2][y2 + 1] == 0:
                    if [x1, y1 + 1, x2, y2 + 1] not in visited:
                        queue.append([x1, y1 + 1, x2, y2 + 1, value + 1])
                        visited.append([x1, y1 + 1, x2, y2 + 1])
                    if [x1, y1, x2 - 1, y2 + 1] not in visited:
                        queue.append([x1, y1, x2 - 1, y2 + 1, value + 1])   # rotate --
                        visited.append([x1, y1, x2 - 1, y2 + 1]) # rotate 00
                    if [x1 + 1, y1, x2, y2 + 1] not in visited:
                        queue.append([x1 + 1, y1, x2, y2 + 1, value + 1])   # rotate 00
                        visited.append([x1 + 1, y1, x2, y2 + 1]) # rotate --
            if x1 > 0:
                if board[x1 - 1][y1] == 0 and [x1 - 1, y1, x2 - 1, y2] not in visited:
                    queue.append([x1 - 1, y1, x2 - 1, y2, value + 1])
                    visited.append([x1 - 1, y1, x2 - 1, y2])
            if x2 < n - 1:
                if board[x2 + 1][y2] == 0 and [x1 + 1, y1, x2 + 1, y2] not in visited:
                    queue.append([x1 + 1, y1, x2 + 1, y2, value + 1])
                    visited.append([x1 + 1, y1, x2 + 1, y2])

def solution(board):
    answer = len(board) * 2 + 1
    answer = BFS(board, 0, answer, len(board))
    return answer
