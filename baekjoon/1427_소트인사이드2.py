string = input()
arr = [0] * 10

# 0~9가 각각 몇 번 나왔는지 세기
for ch in string:
    idx = int(ch)
    arr[idx] += 1

# 9부터 나온 갯수만큼 출력
for i in range(9, -1, -1):
    for j in range(arr[i]):
        print(i, end='')
