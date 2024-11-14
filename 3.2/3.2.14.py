def converter(number):
    res = ''
    while number:
        res = str(number % 2) + res
        number //= 2
    return res

lst = input().split()
lst = list((map(int, lst)))
answer = [{} for _ in range(len(lst))]
for i in range(len(answer)):
    answer[i]["digits"] = answer[i].get("digits", len(converter(lst[i])))
    answer[i]["units"] = answer[i].get("units", converter(lst[i]).count('1'))
    answer[i]["zeros"] = answer[i].get("zeros", converter(lst[i]).count('0'))


print(answer)