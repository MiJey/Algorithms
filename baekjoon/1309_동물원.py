n = int(input())
dp = [0] * (n + 2)

dp[1] = 1
dp[2] = 3   # 첫 번째에 사자를 넣을 수 있는 경우의 수

if n < 2:
    print(dp[n + 1])
    exit()

for i in range(3, n + 2):
    dp[i] = (dp[i - 1] * 2 + dp[i - 2]) % 9901

print(dp[n + 1])
