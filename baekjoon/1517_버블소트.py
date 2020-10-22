import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
result = 0

for i in range(0, n):
    for j in range(i, n):
        if arr[i] > arr[j]:
            result += 1

print(result)
