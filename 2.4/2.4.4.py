n, summ = int(input()), 0
for _ in range(n):
    summ += sum(map(int, input()))
print(summ)