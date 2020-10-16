# 미해결
import sys

input = sys.stdin.readline


def movement(land, visited, l, r, before, sumPopulation, i, j):
    if i < 0 or i >= len(land) or j < 0 or j >= len(land[0]) or visited[i][j]:
        return sumPopulation

    if not (l <= abs(before - land[i][j]) <= r):
        return sumPopulation

    visited[i][j] = True

    return sumPopulation + land[i][j] \
           + movement(land, visited, l, r, land[i][j], sumPopulation, i, j) \
           + movement(land, visited, l, r, land[i][j], sumPopulation, i, j - 1) \
           + movement(land, visited, l, r, land[i][j], sumPopulation, i, j + 1) \
           + movement(land, visited, l, r, land[i][j], sumPopulation, i - 1, j) \
           + movement(land, visited, l, r, land[i][j], sumPopulation, i - 1, j - 1) \
           + movement(land, visited, l, r, land[i][j], sumPopulation, i - 1, j + 1) \
           + movement(land, visited, l, r, land[i][j], sumPopulation, i + 1, j) \
           + movement(land, visited, l, r, land[i][j], sumPopulation, i + 1, j - 1) \
           + movement(land, visited, l, r, land[i][j], sumPopulation, i + 1, j + 1)


n, l, r = map(int, input().split())
result = 0
land = []

for _ in range(n):
    land.append(list(map(int, input().split())))

visited = [[False] * len(land[0]) for _ in range(len(land))]

print("sum of population:", movement(land, visited, l, r, l + land[0][0], 0, 0, 0))

for i in range(len(land)):
    print(land[i])

for i in range(len(land)):
    print(visited[i])
