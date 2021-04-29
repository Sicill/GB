income = input('type income: ')
costs = input('type costs: ')
if int(income) > int(costs):
    print('You are in profit!')
    profit = int(income) / (int(costs) / 100) - 100
    print('Your profit is ' + str(profit) + '%')
    empl = input('type number of employees: ')
    avrg = (int(income) - int(costs)) / int(empl)
    print('Your employee give you ' + str(avrg) + ' in average')
else:
    print('You are in losses!')