import heapq as hq
def solution(operations):
    answer = []
    max_queue = []
    min_queue = []
    for op in operations:
        command = op[0]
        value = int(op[2:])
        if command == 'I':
            hq.heappush(max_queue, value)
            hq.heappush(min_queue, -value)
        else:
            if max_queue != []:
                if value > 0:
                    value = hq.heappop(min_queue)
                    max_queue.remove(-value)
                else:
                    value = hq.heappop(max_queue)
                    min_queue.remove(-value)
    if max_queue == []:
        answer = [0, 0]
    else:
        answer = [-hq.heappop(min_queue), hq.heappop(max_queue)]
    return answer
