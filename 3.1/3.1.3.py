n, k = int(input()), int(input())
for _ in range(k):
    s = input()
    if len(s) > n:
        print(s[:n - 3:] + '...')
    else:
        print(s)