a = int(input())
b = int(input())
c = int(input())

lst = [a, b, c]
if all((i < sum(lst) - i) for i in lst):
    print('YES')
else:
    print('NO')