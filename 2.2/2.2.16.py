v1 = int(input())
v2 = int(input())
v3 = int(input())
lst = [v1, v2, v3]
need = ['Петя', 'Вася', 'Толя']

print("{:^24}".format(need[lst.index(max(lst))]))
need.pop(lst.index(max(lst)))
lst.remove(max(lst))


print('  ' + "{:<22}".format(need[lst.index(max(lst))]))
need.pop(lst.index(max(lst)))
lst.remove(max(lst))


print("{:>22}".format(need[lst.index(max(lst))]) + '  ')
print('   II      I      III   ')
