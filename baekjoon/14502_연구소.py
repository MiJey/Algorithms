import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lab = []
result = 0

for i in range(0, n):
    lab.append(list(map(int, input().split())))

# 벽 개수
lab_size = n * m
wall_area_size = 3

for i in range(0, n):
    for j in range(0, m):
        if lab[i][j] == 1:
            wall_area_size += 1


def get_virus_area_size():
    # 바이러스가 퍼진 영역의 크기 반환
    virus_area = [[0] * m for _ in range(n)]

    def spread_virus(i, j):
        # 벽이면 리턴
        if i < 0 or j < 0 or i >= n or j >= m or lab[i][j] == 1:
            # print("벽이라 리턴", i, j)
            return 0

        # 이미 바이러스가 퍼진 곳이면 리턴
        if virus_area[i][j] == 2:
            # print("이미 바이러스가 퍼져서 리턴", i, j)
            return 0

        # 바이러스 퍼짐
        # print("바이러스 퍼짐", i, j)
        virus_area[i][j] = 2

        return 1 \
            + spread_virus(i - 1, j) \
            + spread_virus(i + 1, j) \
            + spread_virus(i, j - 1) \
            + spread_virus(i, j + 1)


    virus_area_size = 0

    for x in range(0, n):
        for y in range(0, m):
            # 바이러스 시작점부터 퍼트리기
            if lab[x][y] == 2:
                # print("바이러스 시작점부터 퍼트리기", x, y)
                virus_area_size += spread_virus(x, y)

    return virus_area_size


# 벽 3개 브루트포스로 고르기
for x in range(0, m * n - 2):
    # x = i * m + j
    xi = x // n
    xj = x % n

    if lab[xi][xj] != 0:
        continue

    for y in range(x + 1, m * n - 1):
        yi = y // n
        yj = y % n

        if lab[yi][yj] != 0:
            continue

        for z in range(y + 1, m * n):
            zi = z // n
            zj = z % n

            if lab[zi][zj] != 0:
                continue

            # 벽 3개 골랐음
            lab[xi][xj] = 1
            lab[yi][yj] = 1
            lab[zi][zj] = 1

            print("====================")
            print(x, y, z)
            for asdf in range(0, n):
                print(lab[asdf])

            # 안전 영역의 크기 구하기
            safety_area_size = lab_size - wall_area_size - get_virus_area_size()
            print("lab_size", lab_size)
            print("wall_area_size", wall_area_size)
            print("safety_area_size", safety_area_size)

            result = max(result, safety_area_size)

            # 벽 3개 리셋
            lab[xi][xj] = 0
            lab[yi][yj] = 0
            lab[zi][zj] = 0


print(result)
