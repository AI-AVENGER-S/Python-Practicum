n = int(input())
lst = [input() for _ in range(n)]
search = (input()).lower()
for i in lst:
    if search in i.lower():
        print(i)

