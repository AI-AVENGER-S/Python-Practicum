n, count = int(input()), 0

for _ in range(n):
    a = input()
    if a == a[::-1]:
        count += 1
print(count)
