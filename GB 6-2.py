class Road():
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def calc_mass(self):
        print(self._length * self._width * 25 * 5)
nevskiy = Road(20, 3674)
nevskiy.calc_mass()