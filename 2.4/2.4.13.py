n, m, count = int(input()), int(input()), 1
matrix = [[0] * m for _ in range(n)]
for c in range(m):
    for r in range(n):
        matrix[r][c] = count
        count += 1

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).rjust(len(str(count))), end=' ')
    print()