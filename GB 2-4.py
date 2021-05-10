string = input('type string: ')
string = string.split()
count = 0
for word in string:
    count += 1
    print(count, '{:.10s}'.format(word))
