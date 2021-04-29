time = input('type time in seconds: ')
hours = int(time) // 3600
rem = int(time) % 3600
minutes = rem // 60
secs = rem % 60
print(str(hours) + ':' + str(minutes) + ':' + str(secs))