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


# (0, 0)에서 (m-1, n-1)까지 내리막길만 가는 방법
# 이유는 모르겠지만 이게 더 빠름(180ms)
def dfs_from_start(x, y):
    if x == m - 1 and y == n - 1:
        return 1

    if visit[x][y] == -1:
        visit[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n \
                    and matrix[nx][ny] < matrix[x][y]:  # 내리막
                visit[x][y] += dfs_from_start(nx, ny)

    return visit[x][y]


# (m-1, n-1)에서 (0, 0)까지 오르막길만 가는 방법(역주행)
# 이유는 모르겠지만 이게 더 느림(270ms)
def dfs_from_end(x, y):
    if x == 0 and y == 0:
        return 1

    if visit[x][y] == -1:
        visit[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n \
                    and matrix[nx][ny] > matrix[x][y]:  # 내리막(역주행이니까 오르막)
                visit[x][y] += dfs_from_end(nx, ny)

    return visit[x][y]


print(dfs_from_start(0, 0))
print(dfs_from_end(m - 1, n - 1))
