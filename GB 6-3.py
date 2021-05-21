class Worker():
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self._income = income
class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)
    def get_total_income(self):
        sum = 0
        for value in self._income.values():
            sum += value
        print(sum)

cobain = Position('Kurt', 'Cobain', 'Vocal', {'wage': 1234, 'bonus': 635})
cobain.get_full_name()
cobain.get_total_income()

novoselic = Position('Krist', 'Novoselic', 'Bass', {'wage': 2546, 'bonus': 1562})
novoselic.get_full_name()
novoselic.get_total_income()

