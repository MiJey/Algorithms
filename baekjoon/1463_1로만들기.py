n = int(input())

# dp[n]: n이 되기 위해 사용하는 연산 횟수의 최솟값
# 0번째는 계산을 편하게 하기 위해 비워둔 공간
dp = [0] * (n + 1)
dp[2] = 1
dp[3] = 1

if n <= 3:
    print(dp[n])
    exit()

for i in range(4, n + 1):
    # 1을 뺀다
    candidate = [dp[i - 1]]

    # x가 3으로 나누어 떨어지면 3으로 나눈다
    if i % 3 == 0:
        candidate.append(dp[i // 3])

    # x가 2로 나누어 떨어지면 2로 나눈다
    if i % 2 == 0:
        candidate.append(dp[i // 2])

    # 바로 직전에 제일 적은 횟수 + 1
    dp[i] = min(candidate) + 1

print(dp[n])
