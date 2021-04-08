def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    t = 0
    while True:
        if truck_weights == []:
            while True:
                if bridge == [] or sum(bridge) == 0:
                    break
                bridge.pop(0)
                t = t + 1
            break
        bridge.pop(0)
        if sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)
        t = t + 1
    answer = t
    return answer
