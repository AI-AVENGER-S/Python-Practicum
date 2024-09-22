N = int(input())
M = int(input())
T = int(input())
hours = '0' + str((N + T // 60 + ((M + T % 60) // 60)) % 24)
minutes = '0' + str((M + T % 60) % 60)

print(hours[-2:], ':', minutes[-2:], sep='')
