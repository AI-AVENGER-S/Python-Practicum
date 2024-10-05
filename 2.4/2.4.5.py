n, count = int(input()), 0
for _ in range(n):
    flag = True
    while True:
        text = input()
        if text == "ВСЁ":
            break
        if text == "зайка" and flag:
            count += 1
            flag = False
print(count)