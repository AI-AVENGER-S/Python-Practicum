n = int(input())

for r in range(1, n + 1):
    for c in range(1, n + 1):
        print(c, '*', r, '=', c * r)