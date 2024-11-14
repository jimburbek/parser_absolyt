from bs4 import BeautifulSoup as bs
import requests as rq
import json

headers = {
        "User agent":  "prosto bog"
    }
urls_cards = []
for j in range(1, 7):
    url = f'https://scrapingclub.com/exercise/list_basic/?page={j}'
    response = rq.get(url=url, headers=headers)


    if response.status_code == 200:
        soup = bs(response.text, 'lxml')

        card_titles = soup.find_all('div', class_='w-full rounded border')
        for i in card_titles:
            urls_cards.append(i.find('a').get('href'))

all_data=[]
for i in urls_cards:
    url = f'https://scrapingclub.com{i}'
    response = rq.get(url=url, headers=headers)
    card_title = ''
    price = ''
    descr = ''
    if response.status_code == 200:
        soup = bs(response.text, 'lxml')

        card_title = soup.find('div', class_='my-8 w-full rounded border').find('div', class_='p-6').find('h3').text
        price = soup.find('div', class_='my-8 w-full rounded border').find('div', class_='p-6').find('h4').text
        descr = soup.find('div', class_='my-8 w-full rounded border').find('div', class_='p-6').find('p').text

        data = {
            'card_title': card_title,
            'price':price,
            'descr':descr
        }
        all_data.append(data)
with open('data_parser.json', 'w', encoding='UTF-8') as file:
    json.dump(all_data, file, ensure_ascii=False, indent=4)