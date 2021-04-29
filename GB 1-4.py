num = input('type number: ')
max = 0
i = 0
while int(num[i]) > max:
    if i < len(num):
        max = int(num[i])
        i += 1
print(max)