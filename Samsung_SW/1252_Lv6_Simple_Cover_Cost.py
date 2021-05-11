from operator import itemgetter

def count_holes(st_x, st_y, plate_size):
    global matrix
    count = 0
    for x in range(st_x, st_x + plate_size):
        count += matrix[x][st_y:st_y + plate_size].count(1)
    return count

def find_largest_coverage(st_x, st_y, size, plate_size):
    global matrix
    max_count, max_x, max_y = 0, 0, 0
    for x in range(st_x, st_x + size - plate_size + 1):
        for y in range(st_y, st_y + size - plate_size + 1):
            count = count_holes(x, y, plate_size)
            if max_count < count:
                max_count = count
                max_x = x
                max_y = y
    return max_count, max_x, max_y

def convert(st_x, st_y, plate_size, origin, converting):
    global matrix
    for x in range(st_x, st_x + plate_size):
        for y in range(st_y, st_y + plate_size):
            if matrix[x][y] == origin:
                matrix[x][y] = converting

def cover_cost(st_x, st_y, size, plate_size):
    global matrix
    global costs
    global answer
    print(matrix)
    while True:
        max_count, max_x, max_y = find_largest_coverage(st_x, st_y, size, plate_size)
        print(max_count, max_x, max_y)
        if max_count == 0:
            break
        if plate_size == 3:
            if max_count > 5:
                answer.append([max_x, max_y, plate_size])
                convert(max_x, max_y, plate_size, 1, 2)
            elif max_count > 2:
                point1 = count_holes(max_x, max_y, 2)
                point2 = count_holes(max_x, max_y + 1, 2)
                point3 = count_holes(max_x + 1, max_y, 2)
                point4 = count_holes(max_x + 1, max_y + 1, 2)
                max_p = max(point1, point2, point3, point4)
                if max_p == point1:
                    convert(max_x, max_y, 2, 1, 3)
                    count = count_holes(max_x, max_y, 3)
                    if costs[3] > costs[2] + costs[1] * count:
                        for y in range(max_y, max_y + 3):
                            count, _, _ = find_largest_coverage(max_x + 2, y, 1, 1)
                            if count == 1:
                                answer.append([max_x + 2, y, 1])
                        for x in range(max_x, max_x + 3):
                            count, _, _ = find_largest_coverage(x, max_y + 2, 1, 1)
                            if count == 1:
                                answer.append([x, max_y + 2, 1])
                        answer.append([max_x, max_y, 2])
                        convert(max_x, max_y, 3, 1, 2)
                        convert(max_x, max_y, 2, 3, 2)
                    else:
                        answer.append([max_x, max_y, 3])
                        convert(max_x, max_y, 2, 3, 1)
                        convert(max_x, max_y, 3, 1, 2)
                elif max_p == point2:
                    convert(max_x, max_y + 1, 2, 1, 3)
                    count = count_holes(max_x, max_y, 3)
                    if costs[3] > costs[2] + costs[1] * count:
                        for y in range(max_y, max_y + 3):
                            count, _, _ = find_largest_coverage(max_x + 2, y, 1, 1)
                            if count == 1:
                                answer.append([max_x + 2, y, 1])
                        for x in range(max_x, max_x + 3):
                            count, _, _ = find_largest_coverage(x, max_y, 1, 1)
                            if count == 1:
                                answer.append([x, max_y, 1])
                        answer.append([max_x, max_y + 1, 2])
                        convert(max_x, max_y, 3, 1, 2)
                        convert(max_x, max_y + 1, 2, 3, 2)
                    else:
                        answer.append([max_x, max_y, 3])
                        convert(max_x, max_y, 2, 3, 1)
                        convert(max_x, max_y, 3, 1, 2)
                elif max_p == point3:
                    convert(max_x + 1, max_y, 2, 1, 3)
                    count = count_holes(max_x, max_y, 3)
                    if costs[3] > costs[2] + costs[1] * count:
                        for y in range(max_y, max_y + 3):
                            count, _, _ = find_largest_coverage(max_x, y, 1, 1)
                            if count == 1:
                                answer.append([max_x, y, 1])
                        for x in range(max_x, max_x + 3):
                            count, _, _ = find_largest_coverage(x, max_y + 2, 1, 1)
                            if count == 1:
                                answer.append([x, max_y + 2, 1])
                        answer.append([max_x + 1, max_y, 2])
                        convert(max_x, max_y, 3, 1, 2)
                        convert(max_x + 1, max_y, 2, 3, 2)
                    else:
                        answer.append([max_x, max_y, 3])
                        convert(max_x, max_y, 2, 3, 1)
                        convert(max_x, max_y, 3, 1, 2)
                elif max_p == point4:
                    convert(max_x + 1, max_y + 1, 2, 1, 3)
                    count = count_holes(max_x, max_y, 3)
                    if costs[3] > costs[2] + costs[1] * count:
                        for y in range(max_y, max_y + 3):
                            count, _, _ = find_largest_coverage(max_x, y, 1, 1)
                            if count == 1:
                                answer.append([max_x, y, 1])
                        for x in range(max_x, max_x + 3):
                            count, _, _ = find_largest_coverage(x, max_y, 1, 1)
                            if count == 1:
                                answer.append([x, max_y, 1])
                        answer.append([max_x + 1, max_y + 1, 2])
                        convert(max_x, max_y, 3, 1, 2)
                        convert(max_x + 1, max_y + 1, 2, 3, 2)
                    else:
                        answer.append([max_x, max_y, 3])
                        convert(max_x, max_y, 2, 3, 1)
                        convert(max_x, max_y, 3, 1, 2)
            else:
                for x in range(st_x, st_x + 3):
                    for y in range(st_y, st_y + 3):
                        if matrix[x][y] == 1:
                            matrix[x][y] = 2
                            answer.append([x, y, 1])
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    S = int(input())
    N = int(input())
    points = list(map(int,input().split()))
    matrix = []
    for i in range(S):
        matrix.append([0]*S)
    costs = [0, 2, 4, 7]
    answer = []
    for i in range(N):
        matrix[points[i*2] - 1][points[i*2+1] - 1] = 1
    cover_cost(0, 0, S, 3)
    answer = sorted(answer, key=itemgetter(1), reverse=False)
    print("#%d " % (test_case),end='')
    for i in range(len(answer)):
        print('%d %d %d ' % (answer[i][0], answer[i][1], answer[i][2]), end='')
    print()
    # ///////////////////////////////////////////////////////////////////////////////////

