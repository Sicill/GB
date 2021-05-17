def fact(n):
    f = 1
    for num in range(1, n + 1):
        f *= num
        yield f
for num in fact(7):
    print(num)
