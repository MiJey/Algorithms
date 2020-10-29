import sys

input = sys.stdin.readline

n = int(input())

# 0~3: 뱀(방향), -1: 아무것도 없음, -2: 사과
board = [[-1] * n for _ in range(n)]
board[0][0] = 0

# → ↑ ← ↓
directions = [[0, -1, 0, 1], [1, 0, -1, 0]]
cur = 0
head = [0, 0]
tail = [0, 0]

t = 0
count = 0

for _ in range(int(input())):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = -2

# for i in range(n):
#     print(board[i])

change_direction = dict()
for _ in range(int(input())):
    x, c = input().split()
    change_direction[int(x)] = c

while True:
    count += 1
    # print("count", count)

    # 다음 칸 좌표
    head = [head[0] + directions[0][cur], head[1] + directions[1][cur]]

    # 벽에 부딪힌 경우, 자기 몸에 부딪힌 경우
    if head[0] < 0 or head[0] >= n or head[1] < 0 or head[1] >= n \
            or board[head[0]][head[1]] >= 0:
        print(count)
        exit()

    next_cell = board[head[0]][head[1]]

    # 일단 머리가 늘어남
    board[head[0]][head[1]] = cur

    # 사과가 없는 경우 꼬리가 줄어듬
    if next_cell != -2:
        next_tail_dir = board[tail[0]][tail[1]]
        board[tail[0]][tail[1]] = -1
        tail[0] += directions[0][next_tail_dir]
        tail[1] += directions[1][next_tail_dir]

    if count in change_direction:
        if change_direction[count] == "L":
            # 왼쪽 회전
            cur = (cur + 1) % 4
        else:
            # 오른쪽 회전
            cur -= 1
            if cur < 0:
                cur = 3

    board[head[0]][head[1]] = cur

    # for i in range(n):
    #     print(board[i])
    # print("----------")
