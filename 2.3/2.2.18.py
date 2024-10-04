a, i, lst = int(input()), 2, []
while a > 1:
    if a % i == 0:
        a //= i
        lst.append(str(i))
    else:
        i += 1
print(' * '.join(lst))