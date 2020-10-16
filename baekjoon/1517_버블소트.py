import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
result = 0

for i in range(0, n - 1):
    for j in range(i + 1, n):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            result += 1

print(result)
