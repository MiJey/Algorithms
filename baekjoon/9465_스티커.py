import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())    # 여기서 미리 2를 더할 수도 있지만 헷갈릴 것 같아서 냅둠
    matrix = [list(map(int, input().split())), list(map(int, input().split()))]
    dp = [[0] * (n + 2) for _ in range(2)]

    # 대각선, 한 열 건너뛴 대각선으로만 갈 수 있음
    # 두 열 건너뛰는 대각선은 그냥 대각선 두번이라 의미 없음
    for i in range(2, n + 2):
        dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + matrix[0][i - 2]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + matrix[1][i - 2]

    print(max(dp[0][n + 1], dp[1][n + 1]))
