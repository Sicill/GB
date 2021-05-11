x = int(input('x: '))
y = int(input('y: '))
def division(x, y):
    if y == 0:
        return "you can't divide to zero"
    else:
        return x / y
print(division(x, y))