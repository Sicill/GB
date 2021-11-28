import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
from pymongo import MongoClient

url = 'https://spb.hh.ru/'
search = 'арбитраж'
page_num = 0
vacancies = []
#можно указывать сколько угодно страниц, это не приведёт к ошибке
for page in range(2):
    params = {'area': 2, 'fromSearchLine': 'true', 'text': search, 'page': page_num}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
    response = requests.get(url + 'search/vacancy', params=params, headers=headers)
    dom = BeautifulSoup(response.content, 'html.parser')
    find_vacancies = dom.find_all('div', {'class': 'vacancy-serp-item'})
    vacancies += find_vacancies
    page_num += 1

vacancies_lst = []
for vacancy in vacancies:
    vacancy_dict = {}
    name = vacancy.find('a').text
    vacancy_dict['name'] = name
    link = vacancy.find('a').get('href')
    vacancy_dict['link'] = link

    if vacancy.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'}):
        wage_split = vacancy.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'}).text.split()
        vacancy_dict['wage'] = {}
        if wage_split[0] == 'от':
            wage_from = wage_split[1]
            if wage_split[2].isdigit():
                wage_from += wage_split[2]
            wage_from = int(wage_from)
            vacancy_dict['wage']['from'] = wage_from
            vacancy_dict['wage']['to'] = None

        if wage_split[0].isdigit():
            wage_from = wage_split[0]
            if wage_split[1].isdigit():
                wage_from += wage_split[1]
            wage_from = int(wage_from)
            vacancy_dict['wage']['from'] = wage_from
            if wage_split[1] == '–':
                wage_to = wage_split[2]
                if wage_split[3].isdigit():
                    wage_to += wage_split[3]
                wage_to = int(wage_to)
                vacancy_dict['wage']['to'] = wage_to
            if wage_split[2] == '–':
                wage_to = wage_split[3]
                if wage_split[4].isdigit():
                    wage_to += wage_split[4]
                wage_to = int(wage_to)
                vacancy_dict['wage']['to'] = wage_to

        if wage_split[0] == 'до':
            wage_to = wage_split[1]
            if wage_split[2].isdigit():
                wage_to += wage_split[2]
            wage_to = int(wage_to)
            vacancy_dict['wage']['to'] = wage_to
            vacancy_dict['wage']['from'] = None

        vacancy_dict['wage']['currency'] = wage_split[-1]

    else:
        vacancy_dict['wage'] = None

    vacancies_lst.append(vacancy_dict)

with open('vacancies.json', 'w') as vac:
    json.dump(vacancies_lst , vac)

client = MongoClient('localhost', 27017)
db = client['vacancies']
vac_mongo = db.vacancies

for vac in vacancies_lst:
    vac_mongo.insert_one(vac)

old_lst = vacancies_lst
for vac in vacancies_lst:
    if vac not in old_lst:
        vac_mongo.insert_one(vac)

def find_vacancy():
    while True:
        try:
            min_wage = int(input('Type minimum wage: '))
        except:
            print('It should be integer!')
            continue

        try:
            max_wage = int(input('Type maximum wage: '))
        except:
            print('It should be integer!')
            continue

        vacs = vac_mongo.find({'wage.from': {'$gte': min_wage}, 'wage.to': {'$lte': max_wage}})
        for vac in vacs:
            pprint(vac)
        break


find_vacancy()



