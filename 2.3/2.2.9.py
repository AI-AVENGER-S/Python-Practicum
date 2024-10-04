def F(n):
    if n == 0:
        return 1
    return F(n - 1) * n


n = int(input())
print(F(n))