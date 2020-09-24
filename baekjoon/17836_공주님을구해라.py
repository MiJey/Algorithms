import sys
from collections import deque

input = sys.stdin.readline


def bfs(castle, dist):
    q = deque()
    dist[0][0] = 0
    q.append((0, 0))
    sword_location = (-1, -1)

    # BFS로 탐색
    while q:
        x, y = q.popleft()

        if castle[x][y] == 2:
            sword_location = (x, y)

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and castle[nx][ny] != 1 and dist[nx][ny] == -1:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1

    return sword_location


n, m, t = map(int, input().split())
castle = []
dist = [[-1] * m for _ in range(n)]

for _ in range(n):
    castle.append(list(map(int, input().split())))

sx, sy = bfs(castle, dist)          # 칼 위치
princess_dist = dist[n - 1][m - 1]  # 칼 없이 공주에게 가는 최단거리
sword_dist = dist[sx][sy]           # 칼 가지러 가는 최단거리
result = 0

if sword_dist == -1:
    if princess_dist == -1:
        # 칼과 공주에게 가는 길이 모두 막혀있는 경우 Fail
        result = t + 1
    else:
        # 칼은 못가지러 가지만 공주에게는 갈 수 있는 경우
        result = princess_dist
else:
    # 칼 들고 공주에게 가는 최단거리
    sword_princess_dist = sword_dist + (n - 1 - sx) + (m - 1 - sy)

    if princess_dist == -1:
        # 무조건 칼 먼저 가지러 가야하는 경우
        result = sword_princess_dist
    else:
        if sword_princess_dist < princess_dist:
            # 칼을 먼저 가지러 가는게 나은 경우
            result = sword_princess_dist
        else:
            # 칼 냅두고 바로 공주 만나러 가는게 나은 경우
            result = princess_dist

print("Fail" if result > t else result)
