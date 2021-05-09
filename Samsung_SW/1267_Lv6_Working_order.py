iT = 10#int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    V, E = map(int, input().split())
    lists = input().split()
    edges = {}
    index = 0
    nodes = {}
    for i in range(V):
        nodes[str(i + 1)] = 0
    for i in range(0,len(lists),2):
        if lists[i] not in edges:
            edges[lists[i]] = [lists[i+1]]
        else:
            edges[lists[i]].append(lists[i+1])
        nodes[lists[i+1]] += 1
    working_list = []
    while V > len(working_list):
        for n in nodes:
            if n not in working_list and nodes[n] == 0:
                break
        working_list.append(n)
        if n in edges:
            for v in edges[n]:
                nodes[v] -= 1
    print("#%d %s" % (test_case, ' '.join(working_list)))
    # ///////////////////////////////////////////////////////////////////////////////////

