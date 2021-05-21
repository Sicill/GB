class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(f'{self.name} started')
    def stop(self):
        print(f'{self.name} stopped')
    def turn(self, direction):
        print(f'{self.name} turned to the {direction}')
    def show_speed(self):
        print(f'your speed is {self.speed}')
class TownCar(Car):
    def show_speed(self):
        if self.speed <= 60:
            print(f'your speed is {self.speed}')
        else:
            print('you have exceeded the speed limit')
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed <= 40:
            print(f'your speed is {self.speed}')
        else:
            print('you have exceeded the speed limit')
class PoliceCar(Car):
    pass

bmw = TownCar(66, 'black', 'BMW', False)
print(bmw.speed, bmw.color, bmw.name, bmw.is_police)
bmw.go()
bmw.stop()
bmw.turn('left')
bmw.show_speed()

porsche = SportCar(130, 'yellow', 'Porsche', False)
print(porsche.speed, porsche.color, porsche.name, porsche.is_police)
porsche.go()
porsche.stop()
porsche.turn('left')
porsche.show_speed()

volk = WorkCar(78, 'gray', 'Volkswagen', False)
print(volk.speed, volk.color, volk.name, volk.is_police)
volk.go()
volk.stop()
volk.turn('left')
volk.show_speed()

cop = PoliceCar(87, 'blue', 'Police', True)
print(cop.speed, cop.color, cop.name, cop.is_police)
cop.go()
cop.stop()
cop.turn('left')
cop.show_speed()