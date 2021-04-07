def solution(phone_book):
    answer = True
    lengths = {}
    for num1 in phone_book:
        length = len(num1)
        if length in lengths:
            lengths[length][num1] = 0
        else:
            lengths[length] = {num1: 0}
    lengths_sort = list(lengths.keys())
    lengths_sort.sort()
    for num2 in phone_book:
        length_t = len(num2)
        for length in lengths_sort:
            if length >= length_t:
                break
            try:
                lengths[length][num2[:length]] += 1
                return False
            except:
                pass
    return answer
