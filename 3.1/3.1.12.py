n = int(input())
lst = [
    "Манная",
    "Гречневая",
    "Пшённая",
    "Овсяная",
    "Рисовая"
]
for i in range(n):
    print(lst[i % 5])