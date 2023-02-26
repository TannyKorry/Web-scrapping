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


def create_f_json():
    path = os.path.join(os.getcwd())
    full_path = os.path.join(path, 'vacancy.json')
    return full_path


def find_vacancies(page=20):
    KEYWORDS = ['Flask', 'Django']
    suitable_vacancies = {}
    for page in range(0, page):
        url = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2&page=' + str(page)

        resp = requests.get(url, headers=get_head())
        resp.raise_for_status()
        if resp.status_code in range(200, 300):
            response = resp.text

            soup = BeautifulSoup(response, features='lxml')

            vacancy_list = soup.find_all('div', class_='serp-item')

            for serp in vacancy_list:
                vacancy = serp.find('a').text
                for k in KEYWORDS:
                    if k in vacancy:
                        suitable_vacancies[vacancy] = []
                        employer = serp.find('a', class_='bloko-link_kind-tertiary').text
                        link = serp.find('a')['href']
                        city = serp.find('div', attrs={'data-qa': 'vacancy-serp__vacancy-address'},
                                         class_='bloko-text').text.split(' ')[0]
                        salary = serp.find('span', class_='bloko-header-section-3')
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
    return suitable_vacancies


def write_json():
    with open(create_f_json(), "w") as f:
        json.dump(find_vacancies(), f, indent=5)


def read_json():
    with open('vacancy.json', 'r') as f:
        result = json.load(f)
        return result


if __name__ == '__main__':

# Подобрать вакансии
    pprint(find_vacancies())

# Записать подборку в файл json
    write_json()

# Прочитать готовый файл json
#     pprint(read_json())