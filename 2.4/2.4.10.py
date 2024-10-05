n = int(input())
print("А Б В")
for i in range(1, n + 1 - 2):
    for j in range(1, n + 1 - 2):
        for k in range(1, n + 1 - 2):
            if i + j + k == n:
                print(i, j, k)
