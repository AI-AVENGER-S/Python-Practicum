s, counter = input() + '!', 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        counter += 1
    else:
        print(s[i], counter + 1)
        counter = 0