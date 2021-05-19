with open ('file.txt', 'w') as f:
    txt = []
    while True:
        str = input('type something: ')
        txt.append(str)
        if str == '':
            break
    f.writelines(txt)


