class Stationery():
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Start drawing')
class Pen(Stationery):
    def draw(self):
        print(f'Start drawing with {self.title}')
class Pencil(Stationery):
    def draw(self):
        print(f'Start drawing with {self.title}')
class Handle(Stationery):
    def draw(self):
        print(f'Start drawing with {self.title}')
pen = Pen('pen')
pen.draw()
pencil = Pencil('pencil')
pencil.draw()
handle = Handle('handle')
handle.draw()