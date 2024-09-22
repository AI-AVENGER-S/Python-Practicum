a = input()
b = input()

lst = [a[0], a[1], b[0], b[1]]
lst = list(map(int, lst))

lst.sort()
print(lst[-1], ((lst[1] + lst[2]) % 10), lst[0], sep='')