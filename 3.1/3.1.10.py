total = {}
while True:
    s = input().lower()
    if s == 'финиш':
        break
    else:
        s = s.replace(' ', '')
        a = set(list(s))
        for i in a:
            if i in list(total.keys()):
                total[i] += s.count(i)
            else:
                total[i] = s.count(i)
total = dict(sorted(total.items(), key=lambda x: x[1]))
mini = 'я'
for key, value in total.items():
    if value == max(list(total.values())):
        mini = min(mini, key)
print(mini)


