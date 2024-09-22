a = input()

lst = [int(a[0]) + int(a[1]), int(a[1]) + int(a[2])]
lst.sort(reverse=True)
lst = map(str, lst)
print(''.join(lst))