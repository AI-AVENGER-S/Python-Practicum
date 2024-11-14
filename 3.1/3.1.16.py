total = int(input())
strings = [input() for _ in range(int(input()))]

for i in strings:
    if total <= 3:
        break
    print(i[:total:] if (total - len(i)) > 3 else i[:total - 3:] + "...")
    total -= len(i)
