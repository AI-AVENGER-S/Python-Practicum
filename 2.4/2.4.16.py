n, m = int(input()), int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j < n:
            print(f'{i * j:^{m}}', end="|")
        else:
            print(f'{i * j:^{m}}')
    if i < n:
        print('-' * ((n * m) + (n - 1)))