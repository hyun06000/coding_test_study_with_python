def solution(bridge_length, weight, truck_weights):
    on_bridge = [0] * bridge_length
    tic = 0

    while on_bridge:
        on_bridge.pop(0)
        if truck_weights:
            if sum(on_bridge) + truck_weights[0] > weight:
                on_bridge.append(0)
            else:
                on_bridge.append(truck_weights.pop(0))

        tic += 1

    return tic