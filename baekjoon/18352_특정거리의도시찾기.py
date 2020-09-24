import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
node = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b)

# x에서 출발하는 다익스트라
min_dist = [-1] * (n + 1)
min_dist[x] = 0

# 다익스트라 탐색을 deque를 이용한 BFS로 구현
q = deque()
q.append(x)

while q:
    current = q.popleft()
    for next in node[current]:
        if min_dist[next] == -1:
            min_dist[next] = min_dist[current] + 1
            q.append(next)

# 최단거리가 k인 도시를 오름차순으로 출력
flag = True
for i in range(n + 1):
    if min_dist[i] == k:
        print(i)
        flag = False

if flag:
    print(-1)
