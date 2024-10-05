n = int(input())

matrix = [[0] * n for _ in range(n)]

for r in range(n):
    for c in range(n):
        matrix[r][c] = (c + 1) * (r + 1)
        print(matrix[r][c], end=' ')
    print()