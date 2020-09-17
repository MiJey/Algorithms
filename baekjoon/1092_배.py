import sys
input = sys.stdin.readline

# 크레인 마다 줄 서는 순서
#   1. 무거운 박스 먼저 크레인에 줄을 선다
#   2. 가벼운 박스는 아무 크레인이나 빈 공간에 줄을 선다
#
# 예시
# crane = [9, 8, 6]
# boxes = [9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 5, 5, 4, 4, 2, 1, 1]
#          0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17
#
# 실제로 들어가는 순서
# 9:  (0)9  (1)9  (2)9  (3)9  (8)8 (10)8 (18) (21) ...
# 8:  (4)8  (5)8  (6)8  (7)8  (9)8 (11)5 (19) (22) ...
# 6: (12)5 (13)4 (14)4 (15)2 (16)1 (17)1 (20) (23) ...

input()
cranes = list(map(int, input().split()))
input()
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
cranes.append(0)
boxes.sort(reverse=True)
ports = [[] for _ in range(len(cranes))]
i = 0

if boxes[0] > cranes[0]:
    print(-1)
    exit()

for box in boxes:
    if box > cranes[i + 1]:
        while i > 0 and len(ports[i - 1]) <= len(ports[i]):
            i -= 1

        ports[i].append(box)
        continue

    i += 1
    ports[i].append(box)

print(max([len(x) for x in ports]))
