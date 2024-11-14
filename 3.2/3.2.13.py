ingridients = [input() for _ in range(int(input()))]
what_can_cook = {}
for _ in range(int(input())):
    name = input()
    what_can_cook[name] = what_can_cook.get(name, [])
    for _ in range(int(input())):
        what_can_cook[name].append(input())
what_can_cook = dict(sorted(what_can_cook.items(), key=lambda item: item[0]))
flag = 1
for key in what_can_cook:
    if all(i in ingridients for i in what_can_cook[key]):
        print(key)
        flag = 0
if flag:
    print("Готовить нечего")


