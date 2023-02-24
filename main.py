import requests
from bs4 import BeautifulSoup
import re
import pprint
import json
from fake_headers import Headers


def get_head():
    headers = Headers(browser='yandex', os='win')
    return headers.generate()

url = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'

KEYWORDS = ['Django', 'Flask']
# Записать в json информацию о каждой вакансии - ссылка, вилка зп, название компании, город.
resp = requests.get(url, headers=get_head())
response = resp.text

soup = BeautifulSoup(response, features='lxml')

vacancy_list = soup.find_all('div', class_='serp-item')
suitable_vacancies = {}
for vacancy in vacancy_list:
    link = vacancy.find('a')['href']
    salarys = vacancy.find('span', class_='bloko-header-section-3')
    if salarys == None:
        df = 'не указана'
    else:
        df = salarys.text
        # print(f'\n{vacancy}\n{link}\n{salary}\n')
    print(f'\nЗарплата: {df}, ссылка: {link}\n')

# company = vacancy.find('a')['<!-- -->']
    # print(f'\n{salary}\n')

