with open('file6.txt', encoding='utf-8') as f:
    dict = {}
    for line in f:
        lst = line.split(' ')
        hours_lst = []
        for el in lst[1:]:
            num = ''
            for symbol in el:
                if symbol.isdigit():
                    num += symbol
            hours_lst.append(num)
        sum = 0
        for hours in hours_lst:
            if hours.isdigit():
                sum += int(hours)
        dict[lst[0]] = sum
    print(dict)

