import requests
from bs4 import BeautifulSoup
import re


# obraz = '''<article id="717862" data-navigatable="" tabindex="0" class="tm-articles-list__item"><div class="tm-article-snippet tm-article-snippet"><div class="tm-article-snippet__meta-container"><div class="tm-article-snippet__meta"><span class="tm-user-info tm-article-snippet__author"><a href="/ru/users/SmallDonkey/" title="SmallDonkey" class="tm-user-info__userpic"><div class="tm-entity-image"><img alt="" height="32" src="//habrastorage.org/r/w32/getpro/habr/avatars/126/f6c/178/126f6c178fc6b9e90c08f71200079d85.jpg" width="32" class="tm-entity-image__pic"></div></a> <span class="tm-user-info__user"><a href="/ru/users/SmallDonkey/" class="tm-user-info__username">
#       SmallDonkey
#       <!----></a> <span class="tm-article-datetime-published"><time datetime="2023-02-19T11:17:42.000Z" title="2023-02-19, 14:17">48 минут назад</time></span></span></span></div> <!----></div> <h2 class="tm-article-snippet__title tm-article-snippet__title_h2"><a href="/ru/post/717862/" data-article-link="" class="tm-article-snippet__title-link"><span>Как я делаю OCR</span></a></h2> <div class="tm-article-snippet__stats"><div class="tm-article-complexity tm-article-complexity_complexity-low"><span class="tm-svg-icon__wrapper tm-article-complexity__icon"><svg height="24" width="24" class="tm-svg-img tm-svg-icon"><title>Уровень сложности</title> <use xlink:href="/img/megazord-v28.78dd0d98..svg#complexity-low"></use></svg></span> <span class="tm-article-complexity__label">
#     Простой
#   </span></div> <div class="tm-article-reading-time"><span class="tm-svg-icon__wrapper tm-article-reading-time__icon"><svg height="24" width="24" class="tm-svg-img tm-svg-icon"><title>Время на прочтение</title> <use xlink:href="/img/megazord-v28.78dd0d98..svg#clock"></use></svg></span> <span class="tm-article-reading-time__label">
#     1 мин
#   </span></div> <span class="tm-icon-counter tm-data-icons__item"><svg height="24" width="24" class="tm-svg-img tm-icon-counter__icon"><title>Количество просмотров</title> <use xlink:href="/img/megazord-v28.78dd0d98..svg#counter-views"></use></svg> <span class="tm-icon-counter__value">376</span></span></div> <div class="tm-article-snippet__hubs-container"><div class="tm-article-snippet__hubs"><span class="tm-article-snippet__hubs-item"><a href="/ru/hub/machine_learning/" class="tm-article-snippet__hubs-item-link"><span>Машинное обучение</span> <span title="Профильный хаб" class="tm-article-snippet__profiled-hub">*</span></a></span></div></div> <div class="tm-article-snippet__labels-container"><div class="tm-article-snippet__labels"><!----> <div class="tm-article-snippet__label tm-article-snippet__label tm-article-snippet__label_variant-recovery"><span>
#           Recovery mode
#         </span></div></div></div> <!----> <div class="tm-article-body tm-article-snippet__lead"><div class="tm-article-snippet__cover tm-article-snippet__cover_cover"><img src="https://habrastorage.org/getpro/habr/upload_files/05b/1ba/e46/05b1bae461c41721938178d3d7b041b0.jpg" class="tm-article-snippet__lead-image" style="object-position:0% 0%;"></div> <div><div><div class="article-formatted-body article-formatted-body article-formatted-body_version-2"><p>Привет меня зовут Игорь, в свободное от основной профессии время я интересуюсь машинным обучением и занимаюсь разработкой OCR для мобильных устройств.</p><p>Современные решения OCR насколько мне известно в большинстве случаев состоят из двух компонентов, детектирование текста и последующее распознавание.</p><p>Для обучения требуется много качественно размеченных данных, и в случае с детектированием текста это настоящая проблема, найти в открытом доступе большой качественный датасет очень сложно.</p><p>Для решения проблемы я написал собственную программу для разметки данных.</p><p>Работа в программе должна быть проста предельно проста и эффективна, увеличение и уменьшение изображения, перетаскивание, создание и удаление объектов, разметка происходит только с помощью мышки.</p><p></p></div></div> <div class="v-portal" style="display: none;"></div> <div class="v-portal" style="display: none;"></div></div> <a href="/ru/post/717862/" class="tm-article-snippet__readmore"><span>Читать далее</span></a></div></div> <div class="tm-data-icons"><!----> <div class="tm-votes-meter tm-data-icons__item"><svg height="24" width="24" class="tm-svg-img tm-votes-meter__icon tm-votes-meter__icon tm-votes-meter__icon_appearance-article"><title>Всего голосов 1: ↑1 и ↓0</title> <use xlink:href="/img/megazord-v28.78dd0d98..svg#counter-rating"></use></svg> <span title="Всего голосов 1: ↑1 и ↓0" class="tm-votes-meter__value tm-votes-meter__value tm-votes-meter__value_positive tm-votes-meter__value_appearance-article tm-votes-meter__value_rating">+1</span></div> <!----> <button title="Добавить в закладки" type="button" class="bookmarks-button tm-data-icons__item"><span class="tm-svg-icon__wrapper bookmarks-button__icon"><svg height="24" width="24" class="tm-svg-img tm-svg-icon"><title>Добавить в закладки</title> <use xlink:href="/img/megazord-v28.78dd0d98..svg#counter-favorite"></use></svg></span> <span title="Количество пользователей, добавивших публикацию в закладки" class="bookmarks-button__counter">
#     4
#   </span></button> <div title="Читать комментарии" class="tm-article-comments-counter-link tm-data-icons__item"><a href="/ru/post/717862/comments/" class="tm-article-comments-counter-link__link"><svg height="24" width="24" class="tm-svg-img tm-article-comments-counter-link__icon"><title>Комментарии</title> <use xlink:href="/img/megazord-v28.78dd0d98..svg#counter-comments"></use></svg> <span class="tm-article-comments-counter-link__value">
#       1
#     </span></a> <a href="/ru/post/717862/comments/" class="tm-article-comments-counter-link__link"><span title="Читать новые комментарии" class="tm-article-comments-counter-link__unread-counter">
#       +1
#     </span></a></div> <!----> <div class="v-portal" style="display:none;"></div></div></article>'''

url = 'https://habr.com/ru/all/'

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

resp = requests.get(url)
response = resp.text

soup = BeautifulSoup(response, features='lxml')
#1
pattern =r'\d{6}\b'

ID_list = re.findall(pattern, response)
# print(ID_list)
id_viewed = ''
for id_article in ID_list:
    # print(f'\n{id_article}\n')
    if id_article != id_viewed:
        print(f'\n{id_article}\n')
        article = soup.find(id=id_article)
        id_viewed = id_article
    print(article)
# span = id.find('span')
#
# df = span.text
# print(df)





