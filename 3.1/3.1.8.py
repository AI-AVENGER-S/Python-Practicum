n = int(input())
for _ in range(n):
    s = input()
    if 'зайка' not in s:
        print("Заек нет =(")
    else:
        print(s.find('зайка') + 1)


