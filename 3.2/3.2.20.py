def euclidean_algorithm(a, b):
    while b != 0:
        a, b = b, a % b
    return a


test = input().split('; ')
test = list(map(int, list(sorted(set(test)))))
data = {}
for key in test:
    values_to_add = sorted(i for i in test if euclidean_algorithm(i, key) == 1)
    data[key] = data.get(key, values_to_add)

data = dict(sorted(data.items(), key=lambda item: item[0]))

for i in data:
    if len(data[i]):
        print(i, '-', end=' ')
        print(*data[i], sep=', ')