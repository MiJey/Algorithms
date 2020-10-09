input()
arr = sorted(list(map(int, set(input().split(' ')))))
print(' '.join(map(str, arr)))
