string, new_string = input(), ''
for i in string:
    if int(i) % 2 != 0:
        new_string += i
print(new_string)