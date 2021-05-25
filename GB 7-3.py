class Cell():

    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        if self.num <= other.num:
            print('Error')
        else:
            return self.num - other.num

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        return int(self.num / other.num)

    def make_order(self, row):
        str = ''
        while self.num > row:
            str += '*' * row + '\n'
            self.num -= row
        else:
            str += '*' * self.num
        return str

cell = Cell(23)
print(cell.make_order(4))