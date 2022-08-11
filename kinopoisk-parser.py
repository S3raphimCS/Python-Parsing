'''

Парсер кинопоиска по всем страницам в разделе лучших 250 фильмов
Сделан с помощью requests и beautifulsoup
Не сохраняет в файл

'''
import requests
from bs4 import BeautifulSoup
from time import sleep

counter = 0

for i in range(1, 6):
    try:
        print(f'Страница №{i}')
        sleep(2)
        url = f'https://www.kinopoisk.ru/lists/movies/top250/?page={i}'
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        for film in soup.findAll('div', class_='styles_root__ti07r'):
            counter += 1
            print(f'Фильм №{counter}')
            name = film.find('div', class_='base-movie-main-info_mainInfo__ZL_u3').find('span', class_='styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj').text
            eng_name = film.find('span', class_='desktop-list-main-info_secondaryText__M_aus').text
            rating = film.find('div', class_='styles_user__2wZvH').find('div', class_='styles_kinopoisk__JZttS').find('span', class_='styles_kinopoiskValuePositive__vOb2E styles_kinopoiskValue__9qXjg').text
            print(name)
            print(eng_name)
            print(rating)
            sleep(1)
    except:
        print('Ошибка в выполнении...')

