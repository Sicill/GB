import requests
from pprint import pprint
from pymongo import MongoClient
from lxml import html

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
response = requests.get('https://lenta.ru', headers=header)
dom = html.fromstring(response.text)
news = dom.xpath(".//body//div[@class='item']/a/@href")
news_list = []
for new in news:
    news_dict = {}
    news_dict['link'] = 'https://lenta.ru' + new
    link_split = news_dict['link'].split('/')

    if link_split[3] == 'news':
        news_req = requests.get(news_dict['link'], headers=header)
        page = html.fromstring(news_req.text)

    news_dict['title'] = page.xpath(".//h1[@class='b-topic__title']/text()")
    news_dict['date'] = link_split[4] + '-' + link_split[5] + '-' + link_split[6]
    news_list.append(news_dict)


client = MongoClient('localhost', 27017)
db = client['news']
news_mongo = db.news

for new in news_list:
    news_mongo.insert_one(new)

