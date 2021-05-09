T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    k = int(input())
    string = input()
    word_list = []
    for length in range(1, len(string) + 1):
        for index in range(0, len(string) - length + 1):
            word_list.append(string[index:index + length])
    word_list = list(set(word_list))
    word_list.sort()
    if k > len(word_list):
        print("#%d none" % (test_case))
    else:
        print("#%d %s" % (test_case, word_list[k - 1]))
    # ///////////////////////////////////////////////////////////////////////////////////

