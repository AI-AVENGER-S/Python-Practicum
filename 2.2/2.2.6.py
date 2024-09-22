year = int(input())
lst = [int(x) for x in range(4, 10000, 4)]
for i in range(1700, 10000, 100):
    if i % 400 != 0:
        lst.remove(i)
if year in lst:
    print('YES')
else:
    print('NO')