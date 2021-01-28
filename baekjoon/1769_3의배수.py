x = list(map(int, list(input())))
result = 0

while len(x) != 1:
    x = list(map(int, str(sum(x))))
    result += 1

print(result)

if x[0] % 3 == 0:
    print("YES")
else:
    print("NO")
