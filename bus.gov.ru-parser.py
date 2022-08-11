'''

Парсер сайта bus.gov.ru по запросу, который вводится в переменной purpose
Если будет пустая страница - будет ошибка, но это просто исправить
Сделан с помощью selenium + beautifulsoup
Не сохраняет в файл


'''

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common import by
from bs4 import BeautifulSoup
from time import sleep
from tqdm import tqdm


browser = Chrome('chromedriver.exe')
url = 'https://bus.gov.ru/registry'

browser.get(url)
input_tab = browser.find_element(by.By.CLASS_NAME, 'search-input')
purpose = 'Онкологический диспансер'
input_tab.send_keys(purpose)
input_tab.send_keys(Keys.ENTER)
sleep(3)

hospitals =[]

for i in range(10):
    sleep(3)
    for el in browser.find_elements(by.By.CLASS_NAME, 'result'):
        sleep(2)
        try:
            print(el.find_element(by.By.CLASS_NAME, 'advanced-result__number').text)
        except:
            print('xz')
        try:
            link = el.find_element(by.By.CLASS_NAME, 'result__title').get_attribute('href')
        except:
            link = el.find_element(by.By.CLASS_NAME, 'result__common_title').text
        try:
            name = el.find_element(by.By.CLASS_NAME, 'result__title').text
        except:
            name = 'Отсутствует'
        try:
            location = el.find_element(by.By.CLASS_NAME, 'result__location').text
        except:
            location = 'Отсутствует'
        try:
            phone_number = el.find_element(by.By.CLASS_NAME, 'result__phone').text
        except:
            phone_number = 'Отсутствует'
        try:
            self_link = el.find_element(by.By.CLASS_NAME, 'result__url').text
        except:
            self_link = 'Отсутствует'
        print(f'Ссылка на gov.ru - {link}\nНазвание организации - {name}\nАдрес - {location}\nНомер телефона - {phone_number}\nСсылка на собственный сайт - {self_link}\n\n')

    try:
        browser.find_element(by.By.CSS_SELECTOR, 'body > div.main > ui-view > ui-view-ng-upgrade > ui-view > app-registry > div.results > div > div:nth-child(3) > div > div.b-controls__left_40.pagination_box1 > app-pagination > div > div > div.info-section-paginator__next.ng-star-inserted').click()
    except:
        break

print('End!')

input()

