n, count = int(input()), 0
matrix = [[0] * n for _ in range(n)]
for r in range(int(n / 2 + 0.5)):
    for c in range(int(n / 2 + 0.5)):
        matrix[r][c] = min(r + 1, c + 1)
for r in range(int(n / 2 + 0.5)):
    for c in range(int(n / 2 + 0.5)):
        matrix[r][-(c + 1)] = matrix[r][c]
        matrix[-(r + 1)][c] = matrix[r][c]
        matrix[-(r + 1)][-(c + 1)] = matrix[r][c]

for string in matrix:
    count = 0
    for element in string:
        count += 1
        if count < n:
            print(f'{element:>{len(str((n // 2) + 1))}}', end=' ')
        else:
            print(f'{element:>{len(str((n // 2) + 1))}}')
