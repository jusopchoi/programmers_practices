from operator import itemgetter
def binary_search(start, end, lst, N, magnet):
    while True:
        if start >= end:
            return start
        x = (start+end) / 2
        if start == x or x == end:
            return start
        left = 0
        right = 0
        for i in range(N):
            if i < lst:
                left += magnet[i][1]/((x-magnet[i][0])*(x-magnet[i][0]))
            else:
                right += magnet[i][1]/((magnet[i][0] - x) * (magnet[i][0] - x))
        if left > right:
            if left - right <= 0.0000000000001:
                return x
            start = x
        else:
            if right - left <= 0.0000000000001:
                return x
            end = x
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    input_list = input().split()
    magnet = []
    for i in range(N):
        magnet.append([int(input_list[i]), int(input_list[i+N])])
    magnet = sorted(magnet, key=itemgetter(0), reverse=False)
    x_list = []
    for i in range(N - 1):
        x = binary_search(magnet[i][0], magnet[i+1][0], i + 1, N, magnet)
        x_list.append('%.10f' % (x))
    print('#%d %s' % (test_case, ' '.join(x_list)))
    # ///////////////////////////////////////////////////////////////////////////////////

