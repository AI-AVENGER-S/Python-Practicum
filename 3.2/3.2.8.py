lst = []
for _ in range(int(input())):
    lst.append(input().split())
name = input()
lst = sorted(lst, key=lambda item: item[0])
flag = 1
for i in range(len(lst)):
    if any(lst[i][j] == name for j in range(1, len(lst[i]))):
        print(lst[i][0])
        flag = 0
if flag:
    print("Таких нет")