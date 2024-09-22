a = float(input())
b = float(input())
c = float(input())

if a == b == c == 0.0:
    print("Infinite solutions")
elif a == b == 0.0 or (b ** 2 - 4 * a * c) < 0.0:
    print('No solution')
elif (b ** 2 - 4 * a * c) == 0.0:
    print(f"{-b / (2 * a):.2f}")
elif a == 0.0:
    print(f'{-c / b:.2f}')
else:
    lst = [(-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a), (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)]
    lst.sort()
    print(f'{lst[0]:.2f} {lst[1]:.2f}')
