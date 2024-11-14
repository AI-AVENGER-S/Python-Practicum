result = []
while True:
    s = input()
    if s == '':
        break
    else:
        s = s.split()

        for i in range(len(s)):
            if s[i] == 'зайка':
                if i != 0:
                    result.append(s[i - 1])
                if i != len(s) - 1:
                    result.append(s[i + 1])

print(*set(result), sep='\n')