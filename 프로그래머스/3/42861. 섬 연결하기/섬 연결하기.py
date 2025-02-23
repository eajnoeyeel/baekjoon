def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x : x[2])
    linked = {costs[0][0]}
    
    while len(linked) != n:
        for bridge in costs:
            if bridge[0] in linked and bridge[1] in linked:
                continue
            if bridge[0] in linked or bridge[1] in linked:
                linked.update([bridge[0], bridge[1]])
                answer += bridge[2]
                break

    return answer
