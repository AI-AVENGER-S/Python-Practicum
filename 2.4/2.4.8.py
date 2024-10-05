n = int(input())
dic = {input(): sum(map(int, input())) for _ in range(n)}
dic = dict(sorted(dic.items(), key=lambda item: item[1]))
print(list(dic.keys())[-1])