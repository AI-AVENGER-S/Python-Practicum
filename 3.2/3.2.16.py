lst_of_friends = {}
while True:
    s = input()
    if s == '':
        break
    else:
        s = s.split()
        for i in range(2):
            if s[i] in lst_of_friends:
                lst_of_friends[s[i]].append(s[i - 1])
            else:
                lst_of_friends[s[i]] = [s[i - 1]]

lst_of_friends = dict(sorted(lst_of_friends.items(), key=lambda item: item[0]))

answer = []
for friend in lst_of_friends:
    print(f'{friend}: ', end='')
    for sec_friend in lst_of_friends[friend]:
        for i in lst_of_friends[sec_friend]:
            if i != friend and i not in lst_of_friends[friend]:
                answer.append(i)
    print(*list(sorted(set(answer))), sep=', ')
    answer = []
