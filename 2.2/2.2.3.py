v1 = int(input())
v2 = int(input())
v3 = int(input())
lst = [v1, v2, v3]
need = ['Петя', 'Вася', 'Толя']
print(need[lst.index(max(lst))])