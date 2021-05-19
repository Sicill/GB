with open('file7.txt') as f:
    dict_firms = {}
    profits = []
    for line in f:
        lst = line.split(' ')
        if int(lst[2]) > int(lst[3]):
            profit = int(lst[2]) - int(lst[3])
            dict_firms[lst[0]] = profit
            profits.append(profit)
    dict_average = {'average_profit': sum(profits) / len(profits)}
    end_lst = [dict_firms, dict_average]
    print(end_lst)
import json
with open('file7.json', 'w') as f_json:
    json.dump(end_lst, f_json)
