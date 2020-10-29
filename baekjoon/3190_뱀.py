import sys

input = sys.stdin.readline

# 뱀 방향 → ↑ ← ↓
directions = [[0, -1, 0, 1], [1, 0, -1, 0]]
cur = 0

# 뱀 머리, 꼬리 좌표
head = [0, 0]
tail = [0, 0]

# 0~3: 뱀 방향, -1: 아무것도 없음, -2: 사과
n = int(input())
board = [[-1] * n for _ in range(n)]
board[0][0] = 0

# 시간(초)
time = 0


def print_board():
    print("PLAY TIME:", time)

    for i in range(n):
        for j in range(n):
            if board[i][j] == -1:
                print("□", end='')
            elif board[i][j] == -2:
                print("♥", end='')
            elif board[i][j] == 0:
                print("▶", end='')
            elif board[i][j] == 1:
                print("▲", end='')
            elif board[i][j] == 2:
                print("◀", end='')
            elif board[i][j] == 3:
                print("▼", end='')
        print()

    for _ in range(n):
        print("―", end='')

    print()


# 사과 위치
for _ in range(int(input())):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = -2

# print_board()

# x초에 방향 회전 정보
change_direction = dict()

for _ in range(int(input())):
    x, c = input().split()
    change_direction[int(x)] = c

while True:
    time += 1

    # 다음 칸 좌표
    head = [head[0] + directions[0][cur], head[1] + directions[1][cur]]

    # 벽에 부딪힌 경우, 자기 몸에 부딪힌 경우
    if head[0] < 0 or head[0] >= n or head[1] < 0 or head[1] >= n \
            or board[head[0]][head[1]] >= 0:
        print(time)
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

    # x초에 방향 회전
    if time in change_direction:
        if change_direction[time] == "L":
            # 왼쪽 회전
            cur = (cur + 1) % 4
        else:
            # 오른쪽 회전
            cur -= 1
            if cur < 0:
                cur = 3

    board[head[0]][head[1]] = cur

    # print_board()
