def my_func(x, y, z):
    lst = [x, y, z]
    lst.sort()
    first_max = lst[-1]
    second_max = lst[-2]
    return first_max + second_max
print(my_func(30, 10, 20))