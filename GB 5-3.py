with open('file3.txt') as f:
    wages = []
    less20 = []
    for line in f:
        lst = line.split(' ')
        wages.append(int(lst[1]))
        if int(lst[1]) < 20000:
            less20.append(lst[0])
    print(less20)
    print(sum(wages) / len(wages))