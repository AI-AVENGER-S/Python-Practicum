a = input()
b = input()
c = input()
lst = [a, b, c]
lst.sort(key=len)
lst.sort()
print(lst[0])