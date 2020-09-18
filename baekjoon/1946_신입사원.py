import sys
input = sys.stdin.readline

# 1. 서류 점수를 기준으로 정렬
# 2. 서류 점수 1등을 제외하면 다른 사람들은 모두 면접 점수로 승부를 봐야함
# 3. 서류 점수 1등의 면접 점수를 커트라인으로 정함
# 4. 새로운 합격자의 면접 점수가 커트라인보다 높으면 이제 이 사람이 서류 점수 1등인 사람인 셈 치고 커트라인 조정
#
# 예시
# 0 1 2 3 4 5 6
# 0 6 3 5 1 2 4
#   ↑ 커트라인을 6으로 설정
#     ↑ 새로운 커트라인 기준(6 -> 3), result += 1
#       ↑ 새로운 커트라인에 안맞음
#         ↑ 새로운 커트라인 기준(3 -> 1), result += 1
#           ↑ 새로운 커트라인에 안맞음
#             ↑ 새로운 커트라인에 안맞음

for _ in range(int(input())):
    n = int(input())
    newcomers = [0] * (n + 1)

    for _ in range(n):
        a, b = map(int, input().split())
        newcomers[a] = b

    cutLine = newcomers[1]
    result = 0

    for i in range(1, n + 1):
        if newcomers[i] <= cutLine:
            cutLine = newcomers[i]
            result += 1

    print(result)
