from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
import json, scrapy, custom_settings_config, os


class AmazonbooksSpider(scrapy.Spider):
    name = 'amazon-books'
    allowed_domains = ['amazon.co.uk']
    start_urls = ['https://www.amazon.co.uk/dp/178685807X']
    custom_settings = custom_settings_config.custom_settings

    def parse(self, response):
        yield{
            "book_url": response.url,
            'author': response.css('#bylineInfo .a-link-normal::text').getall(),
            'book_title': response.css('#productTitle::text').get(),
            'price': response.css('.a-color-price::text').get(),
            'cover': response.css('#main-image::attr(src)').get()
        }