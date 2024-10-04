def delitel(n):
    res = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res.append(n // i)
            res.append(i)
        res.append(n)
    return list(sorted(set(res)))


a = int(input())
if len(delitel(a)) == 2:
    print('YES')
else:
    print('NO')