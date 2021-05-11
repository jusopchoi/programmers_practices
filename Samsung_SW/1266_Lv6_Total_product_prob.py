facto = [1]
for f in range(1, 19):
    facto.append(facto[-1]*f)
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    percent_a, percent_b = map(int, input().split())
    percent_a = float(percent_a)/100.0
    percent_b = float(percent_b)/100.0
    prime = [2, 3, 5, 7, 11, 13, 17]
    total_a = 0.0
    total_b = 0.0
    for p in prime:
        total_a += facto[18]/(facto[18-p]*facto[p])*pow(percent_a,p)*pow(1-percent_a,18-p)
        total_b += facto[18]/(facto[18-p]*facto[p])*pow(percent_b,p)*pow(1-percent_b,18-p)
    print('#%d %0.6f' % (test_case, total_a + total_b - total_a*total_b))
    # ///////////////////////////////////////////////////////////////////////////////////

