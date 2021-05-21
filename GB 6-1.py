class TrafficLight():
    def __init__(self, color):
        self.color = color
    def running(self):
        lights = {'red': 7, 'yellow': 2,'green': 10}
        if self.color == 'red':
            print('red 7')
            print('yellow 2')
            print('green 10')
        elif self.color == 'yellow':
            print('yellow 2')
            print('green 10')
            print('red 7')
        else:
            print('green 10')
            print('red 7')
            print('yellow 2')

green = TrafficLight('green')
green.running()