def LCS(X, Y, N):
    global dp
    max_dp = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = max(dp[i-1][j - 1] + 1, dp[i - 1][j])
                if max_dp < dp[i][j]:
                    max_dp = dp[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return float(max_dp/N*100)
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    X = input()
    Y = input()
    dp = []
    for i in range(N + 1):
        dp.append([0]*(N+1))
    lcs = LCS(X, Y, N)
    print("#%d %.2f" % (test_case, lcs))
    # ///////////////////////////////////////////////////////////////////////////////////

