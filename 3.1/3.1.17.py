s = input().lower().split()
s = ''.join(s)
if s == s[::-1]:
    print("YES")
else:
    print("NO")
