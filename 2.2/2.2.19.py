def okrbig(x, y):
    if (x ** 2 + y ** 2) <= (10 ** 2):
        return 1
    return 0


def lineldiag(x, y):
    if 3 * y <= (5 * x + 35):
        return 1
    return 0


def lineltop(x, y):
    if y <= 5:
        return 1
    return 0


def okrsmall(x, y):
    if (x ** 2 + y ** 2) <= (5 ** 2):
        return 1
    return 0


def parabola(x, y):
    if (0.25 * x ** 2 + 0.5 * x - 8.75) <= y:
        return 1
    return 0


x = float(input())
y = float(input())

if not okrbig(x, y):
    print("Вы вышли в море и рискуете быть съеденным акулой!")
elif okrbig(x, y) and lineltop(x, y) and lineldiag(x, y) and okrsmall(x, y) and parabola(x, y):
    print("Опасность! Покиньте зону как можно скорее!")
else:
    print("Зона безопасна. Продолжайте работу.")