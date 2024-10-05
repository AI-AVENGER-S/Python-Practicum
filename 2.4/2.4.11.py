def deliteli(number):
    if number > 1 and all(number % i != 0 for i in range(2, int(number ** 0.5) + 1)):
        return True
    return False


n, count = int(input()), 0
for _ in range(n):
    if deliteli(int(input())):
        count += 1
print(count)