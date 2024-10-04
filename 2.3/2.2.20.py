flag, h = -1, 0
for i in range(int(input())):
    b = int(input())
    hn, r, m = b % 256, (b // 256) % 256, b // 256 ** 2
    hx = ((m + r + h) * 37) % 256
    if hx != hn or hn > 99:
        flag = i
        break
    h = hn
print(flag)