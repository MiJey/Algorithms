# 주유소가 있는 마을과 주유소가 없는 마을이 있다.
# 주유소가 없는 마을에서는 가장 가까운 주유소가 있는 마을로 가야한다.
# 주유소가 없는 마을 중 하나에 새로운 주유소를 만들려고 한다.
# 가장 멀리서 오는 거리가 최소가 되도록 하는 마을을 찾아라.

# input
# 주유소 수(<=100), 마을 수(<=500)
# 주유소가 있는 마을 번호
# 마을 사이 도로의 거리

# output
# 새로 주유소를 만들 마을의 번호(여러개가 있다면 가장 작은 번호)

# 예시 1
# input
# 1 4
# 1
# 1 2 10
# 2 3 10
# 2 4 15
# output
# 2

# 예시 2
# input
# 1 7
# 2
# 1 2 10
# 2 3 10
# 3 4 10
# 4 5 10
# 5 6 10
# 6 7 10
# 7 1 10
# output
# 4
import sys
from collections import deque

input = sys.stdin.readline

# m: 주유소 개수
# n: 마을 개수
m, n = map(int, input().split())

# 주유소이 있으면 True(0번째 버림)
# ex) 주유소 있는 마을: [False, True, True, False, False]
town = [False for _ in range(n + 1)]
for _ in range(m):
    town[int(input())] = True

# 다익스트라 알고리즘을 위한 간선 리스트(0번째는 쓰지 않음)
# ex) node [[], [[2, 10]], [[1, 10], [3, 10], [4, 15]], [[2, 10]], [[2, 15]]]
# ex) node[1]: [[2, 3], [4, 5]] => 거리가 3인 1->2, 거리가 5인 1->4
node = [[] for _ in range(n + 1)]

# 입력이 끝날 때까지 받음
while True:
    try:
        # a->b 간선에 가중치 distance
        a, b, distance = map(int, input().split())
        node[a].append([b, distance])
        node[b].append([a, distance])   # 방향이 없기 때문에 a->b, b->a 모두 추가
    except:
        break

# ex) [[], [[2, 10]], [[1, 10], [3, 10], [4, 15]], [[2, 10]], [[2, 15]]]
print("node", node)

# 주유소를 하나씩 추가하면서 가장 가까운 주유소까지의 거리를 찾음
max_dist_list = []  # 거리, 주유소 오픈할 마을 넘버
# ex) max_dist_list [[15, 2], [25, 3], [20, 4]]

for new_gas in range(1, n + 1):
    # 이미 주유소가 있는 마을은 패스
    if town[new_gas]:
        continue

    # new_gas번 마을에 주유소을 추가
    town[new_gas] = True

    # new_gas번 마을에 주유소을 추가했을 때 주유소에서 가장 먼 마을의 거리
    max_dist = 0

    # x에서 출발하는 다익스트라
    for x in range(1, n + 1):
        min_dist_gas = [99999] * (n + 1)    # 가장 가까운 주유소까지 거리
        if town[x]:                         # 시작 지점에 주유소가 있는 경우
            min_dist_gas[x] = 0

        # 여기서부터 진짜 다익스트라 시작
        min_dist = [-1] * (n + 1)   # -1: 아직 방문하지 않음
        min_dist[x] = 0             # 시작 지점

        # 다익스트라 탐색을 deque를 이용한 BFS로 구현
        q = deque()
        q.append(x)

        while q:
            current = q.popleft()

            for next_node, weight in node[current]:
                if min_dist[next_node] == -1:
                    min_dist[next_node] = min_dist[current] + weight
                    q.append(next_node)

                    # 주유소가 있는 마을까지의 거리는 따로 저장
                    # ex) 다른 마을까지 거리: [-1, 0, 10, 20, 25]
                    # ex) 다른 주유소까지 거리: [99999, 0, 10, 99999, 99999]
                    if town[next_node]:
                        min_dist_gas[next_node] = min_dist[current] + weight

        # 다익스트라 끝
        print("----------")
        print(x, "번 마을에서 다른 마을까지 거리:", min_dist)    # [-1, 0, 10, 20, 25]
        print(x, "번 마을에서 다른 주유소까지 거리:", min(min_dist_gas), min_dist_gas)  # [99999, 0, 10, 99999, 99999]

        # 주유소에서 가장 먼 거리 저장
        max_dist = max(max_dist, min(min_dist_gas))

    # 가장 먼 거리와 주유소 오픈할 마을 넘버 저장
    max_dist_list.append([max_dist, new_gas])

    # new_gas번 마을에 주유소 추가한거 되돌리기
    town[new_gas] = False

print("==================")
# 거리 순 정렬 -> 가장 먼 거리가 작아지는 마을에 주유소 오픈!
max_dist_list = sorted(max_dist_list, key=lambda x: x[0])   # ex) max_dist_list [[15, 2], [20, 4], [25, 3]]
print("주유소 오픈할 마을 넘버:", max_dist_list[0][1])
