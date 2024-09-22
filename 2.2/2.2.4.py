v1 = int(input())
v2 = int(input())
v3 = int(input())
lst = [v1, v2, v3]
need = ['Петя', 'Вася', 'Толя']
for i in range(1, 3 + 1):
    print(f'{i}.', need[lst.index(max(lst))])
    lst[lst.index(max(lst))] = 0