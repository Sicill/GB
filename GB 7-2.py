class Clothes():

    def __init__(self, param):
        self.param = param


class Coat(Clothes):

    @property
    def count(self):
        return self.param / 6.5 + 0.5


class Suit(Clothes):

    @property
    def count(self):
        return 2 * self.param + 0.3


coat = Coat(56)
print(coat.count)
suit = Suit(74)
print(suit.count)
