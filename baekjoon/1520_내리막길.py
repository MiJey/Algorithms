import sys

sys.setrecursionlimit(10000)

m, n = map(int, sys.stdin.readline().split())
matrix = []
visit = [[-1] * n for _ in range(m)]

for _ in range(m):
    matrix.append(list(map(int, input().split())))

########################################

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(x, y):
    if x == 0 and y == 0:
        return 1

    if visit[x][y] == -1:
        visit[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n \
                    and matrix[nx][ny] > matrix[x][y]:
                visit[x][y] += dfs(nx, ny)

    return visit[x][y]


print(dfs(m - 1, n - 1))
