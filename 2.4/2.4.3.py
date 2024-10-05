n = int(input())
matrix = [[0] * n for _ in range(n)]
m = 1
for r in range(0, n):
    for c in range(0, n):
        if m > n:
            break
        if r >= c:
            matrix[r][c] = m
            m += 1
            print(matrix[r][c], end=' ')
    print()

