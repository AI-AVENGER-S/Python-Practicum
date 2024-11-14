while True:
    s = input()
    if s == '':
        break
    else:
        if s.count('#') >= 1:
            if s[0] != '#':
                print(s[:s.find('#')])
        else:
            print(s)