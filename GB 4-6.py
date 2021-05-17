from itertools import count, cycle
lst = []
for num in count(3):
    if num > 10:
        break
    else:
        print(num)
        lst.append(num)
count = 0
for num in cycle(lst):
    if count > 20:
        break
    else:
        print(num)
        count += 1
