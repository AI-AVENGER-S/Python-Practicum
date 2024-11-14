lst = []
for _ in range(int(input())):
    lst.append(input())
print(sum(lst.count(i) for i in set(lst) if lst.count(i) != 1))