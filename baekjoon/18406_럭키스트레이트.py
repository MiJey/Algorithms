arr = list(map(int, list(input())))
a, b = 0, 0
half = len(arr) // 2

for i in range(half):
    a += arr[i]

for i in range(half, len(arr)):
    b += arr[i]

if a == b:
    print("LUCKY")
else:
    print("READY")
