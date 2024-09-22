a = input()
b = input()
c = input()

lst = [a, b, c]
lst.sort(key=len)
lst.sort()
for i in lst:
    if 'зайка' in i:
        print(i, len(i))
        break