step = x1 = x2 = 1
num = int(input())
while (not (x1 <= num <= x2)):
    x1 += step
    step += 1
    x2 += step
s = ''
x2 = num
for i in range(x1, x2 + 1):
    s += str(i)
    if i != x2:
        s += ' '
symnum = len(s)
x1 = x2 = step = 1
string = ''
while (not (x1 <= num <= x2)):
    for j in range(x1, x2 + 1):
        string += str(j)
        if j != x2:
            string += ' '
        else:
            print(f'{string:^{symnum}}')
    x1 += step
    step += 1
    x2 += step
    string = ''
for i in range(x1, num + 1):
    string += f'{i} '
print(string[:-1])