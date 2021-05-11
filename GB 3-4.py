def my_func(x, y):
    print(x ** y)
    exp = 1
    for i in range(abs(y)):
        exp /= x
    print(exp)

my_func(3, -4)
