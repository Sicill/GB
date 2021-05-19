with open ('file5.txt', 'w') as f:
    f.write(input('type numbers: '))
with open('file5.txt') as f:
    lst = f.readline().split(' ')
    sum = 0
    for num in lst:
        sum += int(num)
    print(sum)


