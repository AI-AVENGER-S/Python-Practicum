pokupka = 0
while True:
    summ = float(input())
    if summ == 0:
        break
    if summ >= 500:
        summ *= 0.9
    pokupka += summ
print(pokupka)