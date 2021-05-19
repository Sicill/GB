with open('file4.txt') as f1, open('new_file4.txt', 'w') as f2:
    dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    new_list = []
    for line in f1:
        lst = line.split(' ')
        lst[0] = dict[lst[0]]
        new_list.append(' '.join(lst))
    print(new_list)
    f2.writelines(new_list)

