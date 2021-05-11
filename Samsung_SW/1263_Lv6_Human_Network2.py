def search(x, child, visited, N, depth):
    global dp
    global edges
    while True:
        tmp_child = []
        while child != []:
            y = child.pop()
            dp[x][y] = depth
            dp[y][x] = depth
            for i in edges[y]:
                if not visited[i]:
                    visited[i] = True
                    tmp_child.append(i)
        if tmp_child == []:
            break
        child = tmp_child
        depth += 1
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    input_list = list(map(int, input().split()))
    N = input_list[0]
    cc = 1001*1001
    edges = {}
    dp = []
    for i in range(N):
        dp.append(input_list[1 + i*N: 1 + (i+1)*N])
        if i not in edges:
            edges[i] = []
        for j in range(N):
            if input_list[1 + i*N + j] == 1:
                edges[i].append(j)
    for i in range(N):
        child = []
        visited = [False] * N
        visited[i] = True
        for j in edges[i]:
            if dp[i][j] > 1:
                continue
            visited[j] = True
            child.append(j)
        search(i, child, visited, N, 1)
        tmp_cc = sum(dp[i])
        if cc > tmp_cc:
            cc = tmp_cc
    print('#%d %d' % (test_case, cc))
    # ///////////////////////////////////////////////////////////////////////////////////

