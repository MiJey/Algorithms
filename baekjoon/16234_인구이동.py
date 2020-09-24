import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline


def check_border(land, checked, updated, l, r, before, total, count, i, j):
    if i < 0 or i >= len(land) or j < 0 or j >= len(land[0]) or checked[i][j] or updated[i][j]:
        return total, 0

    if not (l <= abs(before - land[i][j]) <= r):
        return total, 0

    checked[i][j] = True

    t4, c4 = check_border(land, checked, updated, l, r, land[i][j], total, count + 1, i, j + 1)
    t2, c2 = check_border(land, checked, updated, l, r, land[i][j], total, count + 1, i + 1, j)
    t3, c3 = check_border(land, checked, updated, l, r, land[i][j], total, count + 1, i, j - 1)
    t1, c1 = check_border(land, checked, updated, l, r, land[i][j], total, count + 1, i - 1, j)

    return (total + land[i][j] + t1 + t2 + t3 + t4), c1 + c2 + c3 + c4 + 1


def update_population(land, checked, updated, population, i, j):
    if i < 0 or i >= len(land) or j < 0 or j >= len(land[0]) or updated[i][j] or (not checked[i][j]):
        return

    land[i][j] = population
    updated[i][j] = True

    update_population(land, checked, updated, population, i, j + 1)
    update_population(land, checked, updated, population, i + 1, j)
    update_population(land, checked, updated, population, i, j - 1)
    update_population(land, checked, updated, population, i - 1, j)


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
            total, count = check_border(land, checked, updated, l, r, l + land[i][j], 0, 0, i, j)

            if count > 1:
                average = total // count
                update_population(land, checked, updated, average, i, j)
                today += 1

    if today == 0:
        break

    result += 1

print(result)
