matrix = []
visited = []
total_cost = 999999999999
def minimal_cost(origin, cost, visited_count):
    global matrix
    global visited
    global total_cost
    if visited_count == 0:
        cost += matrix[origin][1]
        if total_cost > cost:
            total_cost = cost
    else:
        for i in range(2, len(matrix)):
            if visited[i]:
                continue
            if cost + matrix[origin][i] > total_cost:
                continue
            visited[i] = True
            minimal_cost(i, cost + matrix[origin][i], visited_count - 1)
            visited[i] = False
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    matrix = []
    visited = []
    total_cost = 999999999999
    N = int(input())
    custom = input().split()
    custom_list = []
    for i in range(0,len(custom),2):
        custom_list.append([int(custom[i]), int(custom[i+1])])
    for i in range(0,len(custom_list)):
        tmp = []
        for j in range(0, i):
            tmp.append(matrix[j][i])
        tmp.append(0)
        for j in range(i + 1,len(custom_list)):
            tmp.append(abs(custom_list[i][0] - custom_list[j][0]) + abs(custom_list[i][1] - custom_list[j][1]))
        matrix.append(tmp)
        visited.append(False)
    for i in range(2,len(custom_list)):
        visited[i] = True
        visited_count = len(custom_list) - 3
        minimal_cost(i, matrix[0][i], visited_count)
        visited[i] = False
    print('#%d %d' % (test_case, total_cost))
    # ///////////////////////////////////////////////////////////////////////////////////

