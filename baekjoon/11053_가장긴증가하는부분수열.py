import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N
result = 0

for i in range(1, N):
    # 내가 꼬리로 붙을 수 있는 부분 수열 찾기 -> 그 중 가장 긴걸 선택
    for j in range(i):
        # 이전 꼬리가 나보다 숫자가 작아야 함
        # 이전 꼬리의 길이가 최소한 같아야 +1 해서 길어질 수 있음
        if arr[j] < arr[i] and dp[j] >= dp[i]:
            dp[i] = dp[j] + 1

    if dp[i] > result:
        result = dp[i]

print(result)
