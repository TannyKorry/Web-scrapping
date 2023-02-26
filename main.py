import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
from fake_headers import Headers
import os


def get_head():
    headers = Headers(browser='yandex', os='win')
    return headers.generate()


path = os.path.join(os.getcwd())
full_path = os.path.join(path, 'vacancy.json')

for page in range(0, 2):
    url = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2&page=' + str(page)

    KEYWORDS = ['Django', 'Flask']

    resp = requests.get(url, headers=get_head())
    resp.raise_for_status()
    for resp.status_code in range(200, 300):
        response = resp.text

        soup = BeautifulSoup(response, features='lxml')

        vacancy_list = soup.find_all('div', class_='serp-item')

        suitable_vacancies = {}
        for serp in vacancy_list:
            vacancy = serp.find('a').text # Название профессии
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

                    suitable_vacancies[vacancy].append({'Компания': employer, 'Город': city, 'Зарплата': sum_, 'Ссылка': link})

        pprint(suitable_vacancies)
        with open(full_path, "w") as f:
          json.dump(suitable_vacancies, f, indent=5)



#
# with open('vacancy.txt', 'r', encoding='utf8') as f:
#     rows = json.load(f)
#     contacts_list = list(rows)  # дает список списков из файла
# print(rows)