'''
Дата создания - 25.05.2023
Данный код скрапит раздел "Классическая проза" на сайте Лабиринт средствами библиотеки scrapy
Ссылка на раздел - https://www.labirint.ru/genres/2787/?page=1
Кол-во страниц на момент создания - 17
Запускается командой - scrapy crawl labirint -O books.json (Вместо json можно указать другой тип файла) - из директории "labirint parser"
'''

import scrapy
from re import split as splt


class BookSpider(scrapy.Spider):
    name = 'labirint'
    start_urls = ['https://www.labirint.ru/genres/2787/?page=1']

    def parse(self, response):
        for link in response.css('div.genres-carousel__container div.genres-carousel__item a.product-title-link::attr(href)'):
            yield response.follow(link, callback=self.parse_book)

        for i in range(1, 17):
            next_page = f'https://www.labirint.ru/genres/2787/?page={i}'
            yield response.follow(next_page, callback=self.parse)

    def parse_book(self, response):
        yield{
            'name': response.css('div.prodtitle h1::text').get()[response.css('div.prodtitle h1::text').get().find(': ')+2:],
            'author': response.css('div.authors a::text').get(),
            'publisher': response.css('div.publisher a::text').get(),
            'price': response.css('div.buying-pricenew-val span::text').get() + " руб." if response.css('div.buying-pricenew-val span::text').get() else response.css('div.buying-price span.buying-price-val-number::text').get() + ' руб.',
            'id': response.css('div.articul::text').get().split(': ')[1],
            'rating': response.css('div.left div::text').get() + f'(Оценок:{splt(r"[(,),:]", response.css("div.block1 div div::text").get())[-2]})',
        }
