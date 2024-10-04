a, b, flag = int(input()), int(input()), -1
if a > b:
    flag = 1
for i in range(a, b - flag, -flag):
    print(i, end=' ')