fir = input()
sec = input()
res = ''
if len(fir) > len(sec):
    sec = '0' + sec
else:
    fir = '0' + fir
for i in range(1, min(len(fir), len(sec)) + 1):
    res = str((int(fir[-i]) + int(sec[-i])))[-1] + res
print(res)
