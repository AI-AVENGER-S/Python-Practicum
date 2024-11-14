def fac(number):
    if number == 1:
        return 1
    else:
        return number * fac(number - 1)


def index(lst):
    res = []
    if '+' in lst:
        res.append(lst.index('+'))
    if '-' in lst:
        res.append(lst.index('-'))
    if '*' in lst:
        res.append(lst.index('*'))
    if '~' in lst:
        res.append(lst.index('~'))
    if '#' in lst:
        res.append(lst.index('#'))
    if '!' in lst:
        res.append(lst.index('!'))
    if '@' in lst:
        res.append(lst.index('@'))
    if '/' in lst:
        res.append(lst.index('/'))
    return min(res)


lst = input().split()
i = 0
while len(lst) > 1:
    i = index(lst)

    if lst[i] == '+':
        temp = int(lst[i - 2]) + int(lst[i - 1])
        lst.pop(i)
        lst.pop(i - 1)
        lst.pop(i - 2)
        lst.insert(i - 2, temp)
        continue
    if lst[i] == '*':
        temp = int(lst[i - 2]) * int(lst[i - 1])
        lst.pop(i)
        lst.pop(i - 1)
        lst.pop(i - 2)
        lst.insert(i - 2, temp)
        continue
    if lst[i] == '-':
        temp = int(lst[i - 2]) - int(lst[i - 1])
        lst.pop(i)
        lst.pop(i - 1)
        lst.pop(i - 2)
        lst.insert(i - 2, temp)
        continue
    if lst[i] == '/':
        temp = int(lst[i - 2]) // int(lst[i - 1])
        lst.pop(i)
        lst.pop(i - 1)
        lst.pop(i - 2)
        lst.insert(i - 2, temp)
        continue
    if lst[i] == '#':
        lst.pop(i)
        lst.insert(i - 1, lst[i - 1])
        continue
    if lst[i] == '~':
        lst.pop(i)
        lst[i - 1] = -int(lst[i - 1])
        continue
    if lst[i] == '@':
        lst.pop(i)
        lst[i - 1], lst[i - 2] = lst[i - 2], lst[i - 1]
        lst[i - 3], lst[i - 1] = lst[i - 1], lst[i - 3]
        continue
    if lst[i] == '!':
        lst.pop(i)
        lst[i - 1] = int(fac(int(lst[i - 1])))
        continue

print(lst[0])

