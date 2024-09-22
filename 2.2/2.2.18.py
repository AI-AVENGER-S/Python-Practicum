a = int(input())
b = int(input())
c = int(input())

lst = [a, b, c]
lst.sort()
if lst[0] ** 2 + lst[1] ** 2 == lst[2] ** 2:
    print('100%')
elif lst[0] ** 2 + lst[1] ** 2 > lst[2] ** 2:
    print('крайне мала')
else:
    print('велика')