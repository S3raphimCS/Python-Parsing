'''

Парсер с помощью selenium сохраняет основную информацию по квартирам в Хабаровске и 
сохраняет в json, но пока только в unicode шифровке
Все завернуто в отладчики и имеет неформатированный вывод в консоль по одной квартире

'''
from pydoc import classname, text
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common import by
from bs4 import BeautifulSoup
from time import sleep
import json

browser = Chrome('C:/Users/123/Desktop/chromedriver.exe')
url = 'https://www.avito.ru/'
browser.get(url)


#Заходим на Харабровск
browser.find_element(by.By.CLASS_NAME, 'main-select-JJyaZ').click()
browser.find_element(by.By.CLASS_NAME, 'suggest-input-rORJM').click()
browser.find_element(by.By.CLASS_NAME, 'suggest-input-rORJM').send_keys('Хабаровск')
sleep(2)
browser.find_element(by.By.CLASS_NAME, 'suggest-suggests-CzXfs').find_element(by.By.CLASS_NAME, 'suggest-suggest-uk_Ib').click()
browser.find_element(by.By.CLASS_NAME, 'popup-buttons-WICnh').find_element(by.By.CLASS_NAME, 'button-button-CmK9a').click()


#Ищем квартиры и парсим
browser.find_element(by.By.CLASS_NAME, 'input-input-Zpzc1').send_keys('Квартира')
browser.find_element(by.By.CLASS_NAME, 'input-input-Zpzc1').send_keys(Keys.ENTER)
sleep(2)
try:
    i = 1
    result_list = []
    flat_number = 1
    while browser.find_element(by.By.CLASS_NAME, 'pagination-item_arrow-Sttbt'):
        flats = browser.find_element(by.By.CLASS_NAME, 'items-items-kAJAg').find_elements(by.By.CLASS_NAME, 'iva-item-root-_lk9K')
        print(f'Страница №{i}')
        for flat in flats:
            
            try:
                href = flat.find_element(by.By.CLASS_NAME, 'link-link-MbQDP').get_attribute('href')
            except:
                href = 'ашипка'

            try:
                title = str(flat.find_element(by.By.CLASS_NAME, 'iva-item-content-rejJg').find_element(by.By.CLASS_NAME, 'iva-item-body-KLUuy').find_element(by.By.CLASS_NAME, 'iva-item-titleStep-pdebR').find_element(by.By.CLASS_NAME, 'link-link-MbQDP').find_element(by.By.CLASS_NAME, 'title-root-zZCwT').text)
                title = title.split(', ')
                rooms = title[0][0]
                area = title[1]
                floor = title[2]
            except:
                title = 'Нет'
                title = 'Нет'
                rooms = 'Нет'
                area  = 'Нет'
                floor = 'Нет'

            try:
                price = flat.find_element(by.By.CLASS_NAME, 'iva-item-content-rejJg').find_element(by.By.CLASS_NAME, 'iva-item-body-KLUuy').find_element(by.By.CLASS_NAME, 'iva-item-priceStep-uq2CQ').find_element(by.By.CLASS_NAME, 'price-root-RA1pj').find_element(by.By.CLASS_NAME, 'price-text-_YGDY').text
            except:
                prict = 'Нет'

            try:
                price_for_meter = flat.find_element(by.By.CLASS_NAME, 'iva-item-content-rejJg').find_element(by.By.CLASS_NAME, 'iva-item-body-KLUuy').find_element(by.By.CLASS_NAME, 'iva-item-priceStep-uq2CQ').find_element(by.By.CLASS_NAME, 'price-root-RA1pj').find_element(by.By.CLASS_NAME, 'price-noaccent-X6dOy').text
            except:
                price_for_meter = 'Нет'
            
            try:
                complex = flat.find_element(by.By.CLASS_NAME, 'iva-item-content-rejJg').find_element(by.By.CLASS_NAME, 'iva-item-body-KLUuy').find_element(by.By.CLASS_NAME, 'iva-item-developmentNameStep-qPkq2').find_element(by.By.CLASS_NAME, 'iva-item-text-Ge6dR').text
            except:
                complex = 'Скрыт'
            
            try:
                street = flat.find_element(by.By.CLASS_NAME, 'iva-item-content-rejJg').find_element(by.By.CLASS_NAME, 'iva-item-body-KLUuy').find_element(by.By.CLASS_NAME, 'iva-item-developmentNameStep-qPkq2').find_element(by.By.CLASS_NAME, 'geo-root-zPwRk').find_element(by.By.CLASS_NAME, 'geo-address-fhHd0').text
            except:
                street = 'Нет'
            
            try:
                region = flat.find_element(by.By.CLASS_NAME, 'iva-item-content-rejJg').find_element(by.By.CLASS_NAME, 'iva-item-body-KLUuy').find_element(by.By.CLASS_NAME, 'iva-item-developmentNameStep-qPkq2').find_element(by.By.CLASS_NAME, 'geo-root-zPwRk').find_element(by.By.CLASS_NAME, 'geo-georeferences-SEtee').text
            except:
                region = 'Нет'
            
            try:
                seller_link = flat.find_element(by.By.CLASS_NAME, 'style-link-STE_U').get_attribute('href')
            except:
                seller_link = 'Скрыта'

            try:   
                deals = ((flat.find_element(by.By.CLASS_NAME, 'iva-item-aside-GOesg').find_element(by.By.CLASS_NAME, 'iva-item-text-Ge6dR').text).split())[0]
            except:
                deals = 'Нет'


            result_list.append({flat_number:[{'Ссылка на объявление':href, 
                                'Кол-во комнат': rooms, 
                                'Площадь': area,
                                'Этаж': floor,
                                'Стоимость': price,
                                'Стоимость за кв. метр': price_for_meter,
                                'Название жилого района': complex,
                                'Улица': street,
                                'Район': region,
                                'Завершенных объявлений': deals,
                                'Ссылка на продавца': seller_link
                                }]})


            flat_number += 1
            print(result_list[-1])
            print()
            print()
        i += 1
        browser.find_element(by.By.CLASS_NAME, 'pagination-item_arrow-Sttbt').click()
        sleep(2)


except Exception as error:
    print('Возникла ошибка: ', end='')
    print(error)


#Кодирует в Unicode ;c
with open('flats.txt', 'w') as f:
    for element in result_list:
        json.dump(element, f)
        json.dump('\n', f)


print(result_list)
print('Работа завершена')
