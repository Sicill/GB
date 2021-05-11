def int_func(word):
    return word.capitalize()
print(int_func('word'))
string = "i've done it"
print(' '.join(list(map(int_func, string.split(' ')))))

