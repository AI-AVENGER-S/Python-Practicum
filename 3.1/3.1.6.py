n, count = int(input()), 0
lst = [input() for _ in range(n)]
for i in lst:
    for j in range(0, len(i) - 4):
        if 'зайка' in i[j:j + 5]:
            count += 1
print(count)
