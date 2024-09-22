lst = [int(x) for x in input()]

lst.sort()
if lst[0] != 0:
    mini = str(lst[0]) + str(lst[1])
    maxi = str(lst[-1]) + str(lst[-2])
else:
    mini = str(lst[1]) + str(lst[0])
    maxi = str(lst[-1]) + str(lst[-2])
print(mini, maxi)