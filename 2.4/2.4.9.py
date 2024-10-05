n, summ = int(input()), ''
for _ in range(n):
    summ += str(max(map(int, input())))
print(summ)