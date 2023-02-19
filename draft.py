import requests
from bs4 import BeautifulSoup
import re

url = 'https://habr.com/ru/all/'

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

resp = requests.get(url)
response = resp.text

soup = BeautifulSoup(response, features='lxml')

pattern =r'\d{6}\b'

ID_list = re.findall(pattern, response)

id_viewed = ''
for id_article in ID_list:
    if id_article != id_viewed:
        article = soup.find(id=id_article)
        id_viewed = id_article
        if article != None:
            span = article.find(str(id_article)+'/"><span>')
            print(f'\n{span}\n')
        df = span.text
        data, header, link = '','',''
        for kw in KEYWORDS:
            for art in df:
                if kw in art:
                    print(f'{data} - {header} - {link})
# print(df)





