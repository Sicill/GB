start = input('current: ')
current = int(start)
goal = input('goal: ')
day = 1
while current < int(goal):
    current += current / 100 * 10
    day += 1
print(day)