def gcd(p, q):
    if p < q:
        return gcd(q, p)
    elif q == 0:
        return p
    return gcd(q, p % q)

def shoot(idx, N):
    global robots
    global dp
    global dp_diff
    count = 0
    shoot_list = []
    x_up_line = False
    x_down_line = False
    y_right_line = False
    y_left_line = False
    for i in range(N):
        if idx == i:
            continue
        if dp[idx][i] == 0:
            x = robots[idx][0] - robots[i][0]
            y = robots[idx][1] - robots[i][1]
            if x == 0 or y == 0:
                dp[idx][i] = [x, y]
                dp[i][idx] = [-x, -y]
            else:
                g = gcd(abs(x), abs(y))
                dp[idx][i] = [x/g, y/g]
                dp[i][idx] = [-x/g, -y/g]
        x = dp[idx][i][0]
        y = dp[idx][i][1]
        if x == 0:
            if y > 0 and y_left_line == False:
                shoot_list.append([x, y])
                y_left_line = True
            elif y < 0 and y_right_line == False:
                shoot_list.append([x, y])
                y_right_line = True
        elif y == 0:
            if x > 0 and x_down_line == False:
                shoot_list.append([x, y])
                x_down_line = True
            elif x < 0 and x_up_line == False:
                shoot_list.append([x, y])
                x_up_line = True
        else:
            if [x, y] not in shoot_list:
                shoot_list.append([x, y])
    return len(shoot_list)

def second_problem(A, N, K):
    A = A + [0] * N
    C = []
    for i in range(N):
        for j in range(N):
            A[j] = ((A[j] * K + (j + 1)) % N) + 1
            A[N + j] = ((A[j] * (j + 1) + K) % N) + 1
        A.sort()
        B = 1
        for j in range(1, 2*N + 1):
            B = ((B * A[j - 1] + j) % N) + 1
        C.append(B)
    return sum(C)
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    R, N, K = map(int,input().split())
    robots = []
    dp = []
    dp_diff = {}
    for i in range(N):
        x, y = map(int,input().split())
        robots.append([x,y])
        dp.append([0] * (N + 1))
    dp.append([0] * (N + 1))
    A = []
    for i in range(N):
        shooted = shoot(i, N)
        A.append(shooted)
    A2 = A
    C = second_problem(A2, N, K)
    print('#%d %d %d' % (test_case, sum(A), C))
    # ///////////////////////////////////////////////////////////////////////////////////

