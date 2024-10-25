while True:
    s = input()
    if s == '':
        break
    if '@@@' in s[-3:]:
        s = ''
        print(s, end='')
    elif '##' in s[:2]:
        s = s[2:]
        print(s)
    else:
        print(s)