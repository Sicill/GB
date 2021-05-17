def fact(n):
    for num in range(1, n + 1):
        yield num
for num in fact(7):
    print(num)

