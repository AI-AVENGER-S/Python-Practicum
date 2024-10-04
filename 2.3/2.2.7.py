a, b = int(input()), int(input())

for i in range(max(a, b), 10 ** 20):
    if i % a == 0 and i % b == 0:
        print(i)
        break