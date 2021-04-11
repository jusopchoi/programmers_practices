import heapq    
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        k1 = heapq.heappop(scoville)
        if k1 > K:
            break
        if not scoville:
            answer = -1
            break
        k2 = heapq.heappop(scoville)
        s = k1 + k2 * 2
        heapq.heappush(scoville, s)
        answer += 1
    return answer
