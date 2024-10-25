def index(lst):
    res = []
    if '+' in lst:
        res.append(lst.index('+'))
    if '-' in lst:
        res.append(lst.index('-'))
    if '*' in lst:
        res.append(lst.index('*'))
    if '/' in lst:
        res.append(lst.index('/'))
    return min(res)


lst = input().split()
while len(lst) > 1:
    index_of_znak = index(lst)

    if lst[index_of_znak] == '+':
        temp = int(lst[index_of_znak - 2]) + int(lst[index_of_znak - 1])
    if lst[index_of_znak] == '-':
        temp = int(lst[index_of_znak - 2]) - int(lst[index_of_znak - 1])
    if lst[index_of_znak] == '*':
        temp = int(lst[index_of_znak - 2]) * int(lst[index_of_znak - 1])
    if lst[index_of_znak] == '/':
        temp = int(lst[index_of_znak - 2]) / int(lst[index_of_znak - 1])
    lst.pop(index_of_znak)
    lst.pop(index_of_znak - 1)
    lst.pop(index_of_znak - 2)
    lst.insert(index_of_znak - 2, temp)
print(lst[0])