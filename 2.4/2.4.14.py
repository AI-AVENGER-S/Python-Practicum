n, m, count = int(input()), int(input()), 0
matrix = [[0] * m for _ in range(n)]
for r in range(n):
    for c in range(m):
        count += 1
        if r % 2 == 0:
            matrix[r][c] = count
        else:
            matrix[r][-(c + 1)] = count

#вывод
for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).rjust(len(str(count))), end=' ')
    print()