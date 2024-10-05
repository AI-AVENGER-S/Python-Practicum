n = int(input())
count = 1
while count <= n:
    for i in range(3 + count - 1, 0, -1):
        print(f'До старта {i} секунд(ы)')
    print(f'Старт {count}!!!')
    count += 1