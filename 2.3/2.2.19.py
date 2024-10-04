st, end, count = 1, 1000, 0
while count <= 10:
    count += 1
    number = int(((end + st) / 2))
    user_input = input(f'{number}\n')
    if user_input == "Угадал!":
        break
    if user_input == 'Больше':
        st = number + 1
    if user_input == 'Меньше':
        end = number

