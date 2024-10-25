n = int(input())
lst = [input() for _ in range(n)]
if all(s[0] in 'абв' for s in lst):
    print('YES')
else:
    print('NO')
