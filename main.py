import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
from fake_headers import Headers
import os
import re


def get_head():
    headers = Headers(browser='yandex', os='win')
    return headers.generate()


path = os.path.join(os.getcwd())
full_path = os.path.join(path, 'vacancy.json')

suitable_vacancies = {}
for page in range(0, 20):
    url = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2&page=' + str(page)

    resp = requests.get(url, headers=get_head())
    resp.raise_for_status()
    if resp.status_code in range(200, 300):
        response = resp.text

        soup = BeautifulSoup(response, features='lxml')

        vacancy_list = soup.find_all('div', class_='serp-item')

        for serp in vacancy_list:
            vacancy = serp.find('a').text # Название профессии
            KEYWORDS = ['Flask', 'Django']
            for k in KEYWORDS: # Цикл ключевым по словам
                if k in vacancy:
                    suitable_vacancies[vacancy] = []
                    employer = serp.find('a', class_='bloko-link_kind-tertiary').text
                    link = serp.find('a')['href'] # Ссылка на вакансию
                    city = serp.find('div', attrs={'data-qa': 'vacancy-serp__vacancy-address'}, class_='bloko-text').text.split(' ')[0]
                    salary = serp.find('span', class_='bloko-header-section-3') # Вилка зп
                    if salary is None:
                        sum_ = 'не указана'
                    else:
                        sum_ = salary.text

                    pattern_sum = r'(\d+)(\s)(\d{3})'
                    pattern_com = r'([О]+)(\s)(\w+)'
                    substitution = r'\1 \3'
                    summa = re.sub(pattern_sum, substitution, sum_)
                    company = re.sub(pattern_com, substitution, employer)

                    suitable_vacancies[vacancy].append({'Компания': company, 'Город': city, 'Зарплата': summa, 'Ссылка': link})

        # pprint(suitable_vacancies)
        with open(full_path, "w") as f:
          json.dump(suitable_vacancies, f, indent=5)




# with open('vacancy.json', 'r' ) as f:
#     rows = json.load(f)
#
# pprint(rows)