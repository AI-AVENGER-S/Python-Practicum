lst = [int(i) for i in input()]

lst.sort()
if lst[0] + lst[-1] == lst[1] * 2:
    print('YES')
else:
    print('NO')