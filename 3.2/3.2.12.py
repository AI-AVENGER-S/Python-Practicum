lst = [input() for _ in range(int(input()))]
elements = [f"{i} - {lst.count(i)}" for i in sorted(set(lst)) if lst.count(i) != 1]
if not elements:
    print("Однофамильцев нет")
else:
    ordered_set = []
    for element in elements:
        if element not in ordered_set:
            ordered_set.append(element)
    print(*ordered_set, sep='\n')

