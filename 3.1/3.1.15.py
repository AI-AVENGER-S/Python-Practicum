s = input().split()
mini = min(map(int, s))
for i in range(mini, 0, - 1):
    if all(int(j) % i == 0 for j in s):
        print(i)
        break
