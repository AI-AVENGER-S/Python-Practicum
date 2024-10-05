n, lst = int(input()), []
mas = [int(input()) for _ in range(n)]
for x in range(len(mas) - 1):
    a = mas[x]
    b = mas[x + 1]
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    lst.append(a + b)
print(min(lst))