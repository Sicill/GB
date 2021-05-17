import functools
lst = [num for num in range(100, 1001) if num % 2 == 0]
def mult(num1, num2):
    return num1 * num2
print(functools.reduce(mult, lst))