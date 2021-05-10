lst = []
num1 = input('type: ')
lst.append(num1)
num2 = input('type: ')
lst.append(num2)
num3 = input('type: ')
lst.append(num3)
num4 = input('type: ')
lst.append(num4)
num5 = input('type: ')
lst.append(num5)
for i in range(len(lst)-1):
    if i % 2 == 0:
        num = lst[i]
        lst[i] = lst[i + 1]
        lst[i + 1] = num
print(lst)