n = int(input())
# 5키로 봉지를 최대한 들어본다 -> 하나씩 줄여가면서 딱 맞아 떨어지는지 확인
for i in range(n // 5, -1, -1):
    remain = n - (5 * i)
    if remain % 3 == 0:
        print(i + (remain // 3))
        exit()
print(-1)