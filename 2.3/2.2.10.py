x, y = 0, 0
while True:
    a = input()
    if a == "СТОП":
        break
    number = int(input())
    if a == 'СЕВЕР':
        y += number
    if a == 'ЗАПАД':
        x -= number
    if a == 'ЮГ':
        y -= number
    if a == 'ВОСТОК':
        x += number
print(y, x, sep='\n')