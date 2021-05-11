nums = input('type numbers: ')
def sum_nums(lst):
    sum = 0
    for num in lst:
        sum += int(num)
    return sum
lst_nums = nums.split(' ')
sum = sum_nums(lst_nums)
print(sum)
while 'q' not in nums:
    nums = input('type numbers or press q to exit: ')
    lst_nums = nums.split(' ')
    if 'q' in lst_nums:
        lst_nums.remove('q')
        sum = sum + sum_nums(lst_nums)
        print(sum)
        break
    sum = sum + sum_nums(lst_nums)
    print(sum)
else:
    lst_nums = nums.split(' ')
    lst_nums.remove('q')
    sum = sum + sum_nums(lst_nums)
    print(sum)
