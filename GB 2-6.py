lst = []
tuple = ()
count = 1
dict = {'name': '', 'price': '', 'amount': ''}
dict['name'] = input('type name: ')
name_lst = [dict['name']]
dict['price'] = input('type price: ')
price_lst = [dict['price']]
dict['amount'] = input('type amount: ')
amount_lst = [dict['amount']]
tuple = (count, dict)
count += 1
lst.append(tuple)

dict['name'] = input('type name: ')
name_lst.append(dict['name'])
dict['price'] = input('type price: ')
price_lst.append(dict['price'])
dict['amount'] = input('type amount: ')
amount_lst.append(dict['amount'])
tuple = (count, dict)
count += 1
lst.append(tuple)

dict['name'] = input('type name: ')
name_lst.append(dict['name'])
dict['price'] = input('type price: ')
price_lst.append(dict['price'])
dict['amount'] = input('type amount: ')
amount_lst.append(dict['amount'])
tuple = (count, dict)
count += 1
lst.append(tuple)
print(lst)

new_dict = {'name': name_lst, 'price': price_lst, 'amount': amount_lst}
print(new_dict)