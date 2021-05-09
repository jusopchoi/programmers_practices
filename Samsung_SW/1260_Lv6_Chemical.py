dp = {}
def minimal_cost(cross, st, ed):
    global dp
    min_value = 999999999999
    for i in range(st, ed):
        if str(st) + str(i) not in dp:
            minimal_cost(cross, st, i)
        if str(i + 1) + str(ed) not in dp:
            minimal_cost(cross, i+1, ed)
        value = dp[str(st) + str(i)][1][0] * dp[str(st) + str(i)][1][1] * dp[str(i + 1) + str(ed)][1][1]
        value += dp[str(st) + str(i)][0] + dp[str(i + 1) + str(ed)][0]
        if value < min_value:
            min_value = value
    dp[str(st) + str(ed)] = [min_value, [cross[st][0], cross[ed][1]]]
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    matrix = []
    for i in range(N):
        tmp = input().split()
        matrix.append(tmp)
    cross = {}
    min_value = 99999999999
    start = []
    end = []
    dp = {}
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != '0':
                y = 0
                while j + y < N and matrix[i][j + y] != '0':
                    matrix[i][j + y] = '0'
                    y += 1
                x = 1
                while i + x < N and matrix[i + x][j] != '0':
                    matrix[i + x] = matrix[i + x][:j] + ['0'] * y + matrix[i + x][j + y:]
                    x += 1
                cross[x] = y
                start.append(x)
                end.append(y)
    st = list(set(start)-set(end))[0]
    cross_list = []
    while st in cross:
        cross_list.append([st, cross[st]])
        st = cross[st]
    for i in range(len(cross_list)):
        dp[str(i) + str(i)] = [0, [cross_list[i][0], cross_list[i][1]]]
    if '0' + str(len(cross_list) - 1) not in dp:
        minimal_cost(cross_list, 0, len(cross_list) - 1)
    print('#%d %d' % (test_case, dp['0' + str(len(cross_list) - 1)][0]))
    # ///////////////////////////////////////////////////////////////////////////////////

