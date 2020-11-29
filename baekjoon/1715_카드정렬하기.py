import sys
from queue import PriorityQueue
input = sys.stdin.readline

n = int(input())
queue = PriorityQueue()
result = 0

for _ in range(n):
    queue.put(int(input()))

# 가장 작은 2개의 카드 뭉치의 합을 result에 누적
while queue.qsize() > 1:
    deck = queue.get() + queue.get()
    result += deck
    queue.put(deck)

print(result)
