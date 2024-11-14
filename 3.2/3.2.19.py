data, result = {}, []
for i in range(int(input())):
    s = input()
    key = s[:s.find(':')]
    values_to_add = s[s.find(':') + 2:].split(', ')
    data[key] = data.get(key, values_to_add)

for i in range(len(lst := list(data.values()))):
    for j in range(len(lst[i])):
        if all(lst[i - counter].count(lst[i][j]) == 0 for counter in range(1, len(lst))):
            result.append(lst[i][j])
print(*list(sorted(set(result))), sep='\n')
