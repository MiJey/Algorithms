def solution(N, stages):
    count = [0] * (N + 2)
    failure_rate = dict()

    # 예시1: [0, 1, 3, 2, 1, 0, 1]
    # 예시2: [0, 0, 0, 0, 5, 0]
    for stage in stages:
        count[stage] += 1

    # 예시1: {1: 0.125, 2: 0.42857142857142855, 3: 0.5, 4: 0.5, 5: 0.0}
    # 예시2: {1: 0.0, 2: 0.0, 3: 0.0, 4: 1.0}
    challenger_count = len(stages)

    for i in range(1, N + 1):
        challenger_count -= count[i - 1]

        if challenger_count == 0:
            failure_rate[i] = 0
        else:
            failure_rate[i] = count[i] / challenger_count

    # 예시1: [3, 4, 2, 1, 5]
    # 예시2: [4, 1, 2, 3]
    return sorted(failure_rate, key=lambda x: failure_rate[x], reverse=True)


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))  # [3,4,2,1,5]
print(solution(4, [4, 4, 4, 4, 4]))  # [4,1,2,3]
