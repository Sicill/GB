with open('file2.txt') as f:
    count_str = 0
    dict = {}
    for line in f:
        count_str += 1
        dict[count_str] = 0
        for word in line.split(' '):
            dict[count_str] += 1
    print(count_str)
    print(dict)