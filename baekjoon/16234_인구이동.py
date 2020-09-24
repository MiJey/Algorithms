import sys
from collections import deque

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def check_border(land, checked, updated, l, r, i, j):
    total = land[i][j]
    count = 1
    checked[i][j] = True

    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < len(land) and 0 <= ny < len(land[0]) \
                    and not updated[nx][ny] \
                    and not checked[nx][ny] \
                    and l <= abs(land[nx][ny] - land[x][y]) <= r:
                q.append((nx, ny))
                checked[nx][ny] = True
                total += land[nx][ny]
                count += 1

    return total, count


def update_population(land, checked, updated, population, i, j):
    land[i][j] = population
    updated[i][j] = True

    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < len(land) and 0 <= ny < len(land[0]) \
                    and checked[nx][ny] \
                    and not updated[nx][ny]:
                q.append((nx, ny))
                land[nx][ny] = population
                updated[nx][ny] = True


n, l, r = map(int, input().split())
result = 0
land = []

for _ in range(n):
    land.append(list(map(int, input().split())))

while True:
    today = 0
    updated = [[False] * len(land[0]) for _ in range(len(land))]

    for i in range(len(land)):
        for j in range(len(land[0])):
            if updated[i][j]:
                continue

            checked = [[False] * len(land[0]) for _ in range(len(land))]
            total, count = check_border(land, checked, updated, l, r, i, j)

            if count > 1:
                average = total // count
                update_population(land, checked, updated, average, i, j)
                today += 1

    if today == 0:
        break

    result += 1

print(result)
